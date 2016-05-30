#!/usr/bin/env python
# coding:utf-8
from configobj import ConfigObj

from app import g_p_

TASKMGRFILE = g_p_.LocalPath + 'TASKMGRFILE.ini'
taskList = ConfigObj(g_p_.LocalPath + 'config.ini', encoding='UTF8')


def record(self, gcode):
    config.add_section("book")
    pass


def load(self, number):
    pass


def taskList(self):
    # taskList.sections()
    pass
