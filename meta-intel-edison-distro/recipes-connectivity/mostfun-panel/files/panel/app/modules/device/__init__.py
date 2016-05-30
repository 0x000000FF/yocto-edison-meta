#!/usr/bin/env python
# coding: utf-8
'''

'''
__author__ = 'Jux.Liu'

from flask import Blueprint

device = Blueprint('device', __name__)

from . import models, printer, taskmgr, views, wifi4edison
