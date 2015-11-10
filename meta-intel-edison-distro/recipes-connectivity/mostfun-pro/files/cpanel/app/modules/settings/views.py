# !/usr/bin/env python
# coding: utf-8
'''

'''
import json
import subprocess

from flask import url_for, redirect, render_template, request, session, current_app

from . import settings
from app import PATH_
from app.modules.utils.Utils import createQR, getINI, modINI
from ..user import User
from ..utils import login_required_
# from ..device import wifi4edison
from ..utils import SMail

__author__ = 'Jux.Liu'


# @settings.route('/settings', methods=['GET', 'POST'])
# @login_required_
# def settingPage(param={'pwd': '', 'mail': ''}):
#     """
# 打开设置页面
#     :param: null
#     :return: setting.html
#     """
#     return render_template('settings.html', currentCPfrimware=current_app.config['CP_VERSION'],
#                            currentSYSfrimware=current_app.config['SYS_VERSION'], changePwdmsg=param['pwd'],
#                            changeMailmsg=param['mail'])


@settings.route('/get_settings', methods=['GET', 'POST'])
def get_settings(param={'pwd':'', 'mail':''}):
    return render_template('settings.html', currentCPfrimware=current_app.config['CP_VERSION'],
                           currentSYSfrimware=current_app.config['SYS_VERSION'], changePwdmsg=param['pwd'],
                           changeMailmsg=param['mail'])


@settings.route('/change-password', methods=['GET', 'POST'])
@login_required_
def changePwd():
    """
修改设备登陆密码
    :return:
    """
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    user = User(session.get('id'))  # UserID通过session取
    res = user.changePassword(old_password, new_password)
    if res['result']:
        # 测试邮件发送是否成功
        # SendMail初始化格式(邮件内容，附件名称（附件地址在SendMail类中设置))
        send = SMail()
        # TODO: 邮件内容需要修改
        send.send_mail("修改成功了！")

        return redirect(url_for('login.logoutPage'))
    else:
        # TODO: 组织错误信息，必须是ascii
        return settingPage({'pwd': 'fail', 'mail': ''})


wifi_map = None


# @settings.route('/get-wireless-list', methods=['POST', 'GET'])
# @login_required_
# def getWirelessList():
#     """
# 修改设备无线配置
#     :param: null
#     :return: wireless.html
#     """
#     global wifi_map
#     wifi_map = wifi4edison.scanForNetworks()
#     if wifi_map:
#         pass
#     else:
#         wifi_map = ''
#     result = json.dumps(wifi_map)
#     return result


# @settings.route('/get-current-wifi', methods=['GET', 'POST'])
# @login_required_
# def getCurrWifi():
#     return json.dumps({'ssid':wifi4edison.checkNetwork()})


# @settings.route('/connect-wifi', methods=['POST'])
# @login_required_
# def connect_wifi():
#     global wifi_map
#     ssid = request.form['ssid'];
#     password = request.form['password'];
#     connect = wifi4edison.configureNetwork(wifi_map, ssid, password)
#     wifi4edison.setNetwork(connect)
#     createQR()
#
#     return json.dumps(wifi4edison.checkNetwork())


