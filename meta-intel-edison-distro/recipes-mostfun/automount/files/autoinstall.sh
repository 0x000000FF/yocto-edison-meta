#!/bin/bash

checkfile()
{
	cd ${1}
	if [ -s toFlash.tar.gz ]
		then
		echo "prepare to flash"
		rmmod g_multi
		losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
		mount /dev/loop0 /update
		rm -rf /update/*
		echo "unpressing"
		tar -xf toFlash.tar.gz -C /update
		reboot ota
	else
		echo "no file to flash"
	fi
}

checkfile /media/usb
checkfile /media/sdcard
