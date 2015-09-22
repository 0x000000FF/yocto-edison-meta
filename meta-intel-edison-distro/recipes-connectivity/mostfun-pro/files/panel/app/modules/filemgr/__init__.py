# !/usr/bin/env python
# coding: utf-8
'''

'''
__author__ = 'Jux.Liu'
from flask import Blueprint

filemgr = Blueprint('FileManage', __name__)

from .FileManage import FileManage
from . import views
