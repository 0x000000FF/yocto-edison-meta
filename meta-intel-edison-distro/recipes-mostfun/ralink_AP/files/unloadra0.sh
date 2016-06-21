#!/bin/sh
rmmod /lib/modules/rtutil7601Uap.ko
rmmod /lib/modules/mt7601Uap.ko
rmmod /lib/modules/rtnet7601Uap.ko
ifconfig ra0 down