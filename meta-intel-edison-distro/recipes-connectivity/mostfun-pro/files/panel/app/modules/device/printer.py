#!/usr/bin/env python
# coding:utf-8
import os
import threading
import time
import platform
import re
import ConfigParser

import serial

from app import PATH_
from ..utils.Utils import copyFile, deleteFileFolder

# Debug Mode
# 1>no info
# 2>show info
# 3>more info
DEBUGMODE = 1

sysstr = platform.system()
if (sysstr == "Windows"):
    SERIALPORT = 'COM3'
elif (sysstr == "Linux"):
    # Sail 外接edison调试用 ttyUSB0 口
    # Pro 直接调试用 ttyMFD1 口
    SERIALPORT = '/dev/ttyMFD1'
SERIALBAUD = 115200

# pause\resume gcode templet
pauseList = ['G1 Z', 'G1 F9000 X0 Y130', ';pause']
resumeList = ['', '', ';resume']
cancelList = ['G1 Z', 'G1 F9000 X0 Y0', 'M140 S0', 'M109 S0', ';cancel']
cleanList = ['G1 Z', 'G1 F9000 X130 Y130', 'G1 F5000 X130 Y120', 'G1 X120 Y120', 'G1 X120 Y130', ';clean']

taskList = ConfigParser.ConfigParser()
# taskList.readfp(open('tasks.sav'))
# taskList.read(['task.sav', os.path.expanduser('')])


class gcode(object):
    def __init__(self):
        self.position = 0
        self.list = list()
        self._layerCount = 0
        self._layerNum = 0
        self.q = list()

    def load(self, path):
        self._f = open(path, 'r')
        self.q = self._f.readlines()
        self.q.insert(0, ';mostfun')
        self.q.insert(1, 'M110')
        # return self.q


