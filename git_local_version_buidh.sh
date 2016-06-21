#!/bin/bash
VER_FILE=version.h
LOCALVER=`git rev-list HEAD | wc -l | awk '{print $1}'`
echo "LOCALVER:" $LOCALVER
VER=r$LOCALVER
VER="$VER-$(git rev-list HEAD -n 1 | cut -c 1-7)"
GIT_VERSION=$VER
echo "GIT_VERSION:" $VER
echo "Generated" $VER_FILE
echo "#ifndef PROJECT_VERSION_H" > $VER_FILE
echo "#define PROJECT_VERSION_H" >> $VER_FILE
echo "" >> $VER_FILE
echo "#define VERSION_NUMBER \"$GIT_VERSION\"" >> $VER_FILE
echo "" >> $VER_FILE
echo "#endif" >> $VER_FILE
sed -i "s#^LINUX_VERSION_EXTENSION.*#LINUX_VERSION_EXTENSION ?= \"-edison-\${LINUX_KERNEL_TYPE}-$GIT_VERSION\"#g" /media/yocto/edison-src/out/linux64/poky/meta/recipes-kernel/linux/linux-yocto.inc
echo "linux-yocto.inc have been changed!"
