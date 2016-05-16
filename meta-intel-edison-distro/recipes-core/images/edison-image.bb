DESCRIPTION = "A fully functional image to run EDISON"
LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690 \
                    file://${COREBASE}/meta/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
LICENSE = "MIT"
IMAGE_INSTALL = "packagegroup-core-boot ${ROOTFS_PKGMANAGE_BOOTSTRAP} ${CORE_IMAGE_EXTRA_INSTALL}"
IMAGE_INSTALL += "openssh-sftp-server"

IMAGE_LINGUAS = " "

INITRD = ""
INITRD_IMAGE = ""

# Do not use legacy nor EFI BIOS
PCBIOS = "0"
# Do not support bootable USB stick
NOISO = "1"
ROOTFS = ""

# This is useless stuff, but necessary for building because
# inheriting bootimg also brings syslinux in..
AUTO_SYSLINUXCFG = "1"
SYSLINUX_ROOT = ""
SYSLINUX_TIMEOUT ?= "10"
SYSLINUX_LABELS ?= "boot install"
LABELS_append = " ${SYSLINUX_LABELS} "


# Specify rootfs image type
IMAGE_FSTYPES = "ext4"

inherit core-image

# This has to be set after including core-image otherwise it's overriden with "1"
# and this cancel creation of the boot hddimg
NOHDD = "0"

inherit bootimg
do_bootimg[depends] += "${PN}:do_rootfs"

IMAGE_ROOTFS_SIZE = "524288"

IMAGE_FEATURES += "package-management ssh-server-openssh"
# Allow passwordless root login and postinst logging
IMAGE_FEATURES += "debug-tweaks"

#mostfun app

IMAGE_INSTALL += "mostfun-pro-panel"
#IMAGE_INSTALL += "mostfun-panel"
IMAGE_INSTALL += "decode"
#IMAGE_INSTALL += "updateconfig"
IMAGE_INSTALL += "updateconfigdev"
IMAGE_INSTALL += "buzzer"
IMAGE_INSTALL += "tft-8340"
IMAGE_INSTALL += "mountupdate"
IMAGE_INSTALL += "avr-isp"
IMAGE_INSTALL += "marlin"
IMAGE_INSTALL += "mjpgstreamer"
IMAGE_INSTALL += "mail-tool"
#IMAGE_INSTALL += "slice"
IMAGE_INSTALL += "usbhub"
#IMAGE_INSTALL += "models"

#IMAGE_INSTALL += "connman"
#IMAGE_INSTALL += "connman-client"
#IMAGE_INSTALL += "connman-tools"
#IMAGE_INSTALL += "connman-init-systemd"
#IMAGE_INSTALL += "ap-mode-toggle"
IMAGE_INSTALL += "wireless-tools"
IMAGE_INSTALL += "wpa-supplicant"
#IMAGE_INSTALL += "hostapd-daemon"
#IMAGE_INSTALL += "bluez5-dev"
#IMAGE_INSTALL += "bluez5-obex"
IMAGE_INSTALL += "kernel-modules"
IMAGE_INSTALL += "ethtool"
IMAGE_INSTALL += "iptables"
IMAGE_INSTALL += "libstdc++"
IMAGE_INSTALL += "u-boot"
IMAGE_INSTALL += "u-boot-fw-utils"
IMAGE_INSTALL += "file"
IMAGE_INSTALL += "pciutils"
IMAGE_INSTALL += "usbutils"
IMAGE_INSTALL += "ldd"
IMAGE_INSTALL += "i2c-tools"
IMAGE_INSTALL += "watchdog-sample"
IMAGE_INSTALL += "pwr-button-handler"
IMAGE_INSTALL += "blink-led"
IMAGE_INSTALL += "post-install"
IMAGE_INSTALL += "resize-rootfs"
IMAGE_INSTALL += "systemd-analyze"
IMAGE_INSTALL += "wget"

# Allows to enable OpenMP feature
#IMAGE_INSTALL += "libgomp"

# Add audio firmware
#IMAGE_INSTALL += "sst-fw-bin"

# ALSA lib and utilities
#IMAGE_INSTALL += "alsa-lib"
#IMAGE_INSTALL += "alsa-utils-alsamixer alsa-utils-alsactl alsa-utils-aplay alsa-utils-amixer"


# Python and some basic modules

IMAGE_INSTALL += "python"

