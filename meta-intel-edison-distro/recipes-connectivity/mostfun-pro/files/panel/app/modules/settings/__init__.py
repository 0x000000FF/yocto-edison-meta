# !/usr/bin/env python
# coding: utf-8
'''

'''

from flask import Blueprint

__author__ = 'Jux.Liu'

settings = Blueprint('settings', __name__)

from . import views
