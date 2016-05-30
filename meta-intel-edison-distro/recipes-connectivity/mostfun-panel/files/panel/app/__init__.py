#!/usr/bin/env python
# coding: utf-8
'''

'''
import logging
import shutil
from os import mknod, listdir
from os.path import basename, splitext, isfile, join, isdir, exists, getsize

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager

from config import config

__author__ = 'Jux.Liu'

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
bootstrap = Bootstrap()
login_manager = LoginManager()


class GlobalParam(object):
    def __init__(self):
        self.mostfun = None
        self.RootPath = r'/mostfun/'
        self.HomePath = r'/home/'
        self.LocalPath = r'/mostfun/panel/'

        self.SDCard = r'/media/sdcard/'
        self.USB = r'/media/usb/'
        self.Flash = r'/home/mostfuncp/'
        self.PausedPath = r'/paused/'
        self.folder = [self.Flash, self.SDCard, self.USB, self.Flash]

        self.GcodePath = r'/gcode/'
        self.ModelPath = r'/model/'
        self.ModelImgPath = r'/img/'
        self.ModelZipPath = r'/zip/'

        self.TmpFolder = r'/tmp/'
        self.PrtPic = r'/tmp/'
        self.decode = r'/mostfun/decode.mostfun'

        self.log = r'/home/logs/'
        self.cfgbak = r'/home/backup/'
        self.update_list = {}

        self.update_process = 0
        self.total_process = 0


g_p_ = GlobalParam()


def GetFileList(dir, fileList):
    if isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif isdir(dir):
        for s in listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = join(dir, s)
            GetFileList(newDir, fileList)
    return fileList


lists = GetFileList('/home/logs/', [])
if len(lists):
    fn = int(splitext(basename(sorted(lists, key=lambda x: int(splitext(basename(x))[0]))[-1]))[0])
else:
    fn = 0

fn = '{0}{1}.log'.format(g_p_.log, 1 + fn)
mknod(fn)

logger = logging.getLogger('mlogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(fn)
fh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(filename)s | %(lineno)d | %(message)s \n'))
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

bkcfg = '{0}{1}'.format(g_p_.cfgbak, 'config.ini')
lccfg = '{0}{1}'.format(g_p_.LocalPath, 'config.ini')

if not exists(bkcfg):
    shutil.copyfile(lccfg, bkcfg)

if not exists(lccfg) or getsize(lccfg) < 10:
    shutil.copyfile(bkcfg, lccfg)


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .modules.utils import utils as utils_blueprint

    app.register_blueprint(utils_blueprint)

    from .modules.device import device as device_blueprint

    app.register_blueprint(device_blueprint)

    from .modules.user import user as user_blueprint

    app.register_blueprint(user_blueprint)

    from .modules.filemgr import filemgr as filemgr_blueprint

    app.register_blueprint(filemgr_blueprint)

    from .modules.settings import settings as settings_blueprint

    app.register_blueprint(settings_blueprint)

    from .modules.login import login as login_blueprint

    app.register_blueprint(login_blueprint)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    @app.after_request
    def ar(response):
        response.cache_control.max_age = 0
        return response

    return app
