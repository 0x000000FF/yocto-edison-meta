#!/usr/bin/env python
# coding: utf-8
'''

'''

from flask import Blueprint

from SMail import SMail

__author__ = 'Jux.Liu'

utils = Blueprint('utils', __name__)
m=SMail()

from .Utils import login_required_, copyFile, deleteFileFolder
from .CustomFields import ButtonButtonField, ButtonInputField
from MobileDetector import MobileDetector
from . import m

mobile_detector = MobileDetector()