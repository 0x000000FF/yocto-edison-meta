#!/usr/bin/env python
# coding: utf-8
'''
login 路由定义
'''

import random

from flask import render_template, redirect, url_for, request, session
from flask.ext.login import login_user, current_user, logout_user

from app import login_manager
from . import login
from .LoginForm import LoginForm
from ..user import User
from ..utils import login_required_

__author__ = 'Jux.Liu'


@login.route('/login', methods=['POST', 'GET'])
def loginPage():
    '''
登录页面
    :param: null
    :return: login.html
    '''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    style = 'none'
    if form.validate_on_submit():
        # random.randint(),用于创建1到100之间的随机数，用于唯一标识当前用户
        # 现在程序只有一个用户，暂且不考虑随机生成的数有重复的状况
        user_id = random.randint(1, 3)
        user = User(user_id)
        if user.password == form.password.data:
            session['id'] = user_id
            session['password'] = user.password
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            style = 'block'
    return render_template("login.html", form=form, style=style)


@login.route("/logout", methods=['POST', 'GET'])
@login_required_
def logoutPage():
    """
登出操作
    :param: null
    :return: 重定向到 login.html
    """
    logout_user()
    session['id'] = None
    session['password'] = None
    return redirect(url_for(".loginPage"))


@login_manager.user_loader
def load_user(user_id):
    """
加载用户的回调函数，接收惟一表示用户的id标识符，如果
能找到用户，则返回用户对象，否则返回None
    :param user_id: 接收到的用户id
    :return: 用户对象
    """
    user = User(user_id)
    if user.id == user_id:
        return user
    else:
        return None
