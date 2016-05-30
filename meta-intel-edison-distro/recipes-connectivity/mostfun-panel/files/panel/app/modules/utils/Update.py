# -*- coding:utf-8 -*-
"""
    Check System, Panel and 2560 updates.
"""
import shutil
import subprocess
from os import system
from os.path import exists
from time import sleep

from app import g_p_, logger
from app.modules.filemgr import FileManage
from app.modules.utils.Utils import getINI
from config import Config

__author__ = 'Jux.Liu'

file_manager = FileManage()
config = Config()


def check_sys_update():
    g_p_.update_process = 1  # start check sys update

    url = config.SYS_UPDATE_URL
    version_file = config.VERSION_FILE
    path = g_p_.HomePath

    # check update for system
    if exists(g_p_.SDCard + 'version.ini'):
        shutil.copy(g_p_.SDCard + 'version.ini', g_p_.HomePath)
        res = True
    elif exists(g_p_.USB + 'version.ini'):
        shutil.copy(g_p_.USB + 'version.ini', g_p_.HomePath)
        res = True
    else:
        res = file_manager.downloadFile(url=url + version_file, path=path)

    if res:
        sys_version = getINI('update', 'version', '{0}{1}'.format(g_p_.HomePath, config.VERSION_FILE))

        if sys_version.strip() == config.SYS_VERSION.strip():
            errcode = 20
            return {'result': False,
                    'msg'   : config.ERR_CODE[errcode]}
        else:
            msgcode = 20
            return {'result': True,
                    'msg'   : config.MSG_CODE[msgcode].format(sys_version)}

    else:

        errcode = 23
        return {'result': False,
                'msg'   : config.ERR_CODE[errcode]}


def check_panel_2560_update():
    g_p_.update_process = 2  # start check panel and marlin update

    # check update of panel and 2560
    subprocess.call('opkg update', shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen('opkg list-upgradable', shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    res = p.stdout.readlines()
    opkg = False

    if len(res):
        opkg = True

    return opkg


def start_update():
    if g_p_.mostfun.state not in ['ready', 'error']:

        # stop update, wait for print finish
        errcode = 26
        logger.warning('update failed: {0}'.format(config.ERR_CODE[errcode]))
        return {'result': False,
                'msg'   : config.ERR_CODE[errcode]}

    else:
        g_p_.mostfun.state = 'updating'
        g_p_.update_process = 0
        if g_p_.update_list['system_update']:
            update_sys()
        res = opkg_upgrade()
        if res:
            system('systemctl start panel-install')


def opkg_upgrade():
    g_p_.update_process += 1
    g_p_.mostfun.close_serial()
    # p = subprocess.Popen('opkg upgrade', shell=True,
    #                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen('systemctl start checkpackages', shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    g_p_.update_process += 1
    pr = p.stdout.readlines()
    for item in pr:
        if 'Configuring' in item:
            g_p_.mostfun.open_serial()
            return True
    g_p_.mostfun.open_serial()
    return False


def update_sys():
    g_p_.update_process += 1  # backup files
    logger.info('start updating system')
    for item in config.BAK_LIST:
        shutil.copy(item, config.BAK_PATH)
    # update sys
    url = config.SYS_UPDATE_URL
    file = config.SYS_FILE
    g_p_.update_process += 1  # start download
    print('{0}{1}'.format(url, file))
    if exists(g_p_.SDCard + 'toFlash.tar.gz'):
        shutil.copy(g_p_.SDCard + 'toFlash.tar.gz', g_p_.HomePath)
    elif exists(g_p_.USB + 'toFlash.tar.gz'):
        shutil.copy(g_p_.USB + 'toFlash.tar.gz', g_p_.HomePath)
    else:
        file_manager.downloadFile(url='{0}{1}'.format(url, file), path=g_p_.HomePath)

    g_p_.update_process += 1  # start check md5

    md5 = getINI('update', 'md5', '{0}{1}'.format(g_p_.HomePath, config.VERSION_FILE))
    logger.info('the package md5 is: {0}'.format(md5))
    print(md5)

    if file_manager.check_md5('{0}{1}'.format(g_p_.HomePath, 'toFlash.tar.gz'), md5):
        return recovery()

    else:
        logger.warning('update system failed: Download file error, md5 not matched')
        return False


def recovery():
    g_p_.update_process += 1  # start unzip files

    g_p_.mostfun.state = 'updating'
    subprocess.call('sh /etc/mountupdate.sh', shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    subprocess.call('rm -fr /update/*', shell=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    cmd = 'tar -xf {0}{1} -C {2}'.format(g_p_.HomePath, 'toFlash.tar.gz', r'/update/')
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    if len(p.stdout.readlines()) > 0:
        g_p_.mostfun.state = 'ready'
        logger.warning('update system failed: unzip system package failed')
        return False
    # do update
    g_p_.update_process += 1  # start restart
    logger.info('update system: start reboot')
    sleep(10)
    subprocess.call('reboot ota', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
