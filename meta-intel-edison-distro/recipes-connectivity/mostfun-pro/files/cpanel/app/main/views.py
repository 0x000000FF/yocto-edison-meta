# !/usr/bin/env python
# coding: utf-8
'''

'''

import os
import codecs
import json

from flask import render_template, send_from_directory, request

from CPanel import app
from . import main
from ..modules.utils import login_required_


__author__ = 'Jux.Liu'


@main.route('/')
@main.route('/index')
@login_required_
def index():
    """
打开主页面
    :param: null
    :return: index.html
    """
    # return render_template('index.html')
    return render_template('base.html')

@main.route('/get_index', methods=['GET', 'POST'])
def get_index():
    return render_template('index.html')


@main.route('/most3d')
@login_required_
def most3d():
    """
打开 3DMOST 模型库页面
    :param: null
    :return:
    """
    return render_template('most3d.html')

@main.route('/get_most3d', methods=['GET', 'POST'])
def get_most3d():
    return render_template('most3d.html')



@main.route('/wizard')
@login_required_
def wizard():
    """
打开向导页面
    :param: null
    :return:
    """
    return render_template('wizard.html')

@main.route('/get_wizard', methods=['GET', 'POST'])
def get_wizard():
    return render_template('wizard.html')



@main.route('/app')
@login_required_
def getapp():
    """
打开 APP 下载页面
    :param: null
    :return: app.html
    """
    return render_template('app.html')


@main.route('/help')
@login_required_
def help():
    """
打开帮助页面
    :param: null
    :return: help.html
    """
    return render_template('help.html')

@main.route('/get-help', methods=['GET', 'POST'])
def get_help():
    if request.method == 'POST':
        dir = 'app/md/'
        filename = request.form['file_name']
        filedir = dir + filename + '.md'
        file = codecs.open(filedir, mode='r', encoding='utf8')
        text = file.read()
        return json.dumps(text)


@main.route('/favicon.ico')
def favicon():
    """
站点图标设置
    :param: null
    :return:
    """
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')