IMAGE_INSTALL += "python-dbus python-smartpm python-pygobject python-argparse"
IMAGE_INSTALL += "python-distutils python-pkgutil python-audio python-image python-imaging python-email python-netserver python-xmlrpc python-ctypes python-html python-compile python-misc python-numbers python-unittest python-pydoc python-qrcode"


#IMAGE_INSTALL += "python-pip python-blinker python-configobj python-dominate python-flask python-flask-bootstrap python-flask-login python-flask-mail python-flask-wtf python-itsdangerous python-jinja2 python-markupsafe python-six python-werkzeug python-wtforms"

IMAGE_INSTALL += "python-pip python-blinker python-configobj python-dominate python-flask python-flask-bootstrap python-flask-login python-flask-mail python-flask-wtf python-itsdangerous python-jinja2 python-markupsafe python-pyserial python-six python-werkzeug python-wtforms"

#eth manegnment tool
#IMAGE_INSTALL += "batctl"
# Wifi firmware
IMAGE_INSTALL += "bcm43340-fw"
#IMAGE_INSTALL += "rtl8188cus-fw"
IMAGE_INSTALL += "mt7601u"
IMAGE_INSTALL += "ralink-ap"
# Bluetooth Firmware patch for 43340 and its patch utility
#IMAGE_INSTALL += "bcm43340-bt"
# service daemon that listens to rfkill events and trigger FW patch download
#IMAGE_INSTALL += "bluetooth-rfkill-event"
# Wifi driver built as a kernel module
IMAGE_INSTALL += "bcm43340-mod"

# Provides strace and gdb
#IMAGE_FEATURES += "tools-debug"
#IMAGE_INSTALL += "crashlog"

# Clean corrupted journald entries
IMAGE_INSTALL += "cleanjournal"

# Adds various other tools
IMAGE_INSTALL += "tcpdump"
IMAGE_INSTALL += "net-tools"
IMAGE_INSTALL += "lsof"
IMAGE_INSTALL += "iperf"

# Add pulseaudio
#IMAGE_INSTALL += "pulseaudio-server libpulsecore libpulsecommon libpulse libpulse-simple pulseaudio-misc pulseaudio-service"

#Add Gstreamer
#IMAGE_INSTALL += "gstreamer1.0 gstreamer1.0-meta-base gstreamer1.0-meta-audio"

# Those are necessary to manually create partitions and file systems on the eMMC
IMAGE_INSTALL += "parted"
IMAGE_INSTALL += "e2fsprogs-e2fsck e2fsprogs-mke2fs e2fsprogs-tune2fs e2fsprogs-badblocks libcomerr libss libe2p libext2fs dosfstools"

# Time related
IMAGE_INSTALL += "tzdata"

# SWIG
#IMAGE_INSTALL += "swig"


# Edison Arduino stuff
#IMAGE_INSTALL += "clloader"


# Edison Middleware stuff
IMAGE_INSTALL += "packagegroup-core-buildessential"
#IMAGE_INSTALL += "iotkit-opkg" #intel iotkit online opkg repo src
#IMAGE_INSTALL += "zeromq-dev"
#IMAGE_INSTALL += "cppzmq-dev"
#IMAGE_INSTALL += "paho-mqtt-dev"
IMAGE_INSTALL += "mdns-dev"
#IMAGE_INSTALL += "iotkit-comm-js"
#IMAGE_INSTALL += "iotkit-comm-c-dev"
#IMAGE_INSTALL += "iotkit-agent"
#IMAGE_INSTALL += "iotkit-lib-c-dev"
#IMAGE_INSTALL += "xdk-daemon"
IMAGE_INSTALL += "oobe"

# mosquitto and dependencies
#IMAGE_INSTALL += "mosquitto-dev"
#IMAGE_INSTALL += "mosquitto-clients"

# node and sub-components
#IMAGE_INSTALL += "nodejs-dev"
#IMAGE_INSTALL += "nodejs-npm"

# MRAA
IMAGE_INSTALL += "mraa-dev"
IMAGE_INSTALL += "mraa-doc"

# UPM
#IMAGE_INSTALL += "upm-dev"

# INTEL MCU FW
IMAGE_INSTALL += "mcu-fw-load"
IMAGE_INSTALL += "mcu-fw-bin"

# nfs
IMAGE_INSTALL += "nfs-utils"

# Add oFono
#IMAGE_INSTALL += "ofono"

# Add battery level detection
#IMAGE_INSTALL += "battery-voltage"

