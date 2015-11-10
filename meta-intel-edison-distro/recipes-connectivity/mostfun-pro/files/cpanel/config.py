# !/usr/bin/env python
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
    MAIL_SERVER=None
    MAIL_PORT=None
    MAIL_USERNAME=None
    MAIL_PASSWORD=None
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True

    __p = subprocess.Popen('opkg list-installed | grep mostfun', shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    CP_VERSION = __p.stdout.readline()

    __p = subprocess.Popen('uname -r', shell=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    SYS_VERSION = __p.stdout.readline()
    __p.terminate()

    SYS_UPDATE_URL = r'http://update.mostfun.cc/firmware/'
    VERSION_FILE = 'version.txt'
    INTRO_FILE = 'whatsnew.txt'
    SYS_FILE = 'toFlash.zip'

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
    'testing': TestingConfing,
    'production': ProductionConfing,
    'default': DevelopmentConfig
}
