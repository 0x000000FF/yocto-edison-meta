#!/bin/bash
rmmod g_multi
losetup -o 8192 /dev/loop0 /dev/disk/by-partlabel/update
mount /dev/loop0 /update