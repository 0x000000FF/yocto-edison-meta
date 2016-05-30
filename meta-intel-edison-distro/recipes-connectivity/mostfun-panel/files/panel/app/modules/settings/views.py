#!/usr/bin/env python
# coding: utf-8
'''

'''
import json
import shutil
import subprocess
from os import remove
from os.path import exists
from time import sleep

from flask import request, session, current_app, render_template

from app import g_p_, logger
from app.modules.device import wifi4edison
from app.modules.utils.Utils import getINI, modINI
from . import settings
from ..user import User
from ..utils import login_required_, Update, m

__author__ = 'Jux.Liu'


@settings.route('/get-version/')
def get_version():
    pv = current_app.config['CP_VERSION']
    sv = current_app.config['SYS_VERSION']
    if pv is not None and sv is not None:
        return json.dumps({'panel': pv, 'system': sv})
    else:
        return json.dumps({'code': 18})


@settings.route('/get-mail-setting/')
def get_mail_setting():
    param = m.get_config()
    param['mail_enabled'] = getINI('mail', 'enabled')
    if param is None or len(param) != 8:
        return json.dumps({'code': 19})
    param['code'] = 1
    return json.dumps(param)


@settings.route('/change-password/', methods=['GET', 'POST'])
@login_required_
def changePwd():
    """
修改设备登陆密码
    :return:
    """
    old_password = request.get_json()['old_password']
    new_password = request.get_json()['new_password']
    rpt_password = request.get_json()['rpt_password']
    if rpt_password == new_password:

        user = User(session.get('id'))  # UserID通过session取
        pwd_res = user.changePassword(old_password, new_password)

        if pwd_res['result']:
            # todo: 发送的消息内容需要再做修改
            m.send_mail(title="Password changed", content="Your password has been changed.")
            return json.dumps({'result': True, 'msg': '/logout', 'code': 1})

    return json.dumps({'code': 20})


@settings.route('/get-wireless-list/', methods=['POST', 'GET'])
@login_required_
def getWirelessList():
    """
修改设备无线配置
    :param: null
    :return: wireless.html
    """
    wifi_map = wifi4edison.scanForNetworks()
    if wifi_map:
        return json.dumps(wifi_map)
    else:
        return json.dumps('')


@settings.route('/get-current-wifi/', methods=['GET', 'POST'])
@login_required_
def getCurrWifi():
    return json.dumps(wifi4edison.checkNetwork())


@settings.route('/connect-wifi/', methods=['POST'])
@login_required_
def connect_wifi():
    ssid = request.get_json()['ssid']
    secure = request.get_json()['secure']
    password = request.get_json()['password']
    try:
        connect = wifi4edison.configureNetwork(ssid, secure, password)
        wifi4edison.setNetwork(connect)
    except Exception as e:
        logger.error(e)
        res = {'code': 22}
    else:
        res = wifi4edison.checkNetwork()
        logger.info('wifi changed')
    finally:
        return json.dumps(res)


