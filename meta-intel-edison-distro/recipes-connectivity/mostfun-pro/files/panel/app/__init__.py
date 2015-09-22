# !/usr/bin/env python
# coding: utf-8
'''

'''
import os
import platform

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

from config import config

__author__ = 'Jux.Liu'

bootstrap = Bootstrap()
login_manager = LoginManager()
mail = Mail()
PATH_ = {'m': None,
         'HomePath': os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/',
         }


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    sysstr = platform.system()  # 检测平台，指定相关路径
    if (sysstr == "Windows"):
        PATH_['GcodePath'] = r'c:/mostfuncp/gcode/'
        PATH_['ModelPath'] = r'c:/mostfuncp/model/'
        PATH_['ModelImgPath'] = r'c:/mostfuncp/img/'
        PATH_['ModelZipPath'] = r'c:/mostfuncp/zip/'
        PATH_['TmpFolder'] = r'c:/mostfuncp/tmp/'
        PATH_['PrtPic'] = r'c:/'
        PATH_['decode'] = r'c:/'
    elif (sysstr == "Linux"):
        PATH_['GcodePath'] = r'/home/mostfuncp/gcode/'
        PATH_['ModelPath'] = r'/home/mostfuncp/model/'
        PATH_['ModelImgPath'] = r'/home/mostfuncp/img/'
        PATH_['ModelZipPath'] = r'/home/mostfuncp/zip/'
        PATH_['TmpFolder'] = r'/home/mostfuncp/tmp/'
        PATH_['PrtPic'] = r'/home/mostfuncp/'
        PATH_['decode'] = r'/home/decode.mostfun'
        PATH_['sysUpdatePath'] = r'/home/'

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

    return app