@settings.route('/config_wpa', methods=['POST'])
@login_required_
def config_wpa():
    ssid = request.form['ssid']
    wpa_passphrase = request.form['password']
    result = False
    msg = ''
    if len(wpa_passphrase) < 8:
        msg = 'password shuld longer than 8 characters.'
    else:
        if modINI(section='', option='wpa_passphrase', value=wpa_passphrase, filename=r'/etc/hostapd/hostapd.conf') \
                and modINI(section='', option='ssid', value=ssid, filename=r'/etc/hostapd/hostapd.conf'):
            subprocess.call('systemctl restart hostapd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = True
        else:
            msg = 'unknow error.'

    return json.dumps({'result': result, 'msg': msg})


@settings.route('/change-mail', methods=['GET', 'POST'])
@login_required_
def changeMail():
    """
修改设备推送邮箱和接收推送的邮箱
    :return:
    """
    param = {"username": request.form['send_mail'],
             "password": request.form['send_password'],
             "server": request.form['mail_server'],
             "prefix": request.form['prefix'],
             # "sender": request.form['sender'],
             "target": request.form['target_mail'],
             'port': request.form['mail_port']}

    mail = SMail()
    res = mail.change_config(params=param)

    # 这里必须写英文，否则会报错：'ascii' codec can't decode byte 0xe9 in position 0: ordinal not in range(128)。推测是flask本身的问题。
    return settingPage({'pwd': '', 'mail': 'ok'})


@settings.route('/getLang')
def getLang():
    return json.dumps({'lang': getINI(section='other', option='lang')})


@settings.route('/setLang', methods=['POST'])
def setLang():
    lang = request.form['lang']
    return json.dumps(modINI(section='other', option='lang', value=lang))


@settings.route('/chk-sys-update')
def chkSysUpdate():
    url = current_app.config['SYS_UPDATE_URL']
    file = current_app.config['VERSION_FILE']
    from app.modules.filemgr import FileManage
    fm = FileManage()
    res = fm.downloadFile(url=url + file, path=PATH_['sysUpdatePath'])
    if not res['result']:
        return json.dumps({'result': False, 'msg': 'chkFail'})

    vf = open(PATH_['sysUpdatePath'] + 'version.txt', 'r')
    sysversion = vf.read()
    vf.close()
    if cmp(sysversion, current_app.config['SYS_VERSION']):
        # 无更新
        return json.dumps({'result': False, 'msg': 'noUpdate'})

    file = current_app.config['INTRO_FILE']
    fm.downloadFile(url=url + file, path=PATH_['sysUpdatePath'])
    vf = open(PATH_['sysUpdatePath'] + 'whatsnew.txt', 'r')
    updateDetail = vf.readlines()
    vf.close()
    return json.dumps({'msg': updateDetail, 'result': True})


@settings.route('/update-sys', methods=['POST'])
def updateSys():
    print 'update-sys'
    url = current_app.config['SYS_UPDATE_URL']
    file = current_app.config['SYS_FILE']
    from app.modules.filemgr import FileManage
    fm = FileManage()
    fm.downloadFile(url=url + file, path=PATH_['sysUpdatePath'])
    subprocess.call('rm -fr /update/*', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    res = fm.unZip(PATH_['sysUpdatePath'], 'toFlash.zip', r'/update/')
    if not res['result']:
        return json.dumps(res)
    # 执行更新
    subprocess.call('reboot ota', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


@settings.route('/chk-cp-update')
@login_required_
def chkCpUpdate():
    subprocess.call('opkg update', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen('opkg list-upgradable', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    res = p.stdout.readlines()
    flag = False
    msg = ''
    if len(res) == 0:
        msg = 'noUpdate'
    else:
        for item in res:
            if item.startswith('mostfun-pro'):
                flag = True
                break
    print res
    if not flag:
        msg = 'noMostfunUpdate'
    return json.dumps({'msg': msg, 'result': flag})


@settings.route('/update-cp', methods=['POST'])
@login_required_
def updateCP():
    print 'update-cp'
    if PATH_['m'].state == 'printing' or PATH_['m'].state == 'pause':
        return json.dumps({'msg': 'isPrinting', 'result': False})

    flag = False
    # 调用OPKG下载
    p = subprocess.Popen('opkg upgrade', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    res = p.stdout.readlines()
    print res
    for item in res:
        if item.endswith('mostfun-pro.\n'):
            print 'up to date'
            flag = True

    if not flag:
        print 'update Fail'
        return json.dumps({'msg': 'updateFail', 'result': False})
    # 解压缩
    cmd = PATH_['decode'] + ' ' + PATH_['HomePath'] + 'mostfun.des3'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    res = p.stdout.readlines()
    for item in res:
        if item.endswith('records in\n') or item.endswith('records out\n'):
            subprocess.call('shutdown -r now', shell=True)
    print 'decode Fail'
    return json.dumps({'msg': 'decodeFail', 'result': False})


@settings.route('/space-left')
@login_required_
def spaceLeft():
    p = subprocess.Popen('df | grep /mmcblk0p10', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = p.stdout.readline().split()
    p.terminate()
    print data
    return json.dumps({'total': data[1], 'used': data[2]})
