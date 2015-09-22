# !/usr/bin/env python
# coding: utf-8
'''

'''

__author__ = 'Jux.Liu'

import time
import platform
import glob
import os

from flask import json, send_from_directory, render_template

from . import device
from .printer import mostfun
from ..utils import login_required_
from ... import PATH_

sysstr = platform.system()
# 检测平台，指定相关路径
PATH_['m'] = mostfun()
PATH_['m'].reset()


@device.route('/send/<command>')
@login_required_
def send(command):
    """
向设备发送操纵命令
    :param command: 命令
    :return: String: 错误信息/ done
    """
    try:
        PATH_['m'].sendCommand(str(command))
    except Exception as e:
        return str(e)
    else:
        return 'done'


@device.route('/get/<name>')
@login_required_
def getData(name):
    """
获取设备相关信息
    :param name:
    :return:
    """
    if name == 'ok':
        return 'ok'
    if name == 'state':
        if PATH_['m'].state == 'printing' or PATH_['m'].state == 'pause':
            state = PATH_['m'].state
            fileName = os.path.basename(PATH_['m']._filePath)
            layerCount = PATH_['m']._g._layerCount
            return json.dumps([state, fileName, layerCount])
        return json.dumps([PATH_['m'].state])
    if name == 'layernum':
        return str(PATH_['m']._g._layerNum)
    if name == 'alltemp':
        alltempdata = ['%d' % PATH_['m']._extruderTemp, '%d' % PATH_['m']._bedTemp,
                       '%d' % PATH_['m']._extruderTargetTemp, '%d' % PATH_['m']._bedTargetTemp]
        return json.dumps(alltempdata)
    if name == 'extrudertemp':
        return '%d' % PATH_['m']._extruderTemp
    if name == 'extrudertargettemp':
        return '%d' % PATH_['m']._extruderTargetTemp
    if name == 'bedtemp':
        return '%d' % PATH_['m']._bedTemp
    if name == 'bedtargettemp':
        return '%d' % PATH_['m']._bedTargetTemp
    if name == 'filelist':
        # todo: read sd card
        filePathList = glob.glob(PATH_['GcodePath'] + '*.gcode')
        fileInfoTable = list()
        for filePath in filePathList:
            # file_check = ""
            fileName = os.path.basename(filePath).decode('utf-8')
            fileContent = 'mostfun model'
            fileSize = "%.2f" % (os.path.getsize(filePath) / 1024.0 / 1024.0)
            fileTime = time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getctime(filePath)))
            # button = " "
            fileInfoList = [fileName, fileContent, fileSize, fileTime]
            fileInfoTable.append(fileInfoList)
        return json.dumps(fileInfoTable)


@device.route('/print/<GcodeFileName>')
@login_required_
def toPrint(GcodeFileName):
    """
打印操作
    :param GcodeFileName:
    :return:
    """
    PATH_['m'].beginTask(PATH_['GcodePath'] + GcodeFileName.encode(encoding='UTF-8', errors='strict'))
    return "ok"


@device.route('/pause')
@login_required_
def pause():
    """
暂停打印动作
    :param: null
    :return:
    """
    PATH_['m'].pauseTask()
    return "ok"


@device.route('/resume')
@login_required_
def resume():
    """
恢复打印动作
    :param: null
    :return:
    """
    PATH_['m'].resumeTask()
    return "ok"


@device.route('/reset', methods=['GET', 'POST'])
@login_required_
def reset():
    """
强制停机操作
    :param: null
    :return:
    """
    # TODO: 功能未明确是否完成
    # TODO: Reset功能只在Linux上生效，详见models.py
    PATH_['m'].reset()

    # del m
    # m = mostfun('/dev/ttyMFD1')
    # models.Init()
    return "ok"


@device.route('/cancel', methods=['GET', 'POST'])
@login_required_
def cancel():
    """
强制停机操作
    :param: null
    :return:
    """
    PATH_['m'].cancelTask()
    return "ok"


@device.route('/model/<FileName>')
@login_required_
def getModel(FileName):
    """

    :param FileName:
    :return:
    """
    # TODO: 3D模型库
    ext = FileName.split('.')[-1]
    if ext == 'stl' or ext == 'obj':
        folder = PATH_['ModelPath']
        return send_from_directory(folder, FileName)
    elif ext == 'jpg' or ext == 'png':
        folder = PATH_['ModelImgPath']
        return send_from_directory(folder, FileName)
    elif ext == 'gcode':
        folder = PATH_['GcodePath']
        return send_from_directory(folder, FileName)


@device.route('/3dv/<StlFileName>')
@login_required_
def threedv(StlFileName):
    """

    :param StlFileName:
    :return:
    """
    # TODO: 不清楚作用
    return render_template('3dv.html', StlFileName=StlFileName)


@device.route('/UI/<Button>')
@login_required_
def LCDControl(Button):
    if Button is None:
        return
    controlList = {'L': '', 'R': '', 'D': '', 'DL': '', 'DR': '', 'DD': ''}
    return controlList[Button]