class mostfun(object):
    def __init__(self, port=SERIALPORT, baud=SERIALBAUD):
        # ready\printing\pause\waiting\error
        self.state = 'ready'
        self._filePath = ''
        self._serial = serial.Serial(port, baud, timeout=3, writeTimeout=10000)

        self._extruderTemp = 0
        self._extruderTargetTemp = 0
        self._bedTemp = 0
        self._bedTargetTemp = 0
        self._currentX = 0
        self._currentY = 0
        self._currentZ = 0
        self._currentF = 0

        self._g = gcode()
        self._lineNum = 1
        self._saveLastLineNum = 0
        self._lock = False
        self._pauseLine = 0
        # self._tempLineNum = 1
        # self._stopLineNum = 1

        self._queue = list()

        thread = threading.Thread(target=self._monitor)
        thread.daemon = True
        thread.start()

    def lock(self):
        self.state = 'waiting'
        self._lock = True

    def unlock(self):
        self.state = 'printing'
        self._lock = False

    def beginTask(self, path):
        # sendGcodeFile
        if self.state == 'ready':
            deleteFileFolder(PATH_['TmpFolder'])
            copyFile(path, PATH_['TmpFolder'])
            # self._filePath = path
            self._filePath = PATH_['TmpFolder'] + path.split('/').pop()
            self._g.load(self._filePath)
            self._lineNum = 1
            self.state = 'printing'

    def cancelTask(self):
        # 取消打印
        if self.state == 'printing' or self.state == 'pause':
            self.lock()
            self.reset()

            self._g = gcode()
            self._filePath = ''

            time.sleep(3)
            self.sendCommand('G28 X0 Y0')
            self.unlock()
            self.state = 'ready'

    def pauseTask(self):
        if self.state == 'printing':
            self.lock()
            pauseList[0] = 'G1 Z' + str(self._currentZ + 10)
            self._saveLastLineNum = self._lineNum - 1
            tempLineNum = self._lineNum
            for command in pauseList:
                self._g.q.insert(tempLineNum, command)
                tempLineNum += 1
            self.unlock()

    def resumeTask(self):
        # 恢复打印
        if self.state == 'pause':
            # self.cleanNozzle()
            self.lock()
            tempF = ''
            tempX = ''
            tempY = ''
            tempZ = ''
            tempLineNum = self._saveLastLineNum
            while (tempLineNum > 0):
                command = self._g.q[tempLineNum]
                if ';' in command:
                    command = command[0:command.find(';')]
                command = command.rstrip()
                if 'G0' in command or 'G1' in command:
                    if 'F' in command and tempF == '':
                        tempF = re.search('F([0-9]+)', command).group(1)
                    if 'X' in command and tempX == '':
                        tempX = re.search('X([0-9]+)', command).group(1)
                    if 'Y' in command and tempY == '':
                        tempY = re.search('Y([0-9]+)', command).group(1)
                    # if 'Z' in command and tempZ == '':
                    #     tempZ = re.search('Z([0-9]+)',command).group(1)
                    if tempX != '' and tempY != '' and tempF != '':
                        break
                tempLineNum -= 1
            command = 'G1 F9000 X' + tempX + ' Y' + tempY + ' Z' + str(self._currentZ - 10)
            self._g.q.insert(self._lineNum, command)
            tempLineNum = self._lineNum + 1
            while (tempLineNum < len(self._g.q)):
                command = self._g.q[tempLineNum]
                if ';' in command:
                    command = command[0:command.find(';')]
                command = command.rstrip()
                if 'G0' in command or 'G1' in command:
                    if '\n' in command:
                        command = command.rstrip('\n')
                    if 'F' not in command:
                        self._g.q[tempLineNum] = command + ' F' + tempF
                        break
                tempLineNum += 1
            self.unlock()

    def saveTask(self, name):
        if self.state != 'pause':
            self.pauseTask()
        ##saving to tasks.sav
        taskName = os.path.basename(self._filePath)
        taskList.add_section(taskName)
        taskList.set(taskName, 'time', self._filePath)
        taskList.set(taskName, 'lineNum', self._filePath)
        taskList.set(taskName, 'lastX', self._filePath)
        taskList.set(taskName, 'lastY', self._filePath)
        taskList.set(taskName, 'lastZ', self._filePath)
        taskList.set(taskName, 'lastZ', self._filePath)
        # get real time
        self._filePath
        self._lineNum
        self.state = 'ready'

    def loadTask(self):
        # load from tasks.sav
        if self.state == 'ready':
            self.state = 'pause'

    def listTask(self):
        return taskList.sections()

    # 清理喷头,Xmax Ymax放铜刷
    def cleanNozzle(self):
        if self.state == 'pause':
            self.state = 'waiting'
            tempLineNum = self._lineNum
            for command in cleanList:
                self._g.q.insert(tempLineNum, command)
                tempLineNum += 1
            self.state = 'printing'

    # 蜂鸣器BBB
    def buzz(self, times):
        if times == 1:
            pass
        elif times == 2:
            pass
        elif times == 3:
            pass
        pass

    sysstr = platform.system()
    if (sysstr == "Linux"):
        import mraa
        try:
            ResetPin = mraa.Gpio(36)
        except Exception:
            ResetPin = mraa.Gpio(11)
        ResetPin.dir(mraa.DIR_OUT)

        def rst(self):
            self.ResetPin.write(1)
            time.sleep(1)
            self.ResetPin.write(0)

        def Init(self):
            self.ResetPin.write(0)
    elif (sysstr == "Windows"):
        def rst(self):
            self._serial.setDTR(0)
            time.sleep(1)
            self._serial.setDTR(1)

    def reset(self):
        self.state = 'ready'
        self._extruderTargetTemp = 0
        self._bedTargetTemp = 0
        self.rst()

    def _queueAdd(self, command):
        self._queue.append(command)

    def _queueGet(self):
        return self._queue.pop(0)

    def sendCommand(self, command):
        # if 'M109' in command or 'M190' in command:
        #     self.state=='warm-up'
        if 'M104' in command or 'M109' in command:
            try:
                self._extruderTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                if DEBUGMODE == 9:
                    print('_extruderTargetTemp:' + str(self._extruderTargetTemp))
            except:
                pass
        elif 'M140' in command or 'M190' in command:
            try:
                self._bedTargetTemp = float(re.search('S([0-9]+)', command).group(1))
                if DEBUGMODE == 9:
                    print('_bedTargetTemp:' + str(self._bedTargetTemp))
            except:
                pass
        elif ('G0' in command or 'G1' in command):
            try:
                if 'Z' in command:
                    z = float(re.search('Z([0-9\.]*)', command).group(1))
                    if self._currentZ != z:
                        self._currentZ = z
            except:
                pass
        if 'M24' in command:
            self.resumeTask()
        elif 'M25' in command:
            self.pauseTask()
        else:
            self._serial.write(command + '\n')
            if DEBUGMODE == 3:
                print('send:' + command)

    def _sendNextLine(self):
        if self._lineNum >= len(self._g.q):
            self.state = 'ready'
            return
        if self._lock and self._lineNum > self._pauseLine:
            self.state = 'pause'
            return
        command = self._g.q[self._lineNum]
        if DEBUGMODE > 3:
            print('get command:' + command)
        if ';' in command:
            if ';Layer count:' in command:
                self._g._layerCount = int(re.search(';Layer count: *([0-9]*)', command).group(1))
            if ';LAYER:' in command:
                self._g._layerNum = int(re.search(";LAYER:(-?[0-9]*)", command).group(1))
            if ';pause' in command and self._pauseLine != 0:
                self._pauseLine = self._lineNum
            command = command[0:command.find(';')]
        command = command.rstrip()
        if '\n' in command:
            command = command.rstrip('\n')
        self.sendCommand(self._addChecksum(command))
        self._lineNum += 1

    def _addChecksum(self, command, lineNum=0):
        if lineNum == 0:
            lineNum = self._lineNum
        checksum = reduce(lambda x, y: x ^ y, map(ord, "N%d%s" % (lineNum, command)))
        CommandWithChecksum = "N%d %s *%d\n" % (lineNum, command, checksum)
        return CommandWithChecksum

    def _receiveResponse(self):
        Response = self._serial.readline()
        if DEBUGMODE > 3:
            print('Response:' + Response)
        if Response.startswith('Error:'):
            if re.match('Error:[0-9]\n', Response):
                Response = self._serial.readline()
        if 'T:' in Response or Response.startswith('T:'):
            try:
                self._extruderTemp = float(re.search("T: *([0-9\.]*)", Response).group(1))
                if DEBUGMODE > 4:
                    print('extruderTemp:' + str(self._extruderTemp))
                if 'B:' in Response:
                    self._bedTemp = float(re.search("B: *([0-9\.]*)", Response).group(1))
                    if DEBUGMODE > 4:
                        print('bedTemp:' + str(self._bedTemp))
            except:
                pass
        if self.state == 'ready' or self.state == 'pause':
            if Response == '' and time.time() > self._tempTimeout:
                self._tempTimeout = time.time() + 1
                self.sendCommand('M105')
        elif self.state == 'printing':
            if time.time() > self._tempTimeout:
                self._tempTimeout = time.time() + 5
                self._queueAdd('M105')
            if Response == '' and time.time() > self._timeout:
                if DEBUGMODE > 5:
                    print('Communication timeout')
                Response = 'ok'
            if 'ok' in Response:
                self._timeout = time.time() + 5
                if len(self._queue) > 0:
                    self.sendCommand(self._queueGet())
                else:
                    self._sendNextLine()
            elif 'Resend' in Response or "rs" in Response:
                if DEBUGMODE > 1:
                    print('Response:' + Response)
                try:
                    self._lineNum = int(Response.replace("N:", " ").replace("N", " ").replace(":", " ").split()[-1])
                except:
                    self._lineNum = int(Response.split()[1])
        else:
            pass

    def _monitor(self):
        self._timeout = time.time() + 15
        self._tempTimeout = time.time() + 5
        while True:
            self._receiveResponse()


def test():
    m = mostfun()
    print('3\n')
    time.sleep(1)
    print('2\n')
    time.sleep(1)
    print('1\n')
    time.sleep(1)
    sysstr = platform.system()
    if (sysstr == "Linux"):
        m.beginTask(r'/home/20mm.gcode')
        return m
    elif (sysstr == "Windows"):
        m.beginTask("C:\\100mm.gcode")
        return m
