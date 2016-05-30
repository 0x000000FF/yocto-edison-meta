#!/usr/bin/env python
# coding: utf-8
'''

'''

from flask import Blueprint

__author__ = 'Jux.Liu'

user = Blueprint('user', __name__)

from .User import User
