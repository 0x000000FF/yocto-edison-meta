#!/usr/bin/env python
# coding:utf-8

# from flask.ext.login import UserMixin,login_required

from configobj import ConfigObj

from ... import g_p_


class mfconfig(object):
    passWord = ''
    uploadPath = ''
    gcodePath = ''
    serialPort = ''
    serialBaud = 0
    fileBuffer = 0

    @staticmethod
    def loadConfig(self):
        config = ConfigObj(g_p_.LocalPath + 'config.ini', encoding='UTF8')
        self.passWord = config['passwd']['password']
        self.uploadPath = config['path']['uploadPath']
        self.gcodePath = config['path']['gcodePath']
        self.serialPort = config['mostfun']['serialPort']
        self.serialBaud = config['mostfun']['serialBaud']
        self.fileBuffer = config['mostfun']['fileBuffer']


class upgradeTool(object):
    def upgradeAVR(self):
        text = 'avrdude -Cavrdude.conf -v -v -v -v -patmega2560 -cwiring -P \'/dev/ttyMFD1\' -b115200 -D -Uflash:w:\\xxx.hex:i'
        pass

    def upgradeEdison(self):
        pass

    def upgradeWRTnode(self):
        pass


class modelToGcode(object):
    def Cura(self):
        pass


class modeling(object):
    def __init__(self):
        pass


class outageContinued(object):
    def check(self):
        pass

    def record(self):
        pass

    def completed(self):
        pass
