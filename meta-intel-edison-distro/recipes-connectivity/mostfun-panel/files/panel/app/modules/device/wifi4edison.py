#!/usr/bin/env python
# coding: utf-8
###chenlvzhou 2015.5.27
###modified from configure_edison

import commands
import os
import re
import subprocess
import time
from sys import stdout

STATE_DIR = '/var/lib/edison_config_tools'

WPAPSK_REGEX = re.compile(r'\[WPA[2]?-PSK-.+\]')
WPAEAP_REGEX = re.compile(r'\[WPA[2]?-EAP-.+\]')
WEP_REGEX = re.compile(r'\[WEP.*\]')


class wpa_templates:
    START = '''
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=0
update_config=1
ap_scan=1
'''
    OPEN = '''
network={
  ssid="%s"
  %s
  key_mgmt=NONE
}'''
    WEP = '''
network={
  ssid="%s"
  %s
  key_mgmt=NONE
  group=WEP104 WEP40
  wep_key0="%s"
}
'''
    WPAPSK = '''
network={
  ssid="%s"
  %s
  key_mgmt=WPA-PSK
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  eap=TTLS PEAP TLS
  psk="%s"
}
'''
    WPAEAP = '''
network={
  ssid="%s"
  %s
  key_mgmt=WPA-EAP
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  eap=TTLS PEAP TLS
  identity="%s"
  password="%s"
  phase1="peaplabel=0"
}
'''
    # worst case, break this out.
    MAX = '''
network={
  ssid="%s"
  %s
  key_mgmt=WPA-EAP WPA-PSK IEEE8021X NONE
  pairwise=CCMP TKIP
  group=CCMP TKIP WEP104 WEP40
  psk="%s"
  eap=TTLS PEAP TLS
  identity="%s"
  password="%s"
  phase1="peaplabel=0"
}
'''


def scanForNetworks(timeout=10):
    stdout.write("Starting scan\r")
    stdout.flush()
    os.popen("systemctl start wpa_supplicant")
    r = range(timeout, 0, -1)
    for i in r:
        stdout.write("Scanning: %s seconds left \r" % i)
        stdout.flush()
        if i == 6:
            os.popen("wpa_cli scan")
        time.sleep(1)

    data = os.popen("wpa_cli scan_results").read().split("\n")

    print "\n"
    network_map = {}
    ssid_keys = []
    result = []
    loop_time = 0

    while (len(data)):
        line = data.pop().split("\t")
        ssid = ''
        db = 0
        secure = ''
        if (len(line) == 5):
            ssid = line.pop()

            if ssid not in ssid_keys and not ssid == "" and "\\x00" not in ssid:
                tokens = line.pop()
                if WPAPSK_REGEX.search(tokens):
                    network_map[ssid] = "WPA-PSK"
                elif WPAEAP_REGEX.search(tokens):
                    network_map[ssid] = "WPA-EAP"
                elif WEP_REGEX.search(tokens):
                    network_map[ssid] = "WEP"
                else:
                    network_map[ssid] = "OPEN"

                ssid_keys.append(ssid)
                db = line.pop()
                item = {'ssid': ssid.decode('string-escape'), 'secure': network_map[ssid], 'db': db}
                result.append(item)
            loop_time += 1

    network_file = open(STATE_DIR + "/networks.txt", "w")
    network_file.write("{\n")
    for i in range(0, len(ssid_keys)):
        network_file.write('\t"' + ssid_keys[i] + '": "' + network_map[ssid_keys[i]])
        if i == len(ssid_keys) - 1:
            network_file.write('"\n')
        else:
            network_file.write('",\n')
    network_file.write("}\n")
    network_file.close()
    return result


def configureNetwork(ssid, secure, password=''):
    if secure == "OPEN":
        return wpa_templates.OPEN % (ssid, "")
    elif secure == "WEP":
        if len(password) != 5 and len(password) != 13:
            return "Password must be either 5 or 13 characters."
        return wpa_templates.WEP % (ssid, "", password)
    elif secure == "WPA-PSK":
        if len(password) < 8 or len(password) > 63:
            return "Password must be between 8 and 63 characters."
        return wpa_templates.WPAPSK % (ssid, "", password)


def setNetwork(network_conf):
    if not os.path.isfile('/etc/wpa_supplicant/wpa_supplicant.conf.original'):
        subprocess.call("cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.original", shell=True)
    subprocess.call("cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.bak",
                    shell=True)

    subprocess.call("cp /etc/wpa_supplicant/wpa_supplicant.conf.original /etc/wpa_supplicant/wpa_supplicant.conf",
                    shell=True)
    wpa_supplicant = open('/etc/wpa_supplicant/wpa_supplicant.conf',
                          'a')  # Will not take care of duplicates at the moment.
    wpa_supplicant.write(network_conf)
    wpa_supplicant.close()
    linkNetwork()

    # if fail, rollback
    output = commands.getoutput('ifconfig wlan0 | grep addr:').split()
    if len(output) == 0:
        subprocess.call('cp /etc/wpa_supplicant/wpa_supplicant.conf.bak /etc/wpa_supplicant/wpa_supplicant.conf',
                        shell=True)
        linkNetwork()
        return False
    else:
        return True


def linkNetwork():
    if int(subprocess.check_output("systemctl status wpa_supplicant | grep 'active (running)' | wc -l",
                                   shell=True)) == 0:
        subprocess.call("systemctl start wpa_supplicant &> /dev/null", shell=True)
        time.sleep(1)
    else:
        subprocess.call("wpa_cli reconfigure &> /dev/null && sleep 2", shell=True)

    network_count = int(subprocess.check_output('wpa_cli list_networks | wc -l', shell=True))
    subprocess.call("wpa_cli select_network " + str(network_count - 2 - 1) + " &> /dev/null", shell=True)
    time.sleep(5)

    ifarray = subprocess.check_output("wpa_cli ifname", shell=True).split()
    subprocess.call("udhcpc -i " + ifarray[len(ifarray) - 1] + " -n &> /dev/null", shell=True)
    time.sleep(1)


def checkNetwork():
    res = None
    p = subprocess.Popen("ifconfig wlan0 | grep addr: | cut -d : -f 2 | cut -d ' ' -f 1", shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.wait()
    ip = p.stdout.readlines()[0][0:-1]
    if len(ip.strip()):
        p = subprocess.Popen('iwconfig wlan0 | grep ESSID: | cut -d \\" -f 2', shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        p.wait()
        ssid = p.stdout.readlines()[0]
        if ssid[-1] == '\n' or ssid[-1] == '\r':
            ssid = ssid[0:-1]
        res = {'ssid': ssid.strip(), 'ip': ip}
    else:
        res = {'ssid': 'None', 'ip': 'None'}

    return res
