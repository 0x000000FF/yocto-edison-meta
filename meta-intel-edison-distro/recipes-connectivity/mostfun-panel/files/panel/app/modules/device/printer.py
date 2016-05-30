#!/usr/bin/env python
# coding: utf-8
import copy
import os
import platform
import re
import threading
import subprocess
from collections import deque
from time import sleep, time
from ... import g_p_, logger

import serial
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
import gobject

MSG_OBJ_PATH = "/com/example/msg"
MSG_INTERFACE_URI = "com.example.msg"

TIMEFORMAT = "%H:%M:%S"

__author__ = 'const'

# Debug Mode
# 1>no info
# 2>show info
# 3>more info
DEBUG_MSG_LEVE = 7

def debug_mesg(mesg, level):
    global DEBUG_MSG_LEVE
    if level <= DEBUG_MSG_LEVE:
        print mesg

MAX_GCODE_HISTORY_BUFFER = 8

PATH_PAUSED_FILES = r'/home/mostfuncp/paused/'
PATH_INTERRUPTED_FILE = r'/home/mostfuncp/interrupted/'

sysstr = platform.system()
if (sysstr == "Windows"):
    SERIALPORT = 'COM3'
elif (sysstr == "Linux"):
    # SERIALPORT = '/dev/ttyMFD1'
    # SERIALPORT = '/dev/ttyUSB0'
    SERIALPORT = '/dev/ttyUSB0' if os.path.exists(r'/dev/ttyUSB0') else r'/dev/ttyMFD1'

SERIALBAUD = 115200
p2p_mesg_box = deque()
web_mesg_box = deque()
UI_mesg_box = deque()

default_start_gcode = (
    "G90\n",
    "M82\n",
    "M107\n",
    "G28\n",
    "G34\n",
    "G92 E0\n",
    "G1 F9000\n")

def bibi(sustain, times):
    p = subprocess.Popen(["/mostfun/buzzer", str(sustain), str(times)], \
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, \
                         stderr=subprocess.PIPE, shell=False)

class mesg_center(dbus.service.Object):
    def __init__(self,bus,object_path):
        dbus.service.Object.__init__(self,bus,object_path)
        mesg_table = {}
        mesg_que = deque()

    @dbus.service.method(dbus_interface=MSG_INTERFACE_URI,in_signature='', out_signature='s')
    def say_hello(self):
        return "hello, exported method"

    @dbus.service.signal(dbus_interface=MSG_INTERFACE_URI,signature='as')
    def msg_signal(self,msg_list):
        print "exported signal: ",msg_list

    def construct_msg(self):
        timeStamp = time.strftime(TIMEFORMAT)
        self.msg_signal(["1111",timeStamp,"This is the content","1 2 3"])
        return True

    def set_table(self,table):
        mesg_table = table

    def mesg_monitor(self):
        pass

class gcode(object):
    def __init__(self):
        self.position = 0
        self.layerCount = 0
        self.layerNum = 0
        self.layer_offset = 0
        self.extruderTargetTemp = 0.0
        self.bedTargetTemp = 0.0
        self.q = list()
        self.lines = 0
        self.headinfo = list(default_start_gcode)
        self.invalid_gcode = True

    def clear(self):
        self.position = 0
        self.layerCount = 0
        self.layerNum = 0
        self.extruderTargetTemp = 0.0
        self.bedTargetTemp = 0.0
        self.lines = 0
        self.headinfo = list(default_start_gcode)

    def load(self, path):
        self._f = open(path, 'r')
        self.q = self._f.readlines()
        self.lines = len(self.q)
        if (self.lines <= 1):
            return False
        self._f.close()
        line = 0
        # print "*************"
        for command in self.q:
            if line > 300:
                return True
            if command.startswith(';'):
                if ';Layer count:' in command: #head 
                    self.layerCount = int(re.search(';Layer count: *([0-9]*)', command).group(1))
                    # print "========================"
                    # for i in range(0,30):
                    #     print self.q[i]
                    # print "========================"
                    return True
            else:
                command = command[0:command.find(';')]
                if 'G28' in command:
                    # print "28282828"
                    # print self.q[line]
                    # print self.q[line+1]
                    self.q[line] = 'G28\n'
                    if not 'G34' in self.q[line + 1]:
                        self.q.insert(line+1,'G34\n')
                        # print self.q[line+1]
                elif 'M104' in command or 'M109' in command:
                    # print "+++"
                    # print command
                    # print self.headinfo
                    self.extruderTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                    debug_mesg('extruderTargetTemp:' + str(self.extruderTargetTemp), 3)
                    self.headinfo.insert(0,command+'\n')
                    # print self.headinfo
                elif 'M140' in command or 'M190' in command:
                    self.bedTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                    debug_mesg('bedTargetTemp:' + str(self.bedTargetTemp), 3)
                    self.headinfo.insert(0,command+'\n')
            line += 1


