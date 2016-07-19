#!/bin/bash
USBPORT=`echo -e ${1} | cut -d / -f 8 | cut -d . -f 2`
if [ ${USBPORT} -eq 4 ]; 
	then
	umount /media/sdcard
	rm -r /media/sdcard
fi

if [ ${USBPORT} -eq 3 ]; 
	then
	umount /media/usb
	rm -r /media/usb
fi