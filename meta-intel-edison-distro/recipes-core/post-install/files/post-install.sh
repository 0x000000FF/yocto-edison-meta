#!/bin/bash
# This script performs post treatments after flash

# global variable set to 1 if output is systemd journal
fi_journal_out=0

export PATH="$PATH:/usr/sbin/"

# handle argument, if post-install is called from systemd service
# arg1 is "systemd-service"
if [ "$1" == "systemd-service" ]; then fi_journal_out=1; fi;

#echo function to output to journal system or in colored terminal
#arg $1 message
#arg $2 log level
fi_echo () {
    lg_lvl=${2:-"log"}
    msg_prefix=""
    msg_suffix=""
    case "$lg_lvl" in
        log) if [ $fi_journal_out -eq 1 ]; then msg_prefix="<5>"; else msg_prefix="\033[1m"; msg_suffix="\033[0m"; fi;;
        err) if [ $fi_journal_out -eq 1 ]; then msg_prefix="<1>"; else msg_prefix="\033[31;40m\033[1m"; msg_suffix="\033[0m"; fi;;
    esac
    printf "${msg_prefix}${1}${msg_suffix}\n"
}

# set_retry_count to failure file
# arg $1 new retry count
set_retry_count () {
    fw_setenv first_install_retry $1
}

# get_retry_count from failure from bootloader
get_retry_count () {
    retry_count=$(fw_printenv first_install_retry | tr -d "first_install_retry=")
    [ -z $retry_count ] && { set_retry_count 0; retry_count=0;}
    return $retry_count
}

# exit first_install by rebooting and handling the failure by setting
# the firmware target according to failure or success
# on failure increment fail count and reboot
# on success reboot in multi-user target
# arg $1 exit code
exit_first_install () {
    if [ $1 -eq 0 ]; then
        # reset failure count
        set_retry_count 0
        # update firmware target
        # next reboot will be on multi-user target
        fw_setenv bootargs_target multi-user
    fi
    # dump journal to log file
    journalctl -u post-install -o short-iso >> /post-install.log
    systemctl daemon-reload
}

# continue normal flow or exit on error code
# arg $1 : return code to check
# arg $2 : string resuming the action
fi_assert () {
    if [ $1 -ne 0 ]; then
        fi_echo "${2} : Failed ret($1)" err;
        exit_first_install $1;
    else
        fi_echo "${2} : Success";
    fi
}

factory_partition () {
    #unmount factory partition
    systemctl stop factory.mount

    mkdir -p /factory
    mount /dev/disk/by-partlabel/factory /factory
    # test can fail if done during manufacturing
    if [ $? -ne 0 ];
    then
        mkfs.ext4 /dev/disk/by-partlabel/factory
        mount /dev/disk/by-partlabel/factory /factory
        echo "00:11:22:33:55:66" > /factory/bluetooth_address
        echo "VSPPYWWDXXXXXNNN" > /factory/serial_number
    fi
}

mount_home () {
    # mount home partition on /home
    mount /dev/disk/by-partlabel/home /home
    fi_assert $? "Mount /home partition"
}

# generate sshd keys
sshd_init () {
    rm -rf /etc/ssh/*key*
    systemctl start sshdgenkeys
    sed -i 's/^BindToDevice=/# BindToDevice=/g' /lib/systemd/system/sshd.socket ; sync ; systemctl daemon-reload; systemctl restart sshd.socket
}


# Substitute the SSID and passphrase in the file /etc/hostapd/hostapd.conf
# The SSID is built from the hostname and a serial number to have a
# unique SSID in case of multiple Edison boards having their WLAN AP active.
setup_ap_ssid_and_passphrase () {
    # factory_serial is 16 bytes long
    if [ -f /sys/class/net/wlan0/address ];
    then
        ifconfig wlan0 up
        wlan0_addr=$(cat /sys/class/net/wlan0/address | tr '[:lower:]' '[:upper:]')
        ssid="mostfun-${wlan0_addr:12:2}${wlan0_addr:15:2}"

        # Substitute the SSID
        #sed -i -e 's/^ssid=.*/ssid='${ssid}'/g' /etc/hostapd/hostapd.conf
        sed -i -e 's/^SSID=.*/SSID='${ssid}'/g' /etc/Wireless/RT2870AP/RT2870AP.dat
    fi

    if [ -f /factory/serial_number ] ;
    then
        factory_serial=$(head -n1 /factory/serial_number | tr '[:lower:]' '[:upper:]')
        passphrase="${factory_serial}"

        # Substitute the passphrase
        sed -i -e 's/^wpa_passphrase=.*/wpa_passphrase='12345678'/g' /etc/hostapd/hostapd.conf
    fi

    sync
}