@settings.route('/config-wpa/', methods=['POST'])
@login_required_
def config_wpa():
    ssid = request.get_json()['ssid']
    wpapsk = request.get_json()['password']
    result = False
    msg = ''
    if len(wpapsk) < 8:
        msg = 'password shuld longer than 8 characters.'
    else:
        subprocess.call("sed -i -e 's/^WPAPSK=.*/WPAPSK='{0}'/g' /etc/Wireless/RT2870AP/RT2870AP.dat".format(wpapsk),
                        shell=True)
        subprocess.call("sed -i -e 's/^SSID=.*/SSID='{0}'/g' /etc/Wireless/RT2870AP/RT2870AP.dat".format(ssid),
                        shell=True)
        subprocess.call('systemctl restart hostapd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        result = True

    return json.dumps({'code': 1 if result else 23})


@settings.route('/enable-email/', methods=['GET', 'POST'])
@login_required_
def mailEnable():
    res = {'code': 27}
    enabled = request.get_json()['enabled']
    if modINI(section='mail', option='enabled', value=enabled):
        res['code'] = 1
    return json.dumps(res)


@settings.route('/change-mail/', methods=['GET', 'POST'])
@login_required_
def changeMail():
    """
修改设备推送邮箱和接收推送的邮箱
    :return:
    """
    param = {"nickname"   : request.get_json()['nickname'],
             "password"   : request.get_json()['password'],
             "smtp_server": request.get_json()['smtp_server'],
             "prefix"     : request.get_json()['prefix'],
             "to_addr"    : request.get_json()['to_addr'],
             "from_addr"  : request.get_json()['from_addr'],
             'port'       : request.get_json()['port']}

    res = m.change_config(params=param)

    # 这里必须写英文，否则会报错：'ascii' codec can't decode byte 0xe9 in position 0: ordinal not in range(128)。推测是flask本身的问题。
    return json.dumps({'code': 1 if res else 26})


@settings.route('/getLang/')
def getLang():
    return json.dumps({'lang': getINI(section='other', option='lang')})


@settings.route('/setLang/', methods=['POST', 'GET'])
def setLang():
    lang = request.get_json()['lang']
    res = modINI(section='other', option='lang', value=lang)
    return json.dumps({'code': 1 if res else 29})


@settings.route('/chk-update/')
@login_required_
def chkUpdate():
    fn = r'/tmp/upgradelist.txt'
    if exists(fn):
        pass
    else:
        subprocess.call('systemctl start checkupdate', shell=True)

    flag = True
    while flag:
        sleep(1)
        p = subprocess.Popen('systemctl status checkupdate | grep Active', shell=True, stdout=subprocess.PIPE)
        p.wait()
        out = p.stdout.readlines()[0].strip().split(':')
        if 'inactive' in out[1]:
            flag = False
    with open(fn) as f:
        details = f.readlines()
    if len(details) == 0:
        remove(fn)
    return json.dumps(details)


@settings.route('/get-update-process/')
def getUpdateProcess():
    return json.dumps({'process': g_p_.update_process, 'total': g_p_.total_process})


@settings.route('/waiting-update/')
def waitUpdate():
    return render_template('waitingUpdate.html')


@settings.route('/do-update/')
@login_required_
def doUpdate():
    res = {'code': 25}
    if g_p_.mostfun.state not in ['ready', 'error']:
        pass

    else:
        g_p_.total_process=3
        g_p_.update_process = 1
        g_p_.mostfun.state = 'updating'
        g_p_.mostfun.close_serial()
        subprocess.call('systemctl start blink-led', shell=True)
        sleep(3)
        subprocess.call('systemctl start checkpackages', shell=True)
        flag = True
        while flag:
            sleep(3)
            p = subprocess.Popen('systemctl status checkpackages | grep Active', shell=True, stdout=subprocess.PIPE)
            p.wait()
            out = p.stdout.readlines()[0].strip().split(':')
            if 'inactive' in out[1]:
                g_p_.update_process=2
                flag = False
        g_p_.mostfun.open_serial()
        g_p_.update_process = 3
        g_p_.mostfun.state = 'ready'
        with open(r'/tmp/upgrade.txt') as f:
            if 'Configured' in f.readlines()[-1]:
                res = {'code': 1}
            else:
                res = {'code': 25}

    g_p_.update_process = 0
    subprocess.call('systemctl stop blink-led', shell=True)
    return json.dumps(res)


# def chkSysUpdate():
#     return Update.check_sys_update()
#
#
# def chkCpUpdate():
#     return Update.check_panel_2560_update()


@settings.route('/space-left/')
@login_required_
def spaceLeft():
    p = subprocess.Popen('df | grep /mmcblk0p10', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = p.stdout.readline().split()
    p.terminate()
    return json.dumps({'total': data[1], 'used': data[2]})


@settings.route('/recovery/')
def recovery():
    return json.dumps(Update.recovery())


@settings.route('/get-cdn/')
def get_cdn():
    cdn = getINI('other', 'cdn')
    if len(cdn):
        return json.dumps({'code': 1, 'cdn': cdn})
    else:
        return json.dumps({'code': 32})


def testSpeed(url):
    from urllib2 import urlopen
    from datetime import datetime
    sumSpan = 0.0
    for i in range(10):
        startTime = datetime.now()
        try:
            urlopen(url, timeout=10)
        except:
            pass
        endTime = datetime.now()
        span = (endTime - startTime).microseconds / 1000.0
        print(span)
        sumSpan = sumSpan + span

    return '%.0f' % (sumSpan / 10.0)


@settings.route('/change-cdn/', methods=['POST'])
@login_required_
def changeCDN():
    cdn = request.get_json()['cdn']
    if cdn in CDN_list and modINI('other', 'cdn', cdn):
        path = r'/etc/opkg/'
        cdnname = cdn + 'feeds'
        filename = 'feeds.conf'
        shutil.copy(path + cdnname, path + filename)

        return json.dumps({'code': 1})
    else:
        return json.dumps({'code': 33})


CDN_list = {'cn': 'http://update.mostfun.cc',
            'hk': 'http://update.mostfun.cc',
            'eu': 'http://update.mostfun.cc',
            'us': 'http://update.mostfun.cc'}


@settings.route('/test-cdn/')
@login_required_
def testCDN():
    speed_list = {'cn': 0,
                  'hk': 0,
                  'eu': 0,
                  'us': 0}
    for item in CDN_list:
        speed_list[item] = testSpeed(CDN_list[item])
    return json.dumps(speed_list)
