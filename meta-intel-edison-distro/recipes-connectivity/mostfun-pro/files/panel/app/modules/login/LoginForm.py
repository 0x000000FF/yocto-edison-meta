# !/usr/bin/env python
# coding: utf-8
'''
Login页面Form
'''

from flask.ext.wtf import Form
from wtforms import SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired

__author__ = 'Jux.Liu'


class LoginForm(Form):
    '''
    登录页
    '''
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField(u"记住我!")
    submit = SubmitField(u"登录")


