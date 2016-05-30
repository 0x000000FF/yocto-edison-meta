#!/bin/bash
USBPORT=`echo -e ${1} | cut -d / -f 8 | cut -d . -f 2`
DEVICE=`echo -e ${1} | awk -F '/' '{print $NF}'`
if [ ${USBPORT} -eq 4 ]; 
	then
	mkdir /media/sdcard
	mount /dev/${DEVICE} /media/sdcard
fi

if [ ${USBPORT} -eq 3 ]; 
	then
	mkdir /media/usbstorage
	mount /dev/${DEVICE} /media/usbstorage
fi