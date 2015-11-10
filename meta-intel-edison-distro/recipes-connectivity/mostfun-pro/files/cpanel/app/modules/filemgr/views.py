# !/usr/bin/env python
# coding: utf-8
'''

'''
import json

from flask import request, render_template

# from run import app
from . import filemgr, FileManage
from app import PATH_
from ..utils import login_required_

__author__ = 'Jux.Liu'


@filemgr.route('/fileManage')
@login_required_
def fileManage():
    """
打开文件管理页面
    :param: null
    :return:
    """
    return render_template('fileManage.html')

@filemgr.route('/get_fileManage', methods=['GET', 'POST'])
def get_fileManage():
    return render_template('fileManage.html')


@filemgr.route('/upload-file', methods=['GET', 'POST'])
@login_required_
def upload():
    """
上传文件动作
    :param: null
    :return:
    """
    if request.method == 'POST':
        file = request.files['upfile']
        # fm=FileManage()
        # return fm.uploadFile(file)
        res = FileManage().uploadFile(file)
        return json.dumps(res)


@filemgr.route('/del/<FileName>', methods=['POST', 'GET'])
@login_required_
def delFile(FileName):
    FileName = FileName.split("\\")[-1].split(".")[0]
    res = FileManage().delFile(FileName)
    # return json.dumps(res)
    if res["result"]:
        return "ok"
    else:
        return "false"

@filemgr.route('/dels', methods=['POST', 'GET'])
@login_required_
def delsFile():
    if request.method == "POST":
        filenames = request.form.get('data')
        filenames_list = filenames.split(',')
        filenames_list.pop()
        for item in filenames_list:
            item = item.split('.')
            item.pop()
            res = FileManage().delFile(item[0])
            if not res["result"]:
                return "false"
        return "ok"

