#!/usr/bin/env python
# coding:utf-8
from configobj import ConfigObj

from app import PATH_

TASKMGRFILE = PATH_['HomePath'] + '/TASKMGRFILE.ini'
taskList = ConfigObj(PATH_['HomePath'] + '/config.ini', encoding='UTF8')


def record(self, gcode):
    config.add_section("book")
    pass


def load(self, number):
    pass


def taskList(self):
    # taskList.sections()
    pass
