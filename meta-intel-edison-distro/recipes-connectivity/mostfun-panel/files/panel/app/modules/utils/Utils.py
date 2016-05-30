#!/usr/bin/env python
# coding: utf-8
'''

'''

import os
from functools import wraps

from configobj import ConfigObj
from flask import redirect, url_for, request
from flask.ext.login import current_user, current_app

from app import g_p_, logger

__author__ = 'Jux.Liu'


def login_required_(func):
    """
    重写的login_required函数，用于验证当前访问用户是否登录
    :param func:
    :return:
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            # return current_app.login_manager.unauthorized()
            return redirect(url_for("login.loginPage", next=request.url))  # 为什么是写函数名称？蓝图的原因？
        return func(*args, **kwargs)

    return decorated_view


def mail_enabled(func):
    @wraps(func)
    def decorate_view(*args, **kwargs):
        if getINI('mail', 'enabled').upper() != 'FALSE':
            return func(*args, **kwargs)
        else:
            return None

    return decorate_view


def encodeChinese(cnStr):
    """
    将传入的中文字符串编码成 \x01\x23\x45 的形式
    :param cnStr: 传入的中文字符串
    :return: 编码后的字符串
    """
    pass


def deleteFileFolder(src, delself=False):
    """
删除指定目录下的文件和文件夹
    :param src: 指定目录
    :param delself: 是否删除目录自身
    """
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            deleteFileFolder(itemsrc)
    if delself:
        try:
            os.rmdir(src)
        except:
            pass


def copyFile(srcPath, destDir):
    """
拷贝文件到指定目录
    :param srcPath: 文件路径
    :param destDir: 目标路径
    """
    import shutil

    fileName = os.path.basename(srcPath)
    destPath = destDir + os.path.sep + fileName
    if os.path.exists(srcPath):
        shutil.copy(srcPath, destPath)


def getLocalIP(ifname='wlan0'):
    import socket, fcntl, struct

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    ret = socket.inet_ntoa(inet[20:24])
    return ret


def modINI(section, option, value=None, filename=g_p_.LocalPath + 'config.ini'):
    """
修改配置文件内容
    :param section: 配置标签名称
    :param option: 配置项名称
    :param value: 配置项值
    :param filename: 配置文件名
    """
    config = ConfigObj(filename, encoding='UTF8')
    res = ''
    try:
        if len(section):
            config[section][option] = value
        else:
            config[option] = value
        config.write()
        res = True
    except Exception, e:
        logger.error('mod ini error, value: [{0}]{1}={2}'.format(section, option, value))
        res = False
    finally:
        copyFile(filename, g_p_.cfgbak)
        return res


def getINI(section, option, filename=g_p_.LocalPath + 'config.ini'):
    config = ConfigObj(filename, encoding='UTF8')
    try:
        if len(section) and len(option):
            value = config[section][option]
        elif len(section):
            value = config[section]
        elif len(option):
            value = config[option]
        else:
            raise
    except Exception, e:
        logger.error('get ini error, value: [{0}]{1}'.format(section, option))
        value = ''
    finally:
        return value