class mostfun(object):
    def __init__(self, port=SERIALPORT, baud=SERIALBAUD):
        # ready\printing\pause\error\updating
        self.state = 'ready'
        self.busy = False
        self._filePath = ''

        self._extruderTemp = 0
        self._bedTemp = 0
        self._currentX = 0
        self._currentY = 0
        self._currentZ = 0
        self._currentF = 0
        self._currentE = 0
        self._hot_header = False
        self._ispaused_task = False
        self._percnet = 0.0

        self._g = gcode()
        self._secs = 0

        self._buffer_size = 32
        self._history_buffer_size = 32
        self._send_buffer = [deque(maxlen=32),
                             deque(maxlen=32)]  # |[0]query-line|[1]handctl-line|[_gcode_list]gcodefile-line|
        self._gcode_list = self._g.q
        self._gcode_pointor = 0
        self._gcode_lock = False 
        self._gcode_EOF = False
        self._history_buffer = deque(maxlen=self._history_buffer_size)
        self._history_flag = 0
        self._resend_flag = False
        # self._serial = serial.Serial(port, baud, timeout=3, writeTimeout=10000,parity=serial.PARITY_EVEN)
        # self._serial = serial.Serial(port, baud, timeout=3, write_timeout=10000)
        # if self._serial == None:
        #     self.state = 'error'
        self._serial = None
        self.open_serial()

        self._is_busy = False
        self._machine_timeout = 0

        self._temp_timeout = 0
        self._conect_timeout = 0
        self._line_counter = 1
        # self._command = [0, 1, ""]  # command format   =>   |line_number|priority|gcode|
        self._autolevel_done = -1  #-1:did not leveling yet;0:doing leveling;1:leveling done

        self._current_prio = 2

        thread_monitor = threading.Thread(target=self._monitor)
        thread_monitor.daemon = True
        thread_monitor.start()

        thread_watcher = threading.Thread(target=self.mesg_box_watcher)
        thread_watcher.daemon = True
        thread_watcher.start()

        thread_tick = threading.Thread(target=self.clock)
        thread_tick.daemon = True
        thread_tick.start()

    def open_serial(self, port=SERIALPORT, baud=SERIALBAUD):
        self._serial = serial.Serial(port, baud, timeout=3, write_timeout=10000)
        if self._serial == None:
            logger.error("serial init ERROR")
            self.state = 'error'
        logger.warning("serial OK")

    def close_serial(self):
        self._serial.close()
        logger.warning("serial closed")

    def _addChecksum(self,command):
        checksum = reduce(lambda x, y: x ^ y, map(ord, "N%d%s" % (command[0], command[2])))
        CommandWithChecksum = "N%d %s *%d\n" % (command[0], command[2], checksum)
        return CommandWithChecksum

    def _set_gcode_cursor(self, direction,line = 1):  ##direction : +1 get next ;-1  get last

        for i in range(0,line) :
            while True:
                self._gcode_pointor += direction
                if self._gcode_pointor >= len(self._gcode_list) or self._gcode_pointor < 0:
                    return False
                command = self._gcode_list[self._gcode_pointor]
                if command.startswith(';') or command.startswith('\n') or command==' ' or len(command)<2:
                    if 'LAYER:' in command:
                        self._g.layerNum = int(re.search("LAYER:*([0-9-]*)", command).group(1))
                        if self._g.layerNum < 0:
                            self._g.layerNum = 0
                        else:
                            self._g.layerNum += 1
                    # self._gcode_pointor += direction
                    # if self._gcode_pointor >= len(self._gcode_list) or self._gcode_pointor < 0:
                    #     return False
                else:
                    if 'M104' in command or 'M109' in command:
                        self._g.extruderTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                    elif 'M140' in command or 'M190' in command:
                        self._g.bedTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                    # elif 'Z' in command 'G28' not in command:
                    #     self._currentZ = float(re.search("Z*([0-9\.]*)", command).group(1))
                    break
        return True

    def _get_gcode(self):
        if self._gcode_pointor >= len(self._gcode_list):  # print finished
            if self._ispaused_task == True:
                os.remove(self._filePath)
            sleep(3)
            self.reset()
            # print "finished"
            # print self._gcode_pointor
            return None
            logger.info("task finished")
        if len(self._gcode_list) > 0:
            command = self._gcode_list[self._gcode_pointor]
        else:
            logger.warning("empty gcode list")
            return
        if ';' in command:
            command = command[0:command.find(';')]
        if '\n' in command:
            command = command.rstrip('\n')
        command = command.rstrip()
        if self._g.lines > 0:
            self._percnet = self._gcode_pointor*100.0 / self._g.lines
        else:
            self._percnet = 0.0;

        self._set_gcode_cursor(1)

        return command

    def _send_line(self):
        if self._serial.isOpen == False:
            return False

        if len(self._send_buffer[0]) > 0:
            self._current_prio = 0
        elif len(self._send_buffer[1]) > 0:
            self._current_prio = 1
        elif len(self._gcode_list) > 0:
            self._current_prio = 2
        else:
            return False

        command = [0, 1, ""]
        # if self._resend_flag == True:
        # print self._history_buffer
        # print self._history_flag
        # print self._gcode_pointor

        def _generate_command():
            command = [0, 1, ""]
            command[0] = self._line_counter
            command[1] = self._current_prio
            if self._current_prio == 1:
                command[2] = self._send_buffer[1].popleft()
            elif self._current_prio == 2:
                if self._gcode_lock == True:
                    return False
                command[2] = self._get_gcode()
                if command[2] == None:
                    return False
            self._history_buffer.appendleft(copy.deepcopy(command))
            #self._history_buffer.extendleft([copy.deepcopy(command)])
            self._line_counter += 1
            return True

        if self._current_prio == 0:
            self._serial.write(self._send_buffer[0].popleft()) 
            self._is_busy = True
            #debug_mesg("serial send M105",2)

        else:
            if self._history_flag >= self._history_buffer_size or self._history_flag < 0:
                print "illegal flag"
                return False

            # if len(self._history_buffer) == 0:
            #     _generate_command()

            if self._history_flag == 0: #new Gcode
                if self._current_prio == 2 and self._gcode_lock == True: #frome Gcode file but paused
                    print "gcode paused"
                    return False
                if self._resend_flag == False:
                    if _generate_command() == False:
                        return
                elif self._resend_flag == True:
                    self._resend_flag = False

                ready2send = self._addChecksum(self._history_buffer[self._history_flag])
                self._serial.write(ready2send + '\n')
                self._is_busy = True
                # debug_mesg("serial send " + ready2send, 2)
                # _generate_command()
            else:
                ready2send = self._addChecksum(self._history_buffer[self._history_flag])
                self._serial.write(ready2send + '\n')
                self._is_busy = True
                debug_mesg("serial send " + ready2send, 2)
                self._history_flag -= 1

        return True

            # elif self._current_prio == 1:
            #     command[2] = self._send_buffer[self._current_prio].popleft()
            #     command[1] = self._current_prio
            #     command[0] = self._line_counter
            #     self._history_buffer.appendleft(copy.deepcopy(command))
            #     # self._history_buffer.append(self._command)
            #     ready2send = self._addChecksum(self._history_buffer[self._history_flag])
            #     self._serial.write(ready2send + '\n')
            #     debug_mesg("serial send " + ready2send, 2)
            #     self._line_counter += 1
            # elif self._current_prio == 2:
            #     if self._gcode_lock == True:
            #         return False
            #     command[2] = self._get_gcode()
            #     self._set_gcode_cursor(1)
            #     ommand[1] = self._current_prio
            #     command[0] = self._line_counter
            #     self._history_buffer.appendleft(copy.deepcopy(command))
            #     # self._history_buffer.append(self._command)
            #     ready2send = self._addChecksum(self._history_buffer[self._history_flag])
            #     self._serial.write(ready2send + '\n')
            #     debug_mesg("serial send " + ready2send, 2)
            #     self._line_counter += 1

    def _monitor(self):
        while True:
            if time() > self._temp_timeout:
                #if self._is_busy == False:
                self._get_temperature()

            Response = self._serial.readline()
            if len(Response) > 0:
                print "***RES***"
                print Response
            # print time()
            #debug_mesg(Response, 2)
            # if Response == '' and time() > self._conect_timeout:
            #     Response = 'ok'
            # if Response.startswith('ERROR>'):
            #     logger.error(Response) 
            #     # if re.match('Error:[0-9]\n', Response):
            #     #     Response = Response.rstrip() + self._serial.readline()
            #     self.state = 'error'
            if Response == 'ok\n':
                self._is_busy = False
                self._send_line()

            elif 'Resend' in Response:
                self._is_busy = False
                debug_mesg('A command send faild!Response:' + Response, 1)
                line = int(Response.replace("N:", " ").replace("N", " ").replace(":", " ").split()[-1])
                self._roll_back(line)

            else:
                global p2p_mesg_box
                if len(Response) > 0:
                    p2p_mesg_box.append(Response)
            self._conect_time = time() + 5

    def gcode_unlock(self):
        self._gcode_lock = False

    def gcode_lock(self):
        self._gcode_lock = True

    def _roll_back(self, line):
        self._resend_flag = True
        if line >= self._line_counter:
            self._history_buffer[0][0] = line
            self._line_counter = line+1
            return

        elif line < self._line_counter:
            # print len(self._history_buffer)
            for i in range(1,len(self._history_buffer)):
                if line == self._history_buffer[i][0]:
                    self._history_flag = i
                    break

        # if line < self._line_counter - 17:
        #     self._line_counter = line
        #     return
        # if line < self._line_counter:
        #     # self._command = self._history_buffer.pop()
        #     # if self.self._command[1] == 2:
        #     #     self._set_gcode_cursor(-1)
        #     # elif self._command[1] == 0 or self.self._command[1] == 1:
        #     #     self._send_buffer[self._command[1]].appendleft(self._command[2])

        #     while not self._command[0] == self._line_counter:
        #         self._command = self._history_buffer.pop()
        #         print self._command
        #         if len(self._history_buffer) > 0:
        #             if self._command[1] == 0 or self._command[1] == 1:
        #                 self._send_buffer[self._command[1]].appendleft(self._command[2])
        #             elif self._command[1] == 2:
        #                 self._set_gcode_cursor(-1)
        #         else:
        #             debug_mesg("Empty history deque", 1)
        #             break
        # elif line >= self._line_counter:
        #     if self._current_prio == 2:
        #         self._set_gcode_cursor(-1)
        #     self._command = self._history_buffer.pop()

        # self._line_counter = line

    def _get_temperature(self):
        self._send_buffer[0].append("M105\n")
        self._send_line()
        self._temp_timeout = time() + 2

    def set_temperature_timeout(self, timeout):
        self._temp_timeout = timeout

    sysstr = platform.system()
    if (sysstr == "Linux"):
        # ResetPin = mraa.Gpio(36)
        # ResetPin.dir(mraa.DIR_OUT)

        def rst(self):
            # print "####reset####"
            # self.ResetPin.write(0)
            # sleep(0.001)
            # self.ResetPin.write(1)
            #rstPin = open("/sys/class/gpio/gpio14/direction","w")
            with open("/sys/class/gpio/gpio14/direction","w") as rstPin:
                rstPin.write("low")

            sleep(0.1)
            # with open("/sys/class/gpio/gpio14/value","r") as rstPin:
            #     state = rstPin.read()
            # print "++++++++++++++"
            # print state

            with open("/sys/class/gpio/gpio14/direction","w") as rstPin:
                rstPin.write("high")

            sleep(1)
            self.send_command(["G28"])
            #rstPin.close()

        def Init(self):
            subprocess.call("""
                echo 14 > /sys/class/gpio/export
                echo high > /sys/class/gpio/gpio14/direction
                """, shell=True)
            #self.ResetPin.write(1)
    else:
        def rst(self):
            pass

        def Init(self):
            pass

    def get_extruderTemp(self):
        return self._extruderTemp

    def get_bedTemp(self):
        return self._bedTemp

    def get_extruderTargetTemp(self):
        return self._g.extruderTargetTemp

    def get_bedTargetTemp(self):
        return self._g.bedTargetTemp

    def get_state(self):
        return self.state

    def get_percent(self):
        return self._percnet

    def is_hot(self):
        return self._hot_header

    def is_printer_busy(self):
        return self._is_busy

    def get_currentfile(self):
        return self._filePath

    def clear(self):
        self._g.clear()
        self._percnet = 0.0
        self._gcode_list = []
        self._line_counter = 1
        self._gcode_pointor = 0
        self._temp_timeout = time() + 2
        self._send_buffer[0].clear()
        self._send_buffer[1].clear()
        self._history_buffer.clear()
        self._gcode_lock = False
        self._hot_header = False
        self._autolevel_done = -1
        self._current_prio = 2
        self.state = 'ready'

    def reset(self):
        self.state = 'ready'
        self.clear()
        self._secs = 0
        self.rst()
        sleep(1)
        # for i in range(0,100):
        if self._serial.isOpen() == False:
            self._serial.open()

    def send_command(self, commands):
        if len(commands) < self._buffer_size:
            # print "send_command "
            for i in range(len(commands)):
                commands[i] = commands[i].encode('ascii')
                if 'M104' in commands[i] or 'M109' in commands[i]:
                    self._g.extruderTargetTemp = float(re.search('S([0-9]+)', commands[i]).group(1))
                elif 'M140' in commands[i] or 'M190' in commands[i]:
                    self._g.bedTargetTemp = float(re.search('S([0-9]+)', commands[i]).group(1))
            self._send_buffer[1].extend(commands)
            # print "++extend done"
            self._send_line()
            # print "++send done"
            # print self._g.extruderTargetTemp
            return True
        else:
            return False

    def auto_leveling(self):
        if self.state == 'ready':
            UI_mesg_box.append("leveling:1")
            self.busy = True
            self._autolevel_done = 0
            command_alignment = ['G28', 'G29', 'G1 X2 Y181.5 Z15 F4800', 'G33','G1 Z10', 'G1 F4800 X110 Y90 Z1']
            self.send_command(command_alignment)
            logger.info("auto leveling start")
            return True
        else:
            return False

    def beginTask(self, path):
        # sendGcodeFile
        print "begin :"+ path
        logger.info("begin task")
        if path.split(os.sep)[-2] == 'paused' or path.split(os.sep)[-2] == 'interrupted':
            self._ispaused_task = True
        else:
            self._ispaused_task = False

        if self.state == 'ready':
            self.reset()
            #sleep(3)
            self._filePath = path
            if self._g.load(self._filePath) == False:
                print "invalid gcode"
                self.clear()
                return False 
            self._gcode_list = self._g.q
            self.send_command(['M110'])
            self.state = 'printing'
            bibi(600, 1)
            return True
        return False
        #####test####
        # while (True):
        #     self.reset()
        #     sleep(2)
        #     self.send_command(['M110'])
        #     sleep(1)

    def cancelTask(self):
        logger.warning("cancel task")
        self.gcode_lock()
        if self.state == 'printing' or self.state == 'pause':
            self.reset()
            sleep(3)
            self.send_command(["M104 S0", "G28"])
            bibi(400, 2)
            # sleep(3)

    def stop_saveTask(self, powerdown=False):
        logger.info("save task")
        temper = str(self._g.extruderTargetTemp)
        self.gcode_lock()
        # if self.state == 'printing' and self._hot_header == True:
        # if powerdown:
        #     # self.send_command(["M42 P8 S0"])
        #     print "save finished"
        # else:
        #     self.send_command(['M100'])

        if powerdown:
            f = open(PATH_INTERRUPTED_FILE + self._filePath.split(os.sep)[-1], 'w')
        else:
            f = open(PATH_PAUSED_FILES + self._filePath.split(os.sep)[-1], 'w')
        self.send_command(['M100'])
        sleep(3)
        # headinfo = ["M109 S" + temper, "\nG21", "\nG90","\nM82", "\nM107", "\nG28", "\nG34"
        #             "\nG1 F200 E15","\nG92 E0", "\nG1 F6000"]
        # extraed more
        headinfo = self._g.headinfo
        layer = [";Layer count: " + str(self._g.layerCount), "\n;LAYER:" + str(self._g.layerNum)]
        current = ["\nG91","\nG1 F200 E25","\nG90",
                    "\nG1 F6000 Z"+str(self._currentZ+0.4),
                    "\nG91","\nG1 X-10 F3600","\nG1 X10","\nG1 X-10","\nG1 X10","\nG1 X-10","\nG90", 
                    "\nG0 F6000"+" X"+str(self._currentX)+" Y"+str(self._currentY)+" Z"+str(self._currentZ+0.4),
                    "\nG91","\nG1 F200 E2.5","\nG90",
                    "\nG1 F"+str(int(self._currentF))+" Z"+str(self._currentZ),
                    "\nG92 E" + str(self._currentE),"\n"]
        
        # current = [
        #     "\nG1 F6000 Z"+str(self._currentZ+0.4),
        #     "\nG0 F6000"+" X"+str(self._currentX)+" Y"+str(self._currentY),
        #     "\nG1 F"+str(int(self._currentF))+" Z"+str(self._currentZ),
        #     "\nG92 E" + str(self._currentE),"\n"]
        f.writelines(headinfo)
        f.writelines(layer)
        f.writelines(current)
        self._set_gcode_cursor(direction=-1,line=16) #16 lines
        f.writelines(self._g.q[self._gcode_pointor:-1])
        f.close()
        os.system("sync")

        print "save done"

        # sleep(5)
        # if  powerdown:
        #     sys.exit()
        #     os.system('halt')
        # else:
        if not powerdown:
            sleep(5)
            self.reset()

    def pauseTask(self):
        if self.state == 'printing':
            logger.info("pause task")
            self.gcode_lock()
            command_pause = ['M100']  # get the cuttent position first "M114"
            self._set_gcode_cursor(direction=-1,line=16)
            self.send_command(command_pause)
            self.state = 'pause'

    def resumeTask(self):
        if self.state == 'pause':
            logger.info("resume task")
            self.gcode_unlock()

            command_resume = ['G90','M82','M107','G28','G34', \
                              'G1 F6000 Z'+str(self._currentZ+0.4), 'G92 E0','G1 F200 E5', \
                              'G91','G1 X-10 Y-10 E-1 F3600','G1 X10 Y10','G1 X-10 Y-10','G1 X10 Y10','G1 X-10 Y-10','G90', \
                              'G1 F6000 X'+str(self._currentX)+' Y'+str(self._currentY), \
                              'G1 F6000 Z'+str(self._currentZ),'G1 F200 E5.3', \
                              'G92 E'+str(self._currentE),'G1 F' + str(self._currentF)]

            self.send_command(command_resume)
            print command_resume
            self.state = 'printing'

    def clock(self):
        while True:
            if self.state == 'printing':
                self._secs += 1
            sleep(1)

    def get_times(self):
        hh = '%02d' % (self._secs // 3600)
        mm = '%02d' % ((self._secs % 3600) // 60)
        ss = '%02d' % (self._secs % 60)
        return hh + ':' + mm + ':' + ss

    def mesg_box_watcher(self):
        global p2p_mesg_box
        while True:
            if len(p2p_mesg_box) > 0:
                mesg = p2p_mesg_box.popleft()

                if mesg.startswith("ERROR>"):
                    #self.state = "error"
                    logger.error(mesg)

                elif mesg.startswith("WARN>"):
                    logger.warning(mesg)
                    if "UPS END" in mesg:
                        bibi(150,4)
                        sleep(1.2)
                        os.system('shutdown now')

                elif mesg.startswith("INFO>"):
                    if 'zprobe_offset_sensor' in mesg:#G33
                        UI_mesg_box.append("leveling:0")

                    elif 'Auto_leveing finish' in mesg:#G29
                        pass

                    elif 'current_offset' in mesg:#G35
                        pass
                        
                # elif mesg.startswith("ECHO>"):
                #     pass
                else:
                    if 'T:' in mesg:
                        self._extruderTemp = float(re.search("T:*([0-9\.-]*)", mesg).group(1))
                        if self._extruderTemp > self._g.extruderTargetTemp - 0.5      :
                            self._hot_header = True
                            # logger.info("heating done")
                        elif self._extruderTemp < self._g.extruderTargetTemp - 3:
                            self._hot_header = False
                        if 'B:' in mesg:
                            self._bedTemp = float(re.search("B:*([0-9\.-]*)", mesg).group(1))
                        self._temp_timeout = time() + 3

                    elif 'X:' in mesg and 'Y:' in mesg and 'Z:' in mesg and 'E:' in mesg:
                        self._currentX = float(re.search("X:([0-9\.-]*)", mesg).group(1))
                        self._currentY = float(re.search("Y:([0-9\.-]*)", mesg).group(1))
                        self._currentZ = float(re.search("Z:([0-9\.-]*)", mesg).group(1))
                        self._currentE = float(re.search("E:([0-9\.-]*)", mesg).group(1))
                        if 'F:' in mesg:
                            self._currentF = float(re.search("F:*([0-9\.-]*)", mesg).group(1))
                        else:
                            self._currentF = 3600
                if not "ok" in mesg:
                    print "__WEB__"
                    print mesg
                    web_mesg_box.append(mesg)
            else:
                sleep(0.05)

    def web_box_getter(self):
        global web_mesg_box
        res = []
        while len(web_mesg_box):
            item = web_mesg_box.popleft()
            if len(item) > 0:
                res.append(item)
            else:
                continue
        return res

    def UI_box_getter(self):
        global UI_mesg_box
        res = []
        while len(UI_mesg_box):
            item = UI_mesg_box.popleft()
            if len(item) > 0:
                res.append(item)
            else:
                continue
        return res


def test():
    m = mostfun()
    print "begin"
    sysstr = platform.system()
    if (sysstr == "Linux"):
        m.beginTask(r'/home/test.gcode')
    elif (sysstr == "Windows"):
        m.beginTask("E:\\test.gcode")
    print "#print"

#         while True:
#            sleep(1)
#         return m


# if __name__ == '__main__':
#    test()