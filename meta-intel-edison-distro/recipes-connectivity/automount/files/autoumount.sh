#!/bin/bash
USBPORT=`echo -e ${1} | cut -d / -f 8 | cut -d . -f 2`
DEVICE=`echo -e ${1} | awk -F '/' '{print $NF}'`
if [ ${USBPORT} -eq 4 ]; 
	then
	echo "USB port 4"
	umount /media/sdcard
	rm -rf /media/sdcard
fi

if [ ${USBPORT} -eq 3 ]; 
	then
	echo "USB port 3"
	umount /media/usb
	rm -rf /media/usb
fi