set_rootpassword()
{
#    useradd -p \$6\$4767c.BTj7x\$W5X0l/TsrAQz1AgeExQg5xigtWjq15TFc62LDtADupRCXCZUvxoMa1bU6of7.W.ENwIUfw7hxV1E/jxgJ7Rry0 root -g root
#    useradd -p \$6\$bvVxf//fG$u7o0sr20z2fFza.qyMoMZX7BahtNVaMKLR44JGqnPeS8n/1J1Kdnf/e9Y53bMBAd9l3rQqiqgxPQbrlSMEgol/ guest -M
    sed -i '1,1c root:\$6\$4767c.BTj7x\$W5X0l/TsrAQz1AgeExQg5xigtWjq15TFc62LDtADupRCXCZUvxoMa1bU6of7.W.ENwIUfw7hxV1E/jxgJ7Rry0:0:0:root:/home/root:/bin/sh' /etc/passwd
    sed -i '1,1c root:\$6\$4767c.BTj7x\$W5X0l/TsrAQz1AgeExQg5xigtWjq15TFc62LDtADupRCXCZUvxoMa1bU6of7.W.ENwIUfw7hxV1E/jxgJ7Rry0:16778:0:99999:7:::' /etc/shadow
}

create_dirs()
{
    #mkdir /mostfun
    mkdir /update
<<<<<<< HEAD
=======
    mkdir /media/sdcard
    mkdir /media/usb
>>>>>>> c80c8cc25ee4bd6944df95846766a99b39c3de9c

    mkdir /home/mostfuncp
    mkdir /home/backup
    mkdir /home/logs
    mkdir /home/mostfuncp/gcode
    mkdir /home/mostfuncp/img
    mkdir /home/mostfuncp/model
    mkdir /home/mostfuncp/tmp
    mkdir /home/mostfuncp/zip
    mkdir /home/mostfuncp/paused
    mkdir /home/mostfuncp/interrupted
}

restore()
{
    cp /home/backup/RT2870AP.dat /etc/Wireless/RT2870AP/
    cp /home/backup/wpa_supplicant.conf /etc/wpa_supplicant/
    systemctl enable wpa_supplicant
}
# script main part

# print to journal the current retry count
get_retry_count
retry_count=$?
set_retry_count $((${retry_count} + 1))
fi_echo "Starting Post Install (try: ${retry_count})"

systemctl start blink-led
/etc/freshpage.sh /mostfun/TFT/upgrading.bmp
#show upgrading
echo "upgrading"

ota_done=$(fw_printenv ota_done | tr -d "ota_done=")
if [ "$ota_done" != "1" ];
then
    # backup initial /home/root directory
    mkdir /tmp/oldhome
    cp -R /home/* /tmp/oldhome/
    fi_assert $? "Backup home/root contents of rootfs"

    # format partition home to ext4d
    mkfs.ext4 -m0 /dev/disk/by-partlabel/home
    fi_assert $? "Formatting home partition"

    # mount home partition
    mount_home

    # copy back contents to /home and cleanup
    cp -R /tmp/oldhome/* /home/
    rm -rf /tmp/oldhome
    fi_assert $? "Restore home/root contents on new /home partition"

    # create a fat32 primary partition on all available space
    echo -ne "n\np\n1\n\n\nt\nb\np\nw\n" | fdisk /dev/disk/by-partlabel/update

    # silent error code for now because fdisk failed to reread MBR correctly
    # MBR is correct but fdisk understand it as the main system MBR, which is
    # not the case.
    fi_assert 0 "Formatting update partition Step 1"

    # create a loop device on update disk
    losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
    fi_assert $? "Formatting update partition Step 2"

    # format update partition
    mkfs.vfat /dev/loop0 -n "Edison" -F 32
    fi_assert $? "Formatting update partition Step 3"

    # remove loop device on update disk
    losetup -d /dev/loop0
    fi_assert $? "Formatting update partition Step 4 final"
else
    # just mount home partition after OTA update
    mount_home
fi

# handle factory partition
factory_partition

# ssh
sshd_init
fi_assert $? "Generating sshd keys"

# update entry in /etc/fstab to enable auto mount
sed -i 's/#\/dev\/disk\/by-partlabel/\/dev\/disk\/by-partlabel/g' /etc/fstab
fi_assert $? "Update file system table /etc/fstab"


echo "set rootpasswd"
set_rootpassword

echo "create dirs"
create_dirs

echo "reatore"
restore

# Setup Access Point SSID and passphrase
setup_ap_ssid_and_passphrase
fi_assert $? "Generating Wifi Access Point SSID and passphrase"


rm -f /lib/udev/rules.d/80-net-setup-link.rules
sed -i -e 's/^MountFlags=.*/MountFlags='shared'/g' /lib/systemd/system/systemd-udevd.service

#update-rc.d start.sh defaults 97

<<<<<<< HEAD
=======
#update-rc.d start.sh defaults 97

>>>>>>> c80c8cc25ee4bd6944df95846766a99b39c3de9c
echo "set hostname"
echo "mostfun-${wlan0_addr:12:2}${wlan0_addr:15:2}" > /etc/hostname 

systemctl enable udhcpd-for-ra0
systemctl enable mjpg_streamer
<<<<<<< HEAD
=======

systemctl start panel-install
>>>>>>> c80c8cc25ee4bd6944df95846766a99b39c3de9c

systemctl stop blink-led
fi_echo "Post install success"

# end main part
exit_first_install 0

