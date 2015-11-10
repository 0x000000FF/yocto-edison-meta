# !/usr/bin/env python
# coding: utf-8
'''

'''

from functools import wraps
import os

from configobj import ConfigObj
from flask.ext.login import current_user, current_app
from flask import redirect, url_for, request

from app import PATH_

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
        elif not current_user.is_authenticated():
            # return current_app.login_manager.unauthorized()
            return redirect(url_for("login.loginPage", next=request.url))  # 为什么是写函数名称？蓝图的原因？
        return func(*args, **kwargs)

    return decorated_view


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
    if os.path.exists(srcPath) and not os.path.exists(destPath):
        shutil.copy(srcPath, destPath)


def getLocalIP(ifname='wlan0'):
    import socket, fcntl, struct

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
    ret = socket.inet_ntoa(inet[20:24])
    return ret


def createQR():
    import qrcode
    from PIL import Image

    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=1
    )
    qr.add_data(getLocalIP(ifname='wlan0'))
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGB")

    icon = Image.open(r'/home/gif/wireless_signal.png')
    icon = icon.convert('RGBA')

    img_w, img_h = img.size
    factor = 2
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h), mask=icon)

    img.save(r'/home/gif/qr.bmp')


def modINI(section, option, value=None, filename=PATH_['HomePath'] + '/config.ini'):
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
        res = False
    finally:
        return {'result': res}


def getINI(section, option, filename=PATH_['HomePath'] + '/config.ini'):
    config = ConfigObj(filename, encoding='UTF8')
    try:
        if len(section):
            value = config[section][option]
        else:
            value = config[option]
    except Exception, e:
        value = ''
    finally:
        return value


def modCfgMail():
    current_app.config.update(
        MAIL_SERVER=getINI('mail', 'server'),
        MAIL_PORT=int(getINI('mail', 'port')),
        MAIL_USERNAME=getINI('mail', 'username'),
        MAIL_PASSWORD=getINI('mail', 'password'),
    )

