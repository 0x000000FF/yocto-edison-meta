# !/usr/bin/env python
# coding: utf-8
"""
发送电子邮件
"""
from configobj import ConfigObj

from app.modules.utils.Utils import modINI, modCfgMail

__author__ = 'tao'

from threading import Thread
from flask import current_app
from flask.ext.mail import Message,Mail
from app import PATH_

cf = ConfigObj(PATH_['HomePath'] + '/config.ini', encoding='UTF8')


class SMail():
    def __init__(self):
        """
邮件配置
        :param content: 邮件内容
        :param attachments: 邮件附件
        """
        modCfgMail()
        self.mail = Mail(current_app)
        self.mail_prefix = cf["mail"]["prefix"]
        # mail_sender必须与邮箱登陆用户相同
        self.mail_sender = cf['mail']['username']
        self.target = cf["mail"]["target"]
        # 设置附件的默认存放地址
        self.dir = PATH_['PrtPic']

    def send_async_email(self, app, msg):
        with app.app_context():
            self.mail.send(msg)

    def send_mail(self, content="", attachments=None):
        app = current_app._get_current_object()
        msg = Message(self.mail_prefix + u"mostfun mail", sender=self.mail_sender, recipients=[self.target])
        msg.body = content
        if attachments:
            filename = self.dir + attachments
            with app.open_resource(filename) as fp:
                msg.attach(filename, "image/jpg", fp.read())
        thr = Thread(target=self.send_async_email, args=[app, msg])
        thr.start()
        return thr

    def change_config(self,
                      params={"username": '', "password": '', "server": '', "prefix": '', "sender": '', "target": ''}):
        for p in params:
            if params[p]:
                modINI('mail', p, params[p])
        return {'result': True, 'msg': '邮箱修改成功'}
