#!/bin/bash
cp /mostfun/mjpgstreamer/default.jpg /tmp/
/mostfun/mjpgstreamer/mjpg_streamer -i "/mostfun/mjpgstreamer/input_uvc.so" -o "/mostfun/mjpgstreamer/output_file.so"
