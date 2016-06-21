#!/bin/bash
tar -zcvf - ./panel|openssl des3 -salt -k 8d374d372c06ac5bb0174c3646d835f5 | dd of=mostfun.des3
