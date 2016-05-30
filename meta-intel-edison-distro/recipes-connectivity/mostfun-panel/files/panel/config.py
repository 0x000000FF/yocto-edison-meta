#!/usr/bin/env python
# coding: utf-8
'''
配置项
'''

import os
import subprocess

__author__ = 'Jux.Liu'

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'MOSTFUN'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    CTRL_ADMIN = os.environ.get('CTRL_ADMIN') or 'admin'

    __p = subprocess.Popen('opkg list-installed | grep mostfun', shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    CP_VERSION = __p.stdout.readlines()[-1].strip()

    __p = subprocess.Popen('uname -r', shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    SYS_VERSION = __p.stdout.readline()
    __p.terminate()

    SYS_UPDATE_URL = r'http://update.mostfun.cc/firmware/'
    VERSION_FILE = 'version.ini'
    INTRO_FILE = 'whatsnew.txt'
    SYS_FILE = 'toFlash.tar.gz'

    BAK_LIST = [r'/etc/Wireless/RT2870AP/RT2870AP.dat',
                r'/etc/wpa_supplicant/wpa_supplicant.conf']
    BAK_PATH = r'/home/backup/'

    ERR_CODE = {
        20: 'No System Update',
        21: 'No Panel Update',
        22: 'No 2560 Update',
        23: 'System Update Error',
        24: 'Panel Update Error',
        25: '2560 Update Error',
        26: 'Printing Now, Cancel Update'
    }
    MSG_CODE = {
        20: 'New System Version: {0}',
        21: 'New Panel Version: {0}',
        22: 'New 2560 Version: {0}',
        23: 'System Update Success',
        24: 'Panel Update Success',
        25: '2560 Update Success'
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                                                                'dev-data.sqlite')


class TestingConfing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,
                                                                                                 'test-data.sqlite')


class ProductionConfing(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing'    : TestingConfing,
    'production' : ProductionConfing,
    'default'    : DevelopmentConfig
}
