# !/usr/bin/env python
# coding: utf-8
###chenlvzhou 2015.5.27
###modified from configure_edison

import time
import os
import re
import subprocess
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
    os.popen("systemctl stop hostapd && sleep 2 && systemctl start wpa_supplicant")
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
    result = {}
    loop_time = 0

    # print data

    while (len(data)):
        # print str(len(data))+'\t'+str(loop_time)
        line = data.pop().split("\t")
        ssid = ''
        db = 0
        secure = ''
        # print line
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
                result[loop_time] = {'ssid': ssid, 'secure': network_map[ssid], 'db': db}
                print result[loop_time]
            loop_time += 1

    # print 'while fin'
    network_file = open(STATE_DIR + "/networks.txt", "w")
    network_file.write("{\n")
    for i in range(0, len(ssid_keys)):
        network_file.write('\t"' + ssid_keys[i] + '": "' + network_map[ssid_keys[i]])
        if i == len(ssid_keys) - 1:
            network_file.write('"\n')
        else:
            network_file.write('",\n')
    # print 'for end'
    network_file.write("}\n")
    network_file.close()
    # print 'network file write end'
    # return network_map
    # print result
    return result


# def configureNetwork(choice,ssid_keys,network_map):
def configureNetwork(network_map, ssid, password=''):
    if network_map[ssid] == "OPEN":
        return wpa_templates.OPEN % (ssid, "")
    elif network_map[ssid] == "WEP":
        # password = ''
        if len(password) != 5 and len(password) != 13:
            return "Password must be either 5 or 13 characters."
            # password = getNetworkPassword()
        return wpa_templates.WEP % (ssid, "", password)
    elif network_map[ssid] == "WPA-PSK":
        # password = ''
        if len(password) < 8 or len(password) > 63:
            return "Password must be between 8 and 63 characters."
            # password = getNetworkPassword()
        return wpa_templates.WPAPSK % (ssid, "", password)
        # elif network_map[ssid] == "WPA-EAP":
        # identity = getNetworkIdentity()
        # password = getNetworkPassword()
        # return wpa_templates.WPAEAP % (ssid, "", identity, password)
        # else:
        # print noooo("the last line of startNetworkConfig")


def setNetwork(network_conf):
    if not os.path.isfile('/etc/wpa_supplicant/wpa_supplicant.conf.original'):
        subprocess.call("cp /etc/wpa_supplicant/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf.original",
                        shell=True)

    subprocess.call("cp /etc/wpa_supplicant/wpa_supplicant.conf.original /etc/wpa_supplicant/wpa_supplicant.conf",
                    shell=True)
    wpa_supplicant = open('/etc/wpa_supplicant/wpa_supplicant.conf',
                          'a')  # Will not take care of duplicates at the moment.
    wpa_supplicant.write(network_conf)
    wpa_supplicant.close();
    # print "Initiating connection to " + ssid + ". Please wait..."
    # try:
    if int(subprocess.check_output("systemctl status wpa_supplicant | grep 'active (running)' | wc -l",
                                   shell=True)) == 0:
        subprocess.call("systemctl stop hostapd &> /dev/null", shell=True)
        subprocess.call("systemctl start wpa_supplicant &> /dev/null", shell=True)
        time.sleep(10)
    else:
        subprocess.call("wpa_cli reconfigure &> /dev/null && sleep 2", shell=True)

    network_count = int(subprocess.check_output('wpa_cli list_networks | wc -l', shell=True))
    subprocess.call("wpa_cli select_network " + str(network_count - 2 - 1) + " &> /dev/null", shell=True)
    time.sleep(5)

    ifarray = subprocess.check_output("wpa_cli ifname", shell=True).split()
    subprocess.call("udhcpc -i " + ifarray[len(ifarray) - 1] + " -n &> /dev/null", shell=True)
    # except Exception as e:
    # print e
    # print "Sorry. Could not get an IP address."
    # return False
    # else:
    # print "Attempting to enable network access, please check 'wpa_cli status' after a minute to confirm."
    # return True


def checkNetwork(timeout=60):
    timeout = 60
    while True:
        # waiting = "Connecting: %s seconds left         \r" % timeout
        # stdout.write(waiting)
        # stdout.flush()
        time.sleep(1)
        # address = os.popen(
        # "ifconfig | grep -A1 'wlan0' | grep 'inet'| awk -F' ' '{ print $2 }' | awk -F':' '{ print $2 }'").read().rstrip()
        # return address
        # if not address == "":
        #     #print "Done. Please connect your laptop or PC to the same network as this device and go to " + \
        #     #  text_colors.CYAN + "http://" + address + text_colors.END + " or " + text_colors.CYAN + \
        #     #  "http://" + subprocess.check_output('hostname').strip() + ".local" + text_colors.END + \
        #     #  " in your browser."
        #     return address
        #     break
        # if timeout == 0:
        #     #print "Not connected. Something went wrong."
        #     return '0.0.0.0'
        #     break
        # (status,output) = commands.getstatusoutput('iwconfig')
        output = os.popen('iwconfig').read().rstrip()
        return output
        timeout = timeout - 1
