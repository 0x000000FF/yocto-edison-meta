# !/usr/bin/env python
# coding: utf-8
'''

'''
from flask import Blueprint

__author__ = 'Jux.Liu'

login = Blueprint('login', __name__)

from . import views