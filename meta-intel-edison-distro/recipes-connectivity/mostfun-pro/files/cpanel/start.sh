#!/bin/sh
cd /usr/local/nginx/sbin
./nginx
cd /home/mjpgstreamer
export LD_LIBRARY_PATH="$(pwd)"
./mjpg_streamer -i "./input_uvc.so -d /dev/video0 -r 640x480 -f 15" -o "./output_http.so -p 8080 -w ./www"
cd /home/uwsgi-2.0.9
./uwsgi --ini mostfun.ini


python /home/runserver.py