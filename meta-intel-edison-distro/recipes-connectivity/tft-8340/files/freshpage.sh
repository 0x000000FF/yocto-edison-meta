#!/bin/bash
PID=`cat /var/run/TFT_8340.pid`
cp ${1} /tmp/page.bmp
`kill -2 ${PID}`
