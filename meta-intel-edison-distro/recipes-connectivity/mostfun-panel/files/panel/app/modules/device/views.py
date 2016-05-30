#!/usr/bin/env python
# coding: utf-8
'''

'''
import math
import platform
from datetime import datetime as dt

import os
from app.modules.device.printer import mostfun
from app.modules.filemgr import FileManage
from flask import json, send_from_directory, render_template, request
from . import device
from ..utils import login_required_, mobile_detector, m
from ... import g_p_, logger

__author__ = 'Jux.Liu'

sysstr = platform.system()
# 检测平台，指定相关路径
g_p_.mostfun = mostfun()
g_p_.mostfun.reset()


@device.route('/send/<command>/')
@login_required_
def send(command):
    """
向设备发送操纵命令
    :param command: 命令
    :return: String: 错误信息/ done
    """
    if g_p_.mostfun.send_command([command]):
        res = 1
    else:
        res = 31

    return json.dumps({'code': res})


@device.route('/cmd_msg/')
@login_required_
def cmdMsg():
    return json.dumps({'result': g_p_.mostfun.web_box_getter()})


@device.route('/device/state/')
@login_required_
def getState():
    state = g_p_.mostfun.get_state()
    detail = ''
    if state == 'ready':
        pass
    else:
        fileName = os.path.basename(g_p_.mostfun._filePath)
        layerCount = g_p_.mostfun._g.layerCount
        layerNum = g_p_.mostfun._g.layerNum
        percent = g_p_.mostfun.get_percent()
        detail = {'fileName'  : fileName,
                  'layerCount': layerCount,
                  'layerNum'  : layerNum,
                  'percent'   : percent}

    return json.dumps({'result': True, 'msg': {'state': state, 'details': detail}})


@device.route('/device/temperature/')
@login_required_
def getTemper():
    alltempdata = {'extTemp'      : '%d' % g_p_.mostfun.get_extruderTemp(),
                   'bedTemp'      : '%d' % g_p_.mostfun.get_bedTemp(),
                   'extTargetTemp': '%d' % g_p_.mostfun.get_extruderTargetTemp(),
                   'bedTargetTemp': '%d' % g_p_.mostfun.get_bedTargetTemp()}
    return json.dumps(alltempdata)


@device.route('/print/', methods=['POST'])
@login_required_
def toPrint():
    """
打印操作
    :param GcodeFileName:
    :return:
    """
    data = request.get_json()
    ua = request.headers.get('User-Agent')
    if mobile_detector.process_request(ua):
        logger.info('printed by mobile browser')
    else:
        logger.info('printed by normal browser')

    if data['path'] != 3:
        logger.info('start task')
        location = g_p_.GcodePath
        res = 2
    else:
        logger.info('continue task')
        location = g_p_.PausedPath
        res = 3
    location = g_p_.folder[data['path']] + location

    if g_p_.mostfun.beginTask(location + data['filename'].encode(encoding='UTF-8', errors='strict')):
        return json.dumps({'code': 1})
    else:
        return json.dumps({'code': res})


@device.route('/pause/')
@login_required_
def pause():
    """
暂停打印动作
    :param: null
    :return:
    """
    logger.info('pause task')
    g_p_.mostfun.pauseTask()
    return json.dumps({'code': 1})


@device.route('/resume/')
@login_required_
def resume():
    """
恢复打印动作
    :param: null
    :return:
    """
    logger.info('resume task')
    g_p_.mostfun.resumeTask()
    return json.dumps({'code': 1})


@device.route('/reset/', methods=['GET', 'POST'])
@login_required_
def reset():
    """
强制停机操作
    :param: null
    :return:
    """
    # reset功能只在Linux上生效，详见models.py
    logger.warning('reset printer')
    g_p_.mostfun.reset()

    # del m
    # m = mostfun('/dev/ttyMFD1')
    # models.Init()
    return json.dumps({'code': 1})


@device.route('/cancel/', methods=['GET', 'POST'])
@login_required_
def cancel():
    """
强制停机操作
    :param: null
    :return:
    """
    logger.warning('cancel task')
    g_p_.mostfun.cancelTask()
    return json.dumps({'code': 1})


@device.route('/save-task/', methods=['GET', 'POST'])
@login_required_
def save():
    logger.info('save task')
    g_p_.mostfun.stop_saveTask()
    return json.dumps({'code': 1})


@device.route('/cancel-task/', methods=['GET', 'POST'])
@login_required_
def cancelTask():
    logger.warning('cancel task')
    filename = request.get_json()['filename']
    if FileManage().delFile(filename, flag=0):
        return json.dumps({'code': 1})
    else:
        return json.dumps({'code': 9})


@device.route('/model/', methods=['POST', 'GET'])
@login_required_
def getModel():
    """

    :param FileName:
    :return:
    """
    data = request.get_json()
    FileName = data['filename']
    folder = g_p_.folder[data['path']]

    ext = FileName.split('.')[-1]
    if ext == 'stl' or ext == 'obj':
        folder += g_p_.ModelPath
    # elif ext == 'jpg' or ext == 'png':
    #     folder += g_p_.ModelImgPath']
    elif ext == 'gcode':
        folder += g_p_.GcodePath
    fn = '{0}{1}'.format(folder, FileName)
    if os.path.exists(fn):
        sz = '%.2f' % (os.path.getsize(fn) / math.pow(1024, 2))
        if float(sz) > 20.0:
            return json.dumps({'code': 11})
        else:
            return send_from_directory(folder, FileName)
    else:
        return json.dumps({'code': 10})


@device.route('/UI/<Button>/')
@login_required_
def LCDControl(Button):
    if Button is None:
        return
    controlList = {'L': '', 'R': '', 'D': '', 'DL': '', 'DR': '', 'DD': ''}
    return controlList[Button]


def shotpic():
    import subprocess
    subprocess.Popen('echo \'0\' > /tmp/webcom', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


@device.route('/snapshot/')
def snapshot():
    shotpic()
    if not os.path.exists(r'/tmp/0.jpg') or os.path.getsize(r'/tmp/0.jpg') == 0.0 or \
                    (dt.now() - dt.utcfromtimestamp(os.stat(r'/tmp/0.jpg').st_ctime)).seconds > 1000:
        print('error')
        return send_from_directory(r'/tmp/', 'default.jpg', mimetype='application/octet-stream')
    print('no error')
    return send_from_directory(r'/tmp/', '0.jpg', mimetype='application/octet-stream')


@device.route('/webcam/')
def webcam():
    logger.info('webcam called')
    return render_template('webcam.html')


@device.route('/auto-leveling/')
@login_required_
def leveling():
    logger.info('web auto-leveling')
    return json.dumps({'code': 1 if g_p_.mostfun.auto_leveling() else 2})


@device.route('/take-photo/')
@login_required_
def takePic():
    try:
        for item in range(0, 5):
            shotpic()
    except Exception as e:
        return json.dumps({'code': 13})

    res = False
    times = 0
    while not res and times < 10:
        res = m.send_mail(title='Real time shot', content='Real time shot of your printing schedule',
                          attachments=r'/tmp/0.jpg')
        times += 1

    if res:
        logger.info('take photo and send ok')
        return json.dumps({'code': 1})
    elif res == None:
        return json.dumps({'code': 15})
    else:
        logger.error('take photo failed: send mail failed')
        return json.dumps({'code': 14})
