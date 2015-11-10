# !/usr/bin/env python
# coding: utf-8
'''
User类
'''

from flask.ext.login import UserMixin
from configobj import ConfigObj
from app import PATH_

from app.modules.utils.Utils import modINI

__author__ = 'Jux.Liu'


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "MostFun"
        config = ConfigObj(PATH_['HomePath'] + '/config.ini', encoding='UTF-8')
        self.password = config['passwd']['password']

    def __repr__(self):
        return "%s" % self.name

    def changePassword(self, oldPwd, newPwd):
        """
修改密码
        :param oldPwd: 旧密码
        :param newPwd: 新密码
        :return: {result: True成功/False失败, msg: 结果信息}
        """
        result = False
        msg = ''
        if oldPwd:
            if self.password != oldPwd:
                msg = u'原密码错误'
            else:
                if len(newPwd) == 0:
                    newPwd = 'mostfun'
                modINI(section='passwd', option='password', value=newPwd)
                result = True
                msg = u'修改成功'
        else:
            msg = u'原密码不可为空'
        return {'result': result, 'msg': msg.encode(encoding='UTF-8', errors='strict')}
