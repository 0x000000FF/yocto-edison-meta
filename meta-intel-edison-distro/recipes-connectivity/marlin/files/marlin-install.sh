#!/bin/bash
echo "starting flash avr"
systemctl start blink-led
# systemctl disable mostfun_panel
# systemctl stop mostfun_panel
/etc/freshpage.sh /mostfun/TFT/upgrading.bmp
/mostfun/avr_isp/stk.py /mostfun/Marlin.hex
/etc/freshpage.sh /mostfun/TFT/logo.bmp
systemctl stop blink-led
# systemctl enable mostfun_panel
# systemctl start mostfun_panel
echo "flash avr done"