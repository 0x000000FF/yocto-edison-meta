# !/usr/bin/env python
# coding: utf-8
'''

'''

from os import environ, getenv

from app import create_app

__author__ = 'Jux.Liu'

app = create_app(getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        # 编辑以下路径文件最后一行来修改默认启动界面的端口，解决端口冲突问题/usr/lib/edison_config_tools/edison-config-server.js
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 5555
    # app.debug=True,debug=True,threaded=True
    app.run('0.0.0.0', PORT, debug=False, threaded=True)
