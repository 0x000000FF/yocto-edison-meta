# -*- coding:utf-8 -*-
"""

"""
import argparse as ap
import smtplib
import sys
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from configobj import ConfigObj

import os
import shutil
from os.path import exists

__author__ = 'Jux.Liu'

bkcfg = '{0}{1}'.format(r'/home/backup/', 'mail-config.ini')
lccfg = '{0}{1}'.format(r'/mostfun/mail-tool/', 'mail-config.ini')


def modINI(option, value, section='mail', filename=lccfg):
    """
修改配置文件内容
    :param section: 配置标签名称
    :param option: 配置项名称
    :param value: 配置项值
    :param filename: 配置文件名
    """
    config = ConfigObj(filename, encoding='UTF8')
    res = ''
    try:
        if len(section):
            config[section][option] = value
        else:
            config[option] = value
        config.write()
        res = True
    except Exception as e:
        res = False
    finally:
        return res


def getINI(option, section='mail', filename=lccfg):
    value = ''
    config = ConfigObj(filename, encoding='UTF8')
    try:
        if len(section) and len(option):
            value = config[section][option]
        elif len(section):
            value = config[section]
        elif len(option):
            value = config[option]
        else:
            raise Exception
    except Exception as e:
        value = ''
    finally:
        return value


def checkINI(section='mail', filename=lccfg):
    config = ConfigObj(filename, encoding='UTF8')
    keys = [u'smtp_server', u'to_addr', u'from_addr', u'nickname', u'password', u'port', u'prefix']
    options = config[section].keys()
    # 必须用定死的来匹配生成的
    for item in keys:
        if item in options:
            continue
        else:
            return False
    return True


class MAIL():
    def __init__(self):
        self.from_addr = getINI('from_addr')
        self.nickname = getINI('nickname')
        self.password = getINI('password')
        self.to_addr = getINI('to_addr')
        self.smtp_server = getINI('smtp_server')
        self.prefix = getINI('prefix')
        self.port = getINI('port')

    def organize_msg(self, subject, msg, attach_file=None):
        _ = self.msg = MIMEMultipart()

        try:
            if len(attach_file) != 0:
                with open(attach_file, 'rb') as fh:
                    self.mime = MIMEBase(_maintype='image',
                                         _subtype=attach_file.split('.').pop(),
                                         filename=attach_file.split(os.sep).pop())
                    self.mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
                    self.mime.add_header('Content-ID', '<0>')
                    self.mime.add_header('X-Attachment-Id', '0')
                    self.mime.set_payload(fh.read())
                    encoders.encode_base64(msg=self.mime)
                    self.msg.attach(payload=self.mime)
                    # todo: mod msg template
        except Exception as e:
            # todo: mod msg template
            pass
        finally:
            _.attach(MIMEText(msg, 'html', 'utf-8'))
            _['From'] = _format_addr('mostfun <{0}>'.format(self.from_addr))
            _['To'] = _format_addr('{0} <{1}>'.format(self.nickname, self.to_addr))
            _['Subject'] = Header(s='{0}: {1}'.format(self.prefix, subject), charset='utf-8').encode()

    def send(self):
        res = False
        try:
            _ = self.server = smtplib.SMTP(host=self.smtp_server)  # todo: 测试是否有邮箱需要使用port参数
            _.starttls()
            _.set_debuglevel(debuglevel=1)
            _.login(user=self.from_addr, password=self.password)
            _.sendmail(from_addr=self.from_addr, to_addrs=[self.to_addr], msg=self.msg.as_string())
            _.quit()
            res = True
        except Exception as e:
            raise e
        finally:
            return res


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(s=name, charset='utf-8').encode(), addr))


def main(*args):
    if args[0].config is not None:
        cfg = eval(args[0].config)
        for key in cfg:
            value = cfg[key]
            if len(value) > 0:
                modINI(option=key, value=value)
        global lccfg
        global bkcfg
        shutil.copyfile(lccfg, bkcfg)
        print('set config: ok')
        return 0
    elif args[0].subject is not None or args[0].msg is not None or args[0].attach is not None:
        m = MAIL()
        m.organize_msg(subject=args[0].subject, msg=args[0].msg, attach_file=args[0].attach)
        if m.send():
            print('send mail: ok')
            return 0
        else:
            print('send mail: error')
            return 1
    elif args[0].getconfig is not None:
        cfg = {'smtp_server': getINI('smtp_server'),
               'to_addr'    : getINI('to_addr'),
               'from_addr'  : getINI('from_addr'),
               'nickname'   : getINI('nickname'),
               'password'   : getINI('password'),
               'prefix'     : getINI('prefix'),
               'port'       : getINI('port')
               }
        print('the config-dict is: {0}'.format(cfg))
        return 0


def app_init():
    global lccfg
    global bkcfg
    if not exists(bkcfg):
        shutil.copyfile(lccfg, bkcfg)
    if not exists(lccfg) or not checkINI():
        print(3)
        shutil.copyfile(bkcfg, lccfg)


if __name__ == "__main__":
    app_init()
    p = ap.ArgumentParser()
    p.add_argument('-s', '--subject', action='store')
    p.add_argument('-m', '--msg', action='store')
    p.add_argument('-a', '--attach', action='store')
    p.add_argument('-c', '--config', action='store')
    p.add_argument('-g', '--getconfig', action='store_true')
    args, remaining = p.parse_known_args(sys.argv)
    main(args)
