#!/usr/bin/env python
# coding: utf-8
"""
发送电子邮件
"""
import subprocess
from os.path import exists
from os import mknod

from app import g_p_
from app.modules.utils.Utils import mail_enabled

__author__ = 'tao'


class SMail():
    @mail_enabled
    def send_mail(self, title, content, attachments=None):
        cmd = 'python /mostfun/mail-tool/main.py -s "{0}" -m "{1}" -a "{2}"'.format(title, content, attachments)
        fn = '{0}{1}.txt'.format(g_p_.LocalPath, 'stdout')
        if not exists(fn):
            mknod(fn)
        with open(fn, 'w') as fh:
            subprocess.call(cmd, shell=True, stdout=fh, stderr=fh)
        with open(fn, 'r') as fh:
            res = fh.readlines()
            if len(res) >0:
                res = res[-1].split(": ")[-1].strip()
        if res == 'ok':
            return True
        else:
            return False

    def change_config(self,
                      params):
        if len(params) > 0 and isinstance(params, dict):
            cmd = 'python /mostfun/mail-tool/main.py -c "{0}"'.format(params)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            res = p.stdout.readline()
            res = res.split(': ')[-1].strip()
            if res == 'ok':
                return True
            else:
                return False

    def get_config(self):
        cmd = 'python /mostfun/mail-tool/main.py -g'
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        op = p.stdout.readline()
        res = eval(op.split('is: ')[-1])
        return res
