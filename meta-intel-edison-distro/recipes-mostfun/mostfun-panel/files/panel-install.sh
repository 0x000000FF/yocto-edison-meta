#!/bin/bash
systemctl start blink-led
echo "starting decode apps"
cd /mostfun
/mostfun/decode.mostfun /mostfun/mostfun.des3
echo "decode apps done"
rm -f /mostfun/mostfun.des3
echo "restart panel service..."
systemctl restart mostfun_panel
systemctl stop blink-led
/etc/freshpage.sh /mostfun/TFT/logo.bmp
