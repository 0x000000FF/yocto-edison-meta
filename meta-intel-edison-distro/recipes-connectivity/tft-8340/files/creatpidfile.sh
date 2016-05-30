#!/bin/bash
ps | grep ${1} | grep -v grep | awk '{print$1}' > /var/run/${1}.pid