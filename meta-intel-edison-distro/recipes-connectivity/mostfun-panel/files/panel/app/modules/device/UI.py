# -*- coding:utf-8 -*-
from __future__ import division

import os
import shutil
import subprocess
import threading
from time import sleep, time

import Image
import ImageDraw
import ImageFont
import mraa
from configobj import ConfigObj

from app import g_p_
from ..utils.Utils import getINI
from ... import logger

number = 0

ENCODER_PATH = r'/dev/ttymcu0'
FONT_CN = r'/mostfun/panel/font/HelveticaNeueLTPro-Cn.otf'
FONT_BDCN = r'/mostfun/panel/font/HelveticaNeueLTPro-BdCn.otf'
FONT_MDCN = r'/mostfun/panel/font/HelveticaNeueLTPro-MdCn.otf'

FONT_CN_ZH = r'/mostfun/panel/font/SourceHanSansCN-Normal.otf'
FONT_BDCN_ZH = r'/mostfun/panel/font/SourceHanSansCN-Regular.otf'
FONT_MDCN_ZH = r'/mostfun/panel/font/SourceHanSansCN-Medium.otf'
# //font_CN
# FONT_MDCN = r'/mostfun/panel/font/SourceHanSansCN-Medium.otf'

PATH_LOCAL = r'/home/mostfuncp/gcode/'
PATH_SDCARD = r'/media/sdcard/'
PATH_USB = r'/media/usb/'
PATH_PAUSED = r'/home/mostfuncp/paused/'
PATH_INTERRUPTED = r'/home/mostfuncp/interrupted/'
PATH_TMP = r'/home/mostfuncp/tmp/'

# icons
ICON_PATH_PRINT = r'/mostfun/panel/bg/icon/start.bmp'
ICON_PATH_STOP = r'/mostfun/panel/bg/icon/stop.bmp'
ICON_PATH_PAUSE = r'/mostfun/panel/bg/icon/pause.bmp'
BTN_PATH_UP0 = r'/mostfun/panel/bg/icon/up0.bmp'
BTN_PATH_UP1 = r'/mostfun/panel/bg/icon/up1.bmp'
BTN_PATH_DOWN0 = r'/mostfun/panel/bg/icon/down0.bmp'
BTN_PATH_DOWN1 = r'/mostfun/panel/bg/icon/down1.bmp'

# imgs
IMG_PATH_FEEDIN = r'/mostfun/panel/bg/img/feedin.bmp'
IMG_PATH_PULLOUT = r'/mostfun/panel/bg/img/pullout.bmp'
IMG_PATH_FEEDIN1 = r'/mostfun/panel/bg/img/feedin1.bmp'
IMG_PATH_PULLOUT1 = r'/mostfun/panel/bg/img/pullout1.bmp'
IMG_PATH_FEEDIN2 = r'/mostfun/panel/bg/img/feedin2.bmp'
IMG_PATH_PULLOUT2 = r'/mostfun/panel/bg/img/pullout2.bmp'
IMG_HEATING1 = r'/mostfun/panel/bg/img/heating1.bmp'
IMG_HEATING2 = r'/mostfun/panel/bg/img/heating2.bmp'
IMG_LEVELING0 = r'/mostfun/panel/bg/img/leveling0.bmp'
IMG_LEVELING1 = r'/mostfun/panel/bg/img/leveling1.bmp'
IMG_LEVELING2 = r'/mostfun/panel/bg/img/leveling2.bmp'
IMG_LEVELING3 = r'/mostfun/panel/bg/img/leveling3.bmp'
IMG_LEVELING4 = r'/mostfun/panel/bg/img/leveling4.bmp'
IMG_LEVELING5 = r'/mostfun/panel/bg/img/leveling5.bmp'
IMG_LEVELING6 = r'/mostfun/panel/bg/img/leveling6.bmp'
IMG_LEVELING7 = r'/mostfun/panel/bg/img/leveling7.bmp'
IMG_LEVELING8 = r'/mostfun/panel/bg/img/leveling8.bmp'
IMG_LEVELING9 = r'/mostfun/panel/bg/img/leveling9.bmp'
IMG_LEVELING10 = r'/mostfun/panel/bg/img/leveling10.bmp'

IMG_PATH_EX1 = r'/mostfun/panel/bg/img/ex1.bmp'
IMG_PATH_EX2 = r'/mostfun/panel/bg/img/ex2.bmp'
IMG_PATH_EX3 = r'/mostfun/panel/bg/img/ex3.bmp'
IMG_PATH_EX4 = r'/mostfun/panel/bg/img/ex4.bmp'
IMG_PATH_QRwlan1 = r'/mostfun/panel/bg/img/QRwlan1.bmp'
IMG_PATH_QRwlan0 = r'/mostfun/panel/bg/img/QRwlan0.bmp'
# backgrands
PATH_QR_AP = r'/mostfun/panel/bg/bg/back.bmp'
PATH_QR_STA = r'/mostfun/panel/bg/bg/back.bmp'
PATH_LOGO = r'/mostfun/panel/bg/bg/logo.bmp'
PATH_BLACK = r'/mostfun/panel/bg/bg/back.bmp'
PATH_ATTENTION = r'/mostfun/panel/bg/bg/attention.bmp'
PATH_WARNING = r'/mostfun/panel/bg/bg/warning.bmp'
PATH_ERROR = r'/mostfun/panel/bg/bg/error.bmp'
PATH_UPGRADE = r'/mostfun/panel/bg/bg/upgrading.bmp'
PATH_EXTRUD = r'/mostfun/panel/bg/bg/extrud.bmp'
PATH_TEST = r'/mostfun/panel/bg/bg/test.bmp'
PATH_POEWRDOWN = r'/mostfun/panel/bg/bg/powerdown.bmp'
PATH_REFILLTEST = r'/mostfun/panel/bg/bg/refilltest.bmp'
PATH_SLEEP = r'/mostfun/panel/bg/bg/logo.bmp'
PATH_HEATING = r'/mostfun/panel/bg/bg/heating.bmp'
PATH_LEVELING = r'/mostfun/panel/bg/bg/back.bmp'
PATH_ADJUSTING = r'/mostfun/panel/bg/bg/adjusting.bmp'

PATH_FRAME_BUFFER = r'/tmp/page.bmp'

COLOR_WHIT = 0xFFFFFF
COLOR_BLACK = 0x00
COLOR_DARK_GRAY = 0x666666
COLOR_LIGHT_GRAY = 0xAAAAAA
COLOR_RED = 0x0000FF
COLOR_BLUE = 0xFF0000
COLOR_GREEN = 0x00FF00

BUTTON_H = 34
BUTTON_W = 64

TEXT_LIST_W = 160
TEXT_LIST_TEXT_W = 136

LCD_SLEEP_TIMEOUT = 30
Page_timer = 0

Current_gcode_PATH = ""
Current_page = None
Local_files = []
SDcard_files = []

lang = getINI("other", "lang")

if lang == 'zh-CN':
    font_cn16 = ImageFont.truetype(FONT_CN_ZH, 15)
    font_cn18 = ImageFont.truetype(FONT_CN_ZH, 16)
    font_cn20 = ImageFont.truetype(FONT_CN_ZH, 18)
    font_bdcn20 = ImageFont.truetype(FONT_BDCN_ZH, 18)
    font_bdcn30 = ImageFont.truetype(FONT_BDCN_ZH, 24)
    font_mdcn24 = ImageFont.truetype(FONT_MDCN_ZH, 20)
    font_mdcn30 = ImageFont.truetype(FONT_MDCN_ZH, 24)
    UIconfig = ConfigObj("/mostfun/panel/app/modules/device/ZH.ini", encoding='UTF8')
else:
    font_cn16 = ImageFont.truetype(FONT_CN, 16)
    font_cn18 = ImageFont.truetype(FONT_CN, 18)
    font_cn20 = ImageFont.truetype(FONT_CN, 20)
    font_bdcn20 = ImageFont.truetype(FONT_BDCN, 20)
    font_bdcn30 = ImageFont.truetype(FONT_BDCN, 30)
    font_mdcn24 = ImageFont.truetype(FONT_MDCN, 24)
    font_mdcn30 = ImageFont.truetype(FONT_MDCN, 30)
    UIconfig = ConfigObj("/mostfun/panel/app/modules/device/EN.ini", encoding='UTF8')
font_mdcn50 = ImageFont.truetype(FONT_MDCN, 50)
font_cn16_ZH = ImageFont.truetype(FONT_CN_ZH, 15)
font_cn18_ZH = ImageFont.truetype(FONT_CN_ZH, 16)
font_cn20_ZH = ImageFont.truetype(FONT_CN_ZH, 18)
font_mdcn24_ZH = ImageFont.truetype(FONT_MDCN_ZH, 22)
font_mdcn30_ZH = ImageFont.truetype(FONT_MDCN_ZH, 24)

Black_light = bl = mraa.Gpio(21)
Lcd_sleep = False
screen = Image.open(PATH_SLEEP)
screen_draw = ImageDraw.Draw(screen)
p = subprocess.Popen("hostname", shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()
hostname = p.stdout.readlines()[0]
screen_draw.text((5,5),hostname, COLOR_WHIT, font_cn16_ZH)

currentIP = ''

sdPin = mraa.Gpio(6)
cmd_check_card_reader_name = "find /sys/devices/pci0000\:00/0000\:00\:11.0/dwc3-host.2/usb1/1-1/1-1.4/1-1.4\:1.0/ -name sd[a-z] | cut -d \/ -f 15"
cmd_check_USBstorage_name = "find /sys/devices/pci0000\:00/0000\:00\:11.0/dwc3-host.2/usb1/1-1/1-1.3/1-1.3\:1.0/ -name sd[a-z] | cut -d \/ -f 15"
# cmd_get_TFT_PID = '''ps | grep TFT_8340 |  grep -v "grep" | cut -d ' ' -f 3'''
# cmd_get_TFT_PID = "ps | grep TFT_8340 | grep -v grep | awk '{print$1}'"
SDcard = False
USBstorage = False
TFT_PID = 0

class base_ele(object):
    def  __init__(self,location,size,container=None,backgrand=None,isenable=True,isvisiable=True,isselected=0,handle=None,handleargs=None):
        self.location = location
        self.size = size
        self.container = container
        self.backgrand = backgrand
        self.isenable = isenable
        self.isvisiable = isvisiable
        self.isselected = isselected
        self.handle = handle
        self.handleargs = handleargs

    def click(self):
        if self.isenable:
            if self.handleargs == None:
                self.handle()
            else:
                self.handle(self.handleargs)
        else:
            pass

    def left_click(self):
        global Current_page
        Current_page.last_element()

    def right_click(self):
        global Current_page
        Current_page.next_element()

    def disable(self):
        self.isenable = False

    def enable(self):
        self.isenable = True

    def visiable(self):
        self.isvisiable = True
        self.selected = 0

    def unvisiable(self):
        self.isvisiable = False
        if self.isselected == 1:
            self.right_click()

    def draw(self):
        pass


class button(base_ele):
    def __init__(self, location,size, text, handle, handleargs=None):
        base_ele.__init__(self,location=location,size=size,handle=handle,handleargs=handleargs)
        self.text = text
        self.warning = False
        self.location2 = (self.location[0]+self.size[1],self.location[1]+self.size[0])

    def set_warning(self, warning=True):
        self.warning = warning

    def draw(self):
        textsize = self.container.textsize(self.text, font_bdcn30)
        textlocation = ((self.size[1]-textsize[0])/2+self.location[0],(self.size[0]-textsize[1])/2+self.location[1]+8)
        if self.isvisiable == True:
            if self.isenable == True:
                if self.selected == 0:
                    self.container.rectangle((self.location, self.location2), COLOR_BLACK)
                    self.container.text(textlocation, self.text, COLOR_WHIT, font_bdcn30)
                if self.selected == 1:
                    if self.warning:
                        self.container.rectangle((self.location, self.location2), COLOR_RED)
                        self.container.text(textlocation, self.text, COLOR_WHIT, font_bdcn30)
                    else:
                        self.container.rectangle((self.location, self.location2), COLOR_WHIT)
                        self.container.text(textlocation, self.text, COLOR_BLACK, font_bdcn30)
            elif self.isenable == False:
                if self.selected == 1:
                    self.container.rectangle((self.location, self.location2), COLOR_LIGHT_GRAY)
                    self.container.text(textlocation, self.text, COLOR_DARK_GRAY, font_bdcn30)
                if self.selected == 0:
                    self.container.rectangle((self.location, self.location2), COLOR_BLACK)
                    self.container.text(textlocation, self.text, COLOR_DARK_GRAY, font_bdcn30)


class button_img(base_ele):
    def __init__(self, location, imgpath, handle, args=None):
        base_ele.__init__(self,location=location,size=(0,0),handle=handle,handleargs=args)
        self.img = list()
        # 0:not selected 1:selected 2:disabled
        for path in imgpath:
            self.img.append(Image.open(path))
        self.warning = False
        # self.location2 = (self.location[0]+self.img[0].size[0],self.location[1]+self.img[0].size[1])

    def set_warning(self, warning=True):
        self.warning = warning

    def draw(self):
        if self.isenable:
            if self.selected == 0:
                self.backgrand.paste(self.img[0], self.location)
            if self.selected == 1:
                self.backgrand.paste(self.img[1], self.location)
        else:
            self.backgrand.paste(self.img[-1], self.location)


class menu(object):
    def __init__(self, name, items):
        self.name = name
        self.items = list()
        global UIconfig
        section = UIconfig[name]
        state = section['state']
        name = section.values()
        for i in range(0, len(items)):
            templist = list()
            templist.append(name[i])
            templist.append(items[i])
            templist.append(state[i])
            self.items.append(templist)

        self.current_item = self.items[0]
        self.container = None
        self.backgrand = None
        self.selected = 0

    def click(self):
        jump2page(self.current_item[1])

    def left_click(self):
        while True:
            self.current_item = self.items[self.items.index(self.current_item) - 1]
            if self.current_item[2] == "e":
                return

    def right_click(self):
        while True:
            if self.current_item == self.items[-1]:
                self.current_item = self.items[0]
            else:
                self.current_item = self.items[self.items.index(self.current_item) + 1]
            if self.current_item[2] == "e":
                return

    def disable_item(self, item_num):
        self.items[item_num][2] = "d"

    def enable_item(self, item_num):
        self.items[item_num][2] = "e"

    def hidden_item(self, item_num):
        self.items[item_num][2] = "h"

    # def drop_item(self,item_num):
    #     if self.current_item == self.items[item_num]:
    #         pass
    #     self.items.remove(item_num)

    # def additem(self,index,item):
    #     self.items.insert(index,item)

    def draw(self):
        rectangle = 20
        self.container.rectangle((0, 0, 219, 175), COLOR_BLACK)
        if not self.current_item[2] == "e":
            self.right_click()
        for item in self.items:
            if item[2] == "h":
                # self.right_click()
                continue
            if self.current_item == item:
                self.container.rectangle((0, rectangle - 2, 205, rectangle + 30), COLOR_WHIT)
                self.container.text((20, rectangle + 2), item[0], COLOR_BLACK, font_mdcn30)
                rectangle += 27
            else:
                if item[2] == "e":
                    self.container.text((20, rectangle + 7), item[0], COLOR_WHIT, font_cn18)
                elif item[2] == "d":
                    self.container.text((20, rectangle + 7), item[0], COLOR_DARK_GRAY, font_cn18)
                rectangle += 27


class file_list(object):
    def __init__(self, name, dirpath):
        self.name = name
        self.path = dirpath
        self.files = []
        self.refresh()
        self.current = 0
        self.offset = 0
        self.container = None
        self.backgrand = None
        self.selected = 0
        self.rolloffset = 0
        self.counter = 0

    def click(self):
        global Current_gcode_PATH
        if not len(self.files) == 0:
            Current_gcode_PATH = self.path + self.files[self.current]
            comfirming(self.files[self.current])
        else:
            jump2page(p_main_menu)
        self.rolloffset = 0
        self.counter = 0

    def left_click(self):
        if self.current > 0:
            self.current -= 1
        elif self.current == 0:
            self.current = len(self.files) - 1
        if self.current < self.offset:
            self.offset = self.current
        elif self.current > self.offset + 4:
            self.offset = self.current - 4
        self.rolloffset = 0
        self.counter = 0

    def right_click(self):
        if self.current < len(self.files) - 1:
            self.current += 1
        elif self.current == len(self.files) - 1:
            self.current = 0
        if self.current < self.offset:
            self.offset = self.current
        elif self.current > self.offset + 4:
            self.offset = self.current - 4
        self.rolloffset = 0
        self.counter = 0

    def refresh(self):
        if os.path.exists(self.path):
            self.files = os.listdir(self.path)
            for f in self.files:
                if f[-6:] != '.gcode':
                    self.files.remove(f)
        else:
            self.files = []

    def draw(self):
        if os.path.exists(self.path):
            self.container.line(((0, 30), (TEXT_LIST_W, 30)), fill=COLOR_WHIT, width=2)
            self.files = os.listdir(self.path)
            list_temp = list()
            for f in self.files:
                # print '---------'
                if f.endswith('.gcode'):
                    list_temp.append(f)
            self.files = list_temp

            self.container.rectangle((0, 34, 190, 175), COLOR_BLACK)
            if len(self.files) == 0:
                self.container.text((50, 45), UIconfig["mesg"]["empty"], COLOR_WHIT, font_cn18)
                return
            rectangle = 34

            for item in self.files[self.offset:self.offset + 5]:
                try:
                    item = item.decode()
                except Exception as e:
                    logger.error('file name decode failed')

                if self.current == self.files.index(item):
                    # draw selected item
                    self.container.rectangle((0, rectangle, TEXT_LIST_W, rectangle + 28), COLOR_WHIT)
                    if self.container.textsize(item, font_mdcn24_ZH)[0] <= TEXT_LIST_TEXT_W:
                        # short enough,no rolling
                        self.container.text((20, rectangle + 3), item, COLOR_BLACK, font_mdcn24_ZH)
                    else:
                        # long enough,rolling
                        img_w = self.container.textsize(item, font_mdcn24_ZH)[0] + TEXT_LIST_TEXT_W
                        img_tmp = Image.new("RGB", (img_w, 28), "white")
                        draw_tmp = ImageDraw.Draw(img_tmp)
                        draw_tmp.text((3, 3), item, COLOR_BLACK, font_mdcn24_ZH)
                        w = img_tmp.size[0]
                        box = (self.rolloffset, 0, self.rolloffset + TEXT_LIST_TEXT_W, 28)
                        disp = img_tmp.crop(box)

                        self.backgrand.paste(disp, (20, rectangle, 20 + TEXT_LIST_TEXT_W, rectangle + 28))
                        # self.container.text((20-self.rolloffset,rectangle+3),item,COLOR_BLACK,font_mdcn24)

                        if self.rolloffset >= img_w - TEXT_LIST_TEXT_W:
                            self.rolloffset = 0
                            self.counter = 0

                        self.counter += 1
                        if self.counter > 10:
                            self.rolloffset += 2

                    rectangle += 28

                else:
                    # pass
                    width = self.container.textsize(item, font_cn16_ZH)[0]
                    # draw unselected item
                    if width <= TEXT_LIST_TEXT_W:
                        self.container.text((20, rectangle + 3), item, COLOR_WHIT, font_cn16_ZH)
                    else:
                        self.container.text((20, rectangle + 3),
                                            item[:int(len(item) * (TEXT_LIST_TEXT_W / width)) - 2] + u"…", COLOR_WHIT,
                                            font_cn16_ZH)
                    rectangle += 24

            # draw sidebar
            if len(self.files) - 1 == 0:
                slider = 30
            else:
                slider = self.current / (len(self.files) - 1) * 102 + 30

            self.container.rectangle((160, 0, 219, 175), COLOR_BLACK)
            self.container.line(((200, 30), (200, 146)), fill=COLOR_WHIT, width=2)
            self.container.line(((200, slider), (200, slider + 14)), fill=COLOR_WHIT, width=8)


class printing(object):
    def __init__(self, name, printer):
        self.container = None
        self.backgrand = None
        self.selected = -1
        self.layers = 0
        self.current_layer = 0
        self.layer_offset = 0
        self.percent = 0
        self.E_temp = 0.0
        self.B_temp = 0.0
        self.E_target_temp = 0.0
        self.E_target_temp = 0.0
        self.time = "00:00:00"
        self.state = "--"
        self.icon_start = Image.open(ICON_PATH_PRINT, 'r')
        self.icon_stop = Image.open(ICON_PATH_STOP, 'r')
        self.icon_pause = Image.open(ICON_PATH_PAUSE, 'r')
        self.printer = printer
        self.file_name = Current_gcode_PATH.split(r'/')[-1]

    def refresh_printer_state(self):
        global Current_gcode_PATH
        if not self.file_name == Current_gcode_PATH.split(r'/')[-1]:
            # print Current_gcode_PATH.split(r'/')[-1]
            self.file_name = Current_gcode_PATH.split(r'/')[-1]
            print_name_rolling.set_text(self.file_name)
        Current_gcode_PATH = self.printer.get_currentfile()
        self.time = self.printer.get_times()
        self.layer_offset = self.printer._g.layer_offset
        self.current_layer = self.printer._g.layerNum - self.layer_offset
        self.layers = self.printer._g.layerCount - self.layer_offset
        self.percent = self.printer.get_percent()
        self.E_temp = self.printer.get_extruderTemp()
        self.B_temp = self.printer.get_bedTemp()
        self.E_target_temp = self.printer.get_extruderTargetTemp()
        self.B_target_temp = self.printer.get_bedTargetTemp()
        self.state = self.printer.get_state()

    def reset_state(self):
        self.layers = 0
        self.current_layer = 0
        self.percent = 0
        self.time = "00:00:00"

    def click(self):
        if self.state == "printing" or self.state == "pause":
            jump2page(p_printing_ctl_menu)
        else:
            jump2page(p_main_menu)

    def left_click(self):
        if self.state == "printing" or self.state == "pause":
            pass
        else:
            jump2page(p_main_menu)

    def right_click(self):
        self.left_click()

    def draw(self):
        self.container.rectangle((0, 32, 219, 175), COLOR_BLACK)

        if self.state == "printing":
            self.backgrand.paste(self.icon_start, (8, 115, 40, 147))

        elif self.state == "pause":
            self.backgrand.paste(self.icon_pause, (8, 115, 40, 147))

        self.container.text((10, 42), UIconfig["mesg"]["layers"] + str(self.current_layer) + '/' + str(self.layers),
                            COLOR_WHIT,
                            font_cn18)
        # self.container.text((10,67),"E_Temp:"+str(self.E_temp)+r'/'+str(self.E_target_temp)+'C',COLOR_WHIT,font_cn18)
        # self.container.text((10,89),"B_Temp:"+str(self.B_temp)+r'/'+str(self.B_target_temp)+'C',COLOR_WHIT,font_cn18)
        self.container.text((10, 70), UIconfig["mesg"]["complete"] + '%0.2f' % (self.percent) + '%', COLOR_WHIT,
                            font_cn18)

        # draw time
        self.container.text((210 - self.container.textsize(str(self.time), font_mdcn50)[0], 110), str(self.time),
                            COLOR_WHIT, font_mdcn50)
        # draw process bar
        self.container.line(((10, 155), (210, 155)), fill=COLOR_WHIT, width=1)
        self.container.line(((10, 166), (210, 166)), fill=COLOR_WHIT, width=1)
        self.container.line(((10, 155), (10, 166)), fill=COLOR_WHIT, width=1)
        self.container.line(((210, 155), (210, 166)), fill=COLOR_WHIT, width=1)
        # draw process bar process
        if self.percent >= 0:
            self.container.line(((12, 161), (int(12 + 196.0 * (self.percent / 100.0)), 161)), fill=COLOR_WHIT, width=8)


class static_p(object):
    def __init__(self):
        self.selected = -1

    def click(self):
        jump2page(Last_page)

    def left_click(self):
        jump2page(Last_page)

    def right_click(self):
        jump2page(Last_page)

    def draw(self):
        pass


class textbox(object):
    def __init__(self, position, textshow, style="middle", fontb=font_cn18_ZH, fonts=font_cn16_ZH):
        if position == "center":
            self.X = 4
            self.Y = 50
            self.XX = 215
            self.YY = 106
        else:
            self.X = position[0]
            self.Y = position[1]
            self.XX = position[2]
            self.YY = position[3]
        self.style = style
        self.textstr = textshow.decode()
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.fontb = fontb
        self.fonts = fonts
        self.font = fontb
        self.cursor = [0, 0]
        self.char_H = 0
        self.char_W = 0

    def set_text(self, text):
        self.textstr = text.decode()

    def type_a_char(self, char):
        width = self.container.textsize(char, self.font)[0]
        height = self.container.textsize(char, self.font)[1]
        if height + self.cursor[1] > self.YY - self.Y:
            return

        if width + self.cursor[0] > self.XX - self.X:
            self.cursor[0] = 0
            self.cursor[1] += height

        self.container.text((self.cursor[0] + self.X, self.cursor[1] + self.Y), char, COLOR_WHIT, self.font)
        self.cursor[0] += width

    def draw(self):
        size = self.container.textsize(self.textstr, self.font)
        if size[0] * size[1] > (self.XX - self.X) * (self.YY - self.Y):
            self.font = self.fonts

        self.container.rectangle((self.X, self.Y, self.XX, self.YY), COLOR_BLACK)
        if size[0] <= self.XX - self.X:
            if self.style == "middle":
                self.container.text((self.X + ((self.XX - self.X - size[0]) / 2), self.Y),
                                    self.textstr, COLOR_WHIT, self.font)
            elif self.style == "left":
                self.container.text((self.X, self.Y), self.textstr, COLOR_WHIT, self.font)
        else:
            # self.cursor[1] = self.YY-self.Y-(size[1]*int(size[0]/(self.XX-self.X)))/2
            for c in self.textstr:
                # print c.encode()
                self.type_a_char(c)
            self.cursor = [0, 0]


class timer_show(object):
    def __init__(self, position, count, font=font_cn20):  # only Y coordinate is needed
        self.position = position
        self.counter = count
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.font = font

    def draw(self):
        current_T = self.counter - int(time() - Page_timer)
        size = self.container.textsize(str(current_T) + "s", self.font)
        self.container.rectangle(
            (self.position[0], self.position[1], self.position[0] + size[0] + 12, self.position[1] + size[1] - 6),
            COLOR_BLACK)
        self.container.text(self.position, str(current_T) + "s", COLOR_WHIT, self.font)


class rolling_text(object):
    def pre_draw(self):
        self.image = Image.new("RGB", (100, 100), "black")
        self.tempdraw = ImageDraw.Draw(self.image)
        self.img_size = self.tempdraw.textsize(self.textstr, self.font)
        self.image = self.image.resize(self.img_size)
        self.tempdraw = ImageDraw.Draw(self.image)
        self.tempdraw.text((0, 3), self.textstr, COLOR_WHIT, self.font)
        self.box = None
        self.disp = None

    def __init__(self, position_Y, textshow, font=font_mdcn24_ZH, style='l'):  # only Y coordinate is needed
        self.position = position_Y
        self.textstr = textshow.decode()
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.font = font
        self.cursor = [0, 0]
        self.rolloffset = 0
        self.style = style
        self.pre_draw()
        self.speed = 3
        self.dirty = True

    def set_text(self, text):
        self.textstr = text.decode()
        self.pre_draw()
        self.dirty = True

    def draw(self):
        if self.dirty == True:
            if self.img_size[0] <= 220:
                if self.style == 'm':
                    self.backgrand.paste(self.image, (
                    (220 - self.img_size[0]) / 2, self.position, (220 - self.img_size[0]) / 2 + self.img_size[0],
                    self.position + self.img_size[1]))
                elif self.style == 'l':
                    self.backgrand.paste(self.image,
                                         (0, self.position, self.img_size[0], self.position + self.img_size[1]))
                elif self.style == 'r':
                    self.backgrand.paste(self.image,
                                         (220 - self.img_size[0], self.position, 220, self.position + self.img_size[1]))
                self.dirty = False
            else:
                # long enough,rolling

                self.box = (self.rolloffset, 0, self.rolloffset + 220, self.img_size[1])
                self.disp = self.image.crop(self.box)

                self.backgrand.paste(self.disp, (0, self.position, 220, self.position + self.img_size[1]))
                if self.rolloffset >= self.img_size[0]:
                    self.rolloffset = 0

                self.rolloffset += self.speed
                self.dirty = True


class image(object):
    def __init__(self, X, Y, imgpath, times=-1):
        self.X = X
        self.Y = Y
        self.img = list()
        for path in imgpath:
            self.img.append(Image.open(path))
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.xx = self.X + self.img[0].size[0]
        self.yy = self.Y + self.img[0].size[1]
        self.frame = 0
        self.times = times
        self.speed = 5

    def play(self, times):
        self.times = times * len(self.img) * self.speed

    def draw(self):
        if self.times == 0:
            self.backgrand.paste(self.img[0], (self.X, self.Y, self.xx, self.yy))
        else:
            if self.frame == len(self.img) * self.speed:
                self.frame = 0
            self.container.rectangle((self.X, self.Y, self.xx, self.yy), COLOR_BLACK)
            self.backgrand.paste(self.img[int(self.frame / self.speed)], (self.X, self.Y, self.xx, self.yy))
            self.frame += 1
            if self.times > 0:
                self.times -= 1


class process_bar(object):
    def __init__(self, (X, Y), (XX, YY), color=COLOR_BLACK):
        self.start = (X, Y)
        self.end = (XX, YY)
        self.persent = 0.0
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.color = color
        self.dirty = True

    def set_persent(self, persent):
        self.persent = persent
        self.dirty = True

    def draw(self):
        if self.dirty == True:
            # print self.persent
            self.container.line((self.start, self.end), fill=COLOR_BLACK, width=5)
            endx = int((self.end[0] - self.start[0]) * self.persent + self.start[0])
            endy = int((self.end[1] - self.start[1]) * self.persent + self.start[1])

            self.container.line((self.start, (endx, endy)), fill=self.color, width=5)
            self.dirty = False


class shap_line(object):
    def __init__(self, location, color=COLOR_BLACK,width=5):
        self.location = location#X1,Y1,X2,Y2
        self.width = width
        self.selected = -1
        self.container = None
        self.backgrand = None
        self.color = color
        self.dirty = True
        self.offset = [0,0]#X,Y 
        self.range = [0,0,0,0]#X+,X-,Y+,Y-

    def set_range(self,ran):
        self.range = ran

    def set_offset(self, offset):
        if self.offset[0]+offset[0]>=self.range[0] and self.offset[0]+offset[0]<=self.range[1] and \
            self.offset[1]+offset[1]>=self.range[2] and self.offset[1]+offset[1]<=self.range[3] :

            self.container.line([self.location[0] + self.offset[0],self.location[1] + 
                    self.offset[1],self.location[2] + self.offset[0],self.location[3] + 
                    self.offset[1]],fill=COLOR_BLACK, width=self.width)
            self.offset[0] += offset[0]
            self.offset[1] += offset[1]
            self.dirty = True

    def draw(self):
        if self.dirty == True:
        # print self.persent
            if self.offset[0]==self.range[0] or self.offset[0]==self.range[1] or \
                self.offset[1]==self.range[2] or self.offset[1]==self.range[3]:
                color = COLOR_RED
            else:
                color = self.color
            self.container.line([self.location[0] + self.offset[0],self.location[1] + 
                self.offset[1],self.location[2] + self.offset[0],self.location[3] + 
                self.offset[1]],fill=color, width=self.width)
            self.dirty = False


class page(object):
    def __init__(self, backgrand_path, owner=("ready",), enablehoming=True):
        self.backgrand = Image.open(backgrand_path)
        self.container = ImageDraw.Draw(self.backgrand)
        self.elements = []
        self.shows = []
        self.current_element = None
        self.dirty = True
        self.owner = owner
        self.timeout = 0
        self.handle = None
        self.handleargs = None
        self.action = None
        self.actionargs = None
        self.isdisable = False
        self.autojump = None
        self.enable_autojump = False
        self.enable_homing = enablehoming

    def page_enable(self):
        self.isdisable = False

    def page_disable(self):
        self.isdisable = True

    def set_action(self, action, args=None):
        self.action = action
        self.actionargs = args

    def set_timeout(self, timeout, handle, args=None):
        self.timeout = timeout
        self.handle = handle
        self.handleargs = args

    def add_ele(self, ele):
        self.elements.append(ele)
        ele.container = self.container
        ele.backgrand = self.backgrand
        self.current_element = self.elements[-1]

    def add_show(self, show):
        self.shows.append(show)
        show.container = self.container
        show.backgrand = self.backgrand

    def set_auto_jump(self, page):
        self.autojump = page

    def enable_jump(self):
        self.enable_autojump = True

    def disable_jump(self):
        self.enable_autojump = False

    def draw_page(self):
        pass

    def flush_page(self):
        global Page_timer
        if self.isdisable == True:
            jump2page(p_home)
        else:
            if not self.timeout == 0:
                if time() - Page_timer > self.timeout:
                    if not self.handleargs == None:
                        self.handle(self.handleargs)
                    else:
                        self.handle()

            for ele in self.elements:
                if ele == self.current_element:
                    ele.selected = 1
                else:
                    ele.selected = 0
                ele.draw()
            for show in self.shows:
                show.draw()

            self.backgrand.save(PATH_FRAME_BUFFER)

    def last_element(self):
        #TODO, attention ,dead loop probably when set all ele to unvisiable
        while True:
            self.current_element = self.elements[self.elements.index(self.current_element) - 1]
            if self.current_element.isvisiable == True:
                break

    def next_element(self):
        #TODO, attention ,dead loop probably when set all ele to unvisiable
        while True:
            if self.current_element == self.elements[-1]:
                self.current_element = self.elements[0]
            else:
                self.current_element = self.elements[self.elements.index(self.current_element) + 1]
            if self.current_element.isvisiable == True:
                break

    def click(self,key):
        global Page_timer
        Page_timer = time()
        if key == '0':
            try:
                self.current_element.click()
                # Current_page.dirty = True
                print '0'
            except:
                pass
        elif key == '1':
            if self.enable_homing == True:
                jump2page(p_home)
            # Current_page.dirty = True

        elif key == '<':
            try:
                self.current_element.left_click()
                # Current_page.dirty = True
            except:
                pass

        elif key == '>':
            try:
                self.current_element.right_click()
                # Current_page.dirty = True
            except:
                pass

class encoder(object):
    def __init__(self, dev=ENCODER_PATH):
        self._device = open(dev, 'r')
        self.state = 'n'

    def refresh_state(self):
        self.state = self._device.read(1)


def black_light(state):
    if state == "on":
        Black_light.write(1)
    elif state == "off":
        Black_light.write(0)


def begin_printing(gcode=None):
    waiting(UIconfig["mesg"]["load"])
    # menu_printing_ctl.redirect_item(0, ["Pause", p_pause_printing, 1])
    # menu_printing_ctl.hidden_item(1)
    # menu_printing_ctl.enable_item(0)
    if gcode == None:
        global Current_gcode_PATH
        gcode = Current_gcode_PATH
    if g_p_.mostfun.beginTask(gcode) == False:
        warning("Invalid G-code,cancel")
        sleep(3)
        cancel_printing()
        return
    p_home = p_printing
    # print gcode
    p_heating.enable_jump()
    jump2page(p_heating)


def cancel_printing():
    waiting(UIconfig["mesg"]["wait"])
    g_p_.mostfun.cancelTask()
    p_home = p_main_menu
    jump2page(p_home)


def pause_printing():
    g_p_.mostfun.pauseTask()
    # menu_printing_ctl.hidden_item(0)
    # menu_printing_ctl.enable_item(1)
    jump2page(p_home)


def resume_printing():
    g_p_.mostfun.resumeTask()
    # menu_printing_ctl.hidden_item(1)
    # menu_printing_ctl.enable_item(0)
    jump2page(p_home)


def save_printing(powerdown=False):
    waiting(UIconfig["mesg"]["wait"])
    g_p_.mostfun.stop_saveTask(powerdown)
    if powerdown == False:
        p_home = p_main_menu
        jump2page(p_home)


def jump2page(page):
    global Current_page
    global Last_page
    global Page_timer
    Page_timer = time()

    if page == p_printing_ctl_menu:
        if g_p_.mostfun.get_state() == 'pause':
            menu_printing_ctl.enable_item(-1)
            menu_printing_ctl.hidden_item(0)
            menu_printing_ctl.enable_item(1)
        else:
            menu_printing_ctl.disable_item(-1)
            menu_printing_ctl.hidden_item(1)
            menu_printing_ctl.enable_item(0)

    elif page == p_refill:
        g_p_.mostfun.send_command(["G28 Z","G1 F3600 X110 Y120"])
        if g_p_.mostfun.get_extruderTargetTemp() < 210:
            g_p_.mostfun.send_command(["M104 S210.000000"])
    elif page == p_connection_menu:
        waiting(UIconfig["mesg"]["checkwifi"])
        check_wifi("wlan0", 1)
        check_wifi("ra0", 0)
    elif page == p_continue:
        file_name_rolling.set_text(Current_gcode_PATH.split(r'/')[-1])
    elif page == p_auto_leveling:
        Btn_adjusting.disable()
    if len(page.elements) >= 1:
        page.current_element = page.elements[-1]
    Last_page = Current_page
    Current_page = page


def jumpback():
    global Last_page
    jump2page(Last_page)


def extrud():
    # extrud test gcode
    # M109 S100.000000
    # G91
    # G1 F1200 E10
    # G90
    Img_ex_test.play(8)
    g_p_.mostfun.send_command(["G91", "G1 F200 E20", "G90"])


def Z_up():
    img_bord.set_offset([0,-1])
    g_p_.mostfun.send_command(["G91", "G1 F200 Z-0.1", "G90"])


def Z_down():
    img_bord.set_offset([0,1])
    g_p_.mostfun.send_command(["G91", "G1 F200 Z0.1", "G90"])


def level_start():
    # g_p_.mostfun.send_command(["G35"])
    g_p_.mostfun.auto_leveling()
    Btn_check_start.text = UIconfig["button"]["finish"]
    Btn_check_start.handle = level_fihish
    Btn_check_start.disable()
    Btn_adjusting.disable()

def level_fihish():
    g_p_.mostfun.send_command(["G28"])
    jump2page(p_home)
    Btn_check_start.text = UIconfig["button"]["start"]
    Btn_check_start.handle = level_start
    Btn_adjusting.disable()

def level_hand_check_apply():
    g_p_.mostfun.send_command(["G35"])
    level_fihish()
    waiting(UIconfig["mesg"]["wait"])
    sleep(3)
    jump2page(p_home)
    #level_done()

def level_hand_check_cancel():
    # g_p_.mostfun.send_command(["G28"])
    # jump2page(p_home)
    level_fihish()

def level_done():
    g_p_.mostfun.reset()
    jump2page(p_home)


def waiting(text):
    # print "wait"
    p_waiting.shows[0].textstr = text
    jump2page(p_waiting)


def warning(text):
    p_warning.shows[0].textstr = text
    jump2page(p_warning)

def error(text):
    p_error.shows[0].textstr = text
    jump2page(p_error)

def comfirming(text):
    comfirm_msg.set_text(text)
    jump2page(p_confirm)


def check_interrupt():
    interrupted_file = os.listdir(PATH_INTERRUPTED)
    if len(interrupted_file) == 0:
        return False
    file_name_rolling.set_text(interrupted_file[0])
    global Current_gcode_PATH
    Current_gcode_PATH = PATH_INTERRUPTED + interrupted_file[0]
    tmp_files = os.listdir(PATH_TMP)
    for f in tmp_files:
        os.remove(PATH_TMP + f)
    return True


def save_interrupt():
    waiting(UIconfig["mesg"]["wait"])
    files = os.listdir(PATH_INTERRUPTED)
    for f in files:
        shutil.move(PATH_INTERRUPTED + f, PATH_PAUSED)
    jump2page(p_main_menu)


def skip_interrupt():
    waiting(UIconfig["mesg"]["wait"])
    files = os.listdir(PATH_INTERRUPTED)
    for f in files:
        os.remove(PATH_INTERRUPTED + f)
    jump2page(p_main_menu)


def continue_interrupt():
    global Current_gcode_PATH
    files = os.listdir(PATH_INTERRUPTED)
    for f in files:
        shutil.move(PATH_INTERRUPTED + f, PATH_TMP)
    Current_gcode_PATH = PATH_TMP + files[0]
    begin_printing()


def back2printing():
    p_heating.disable_jump()
    jump2page(p_home)


def check_SD():
    # global SDcard
    # global USBstorage
    # p = subprocess.Popen(cmd_check_card_reader_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p.wait()
    # res = p.stdout.readlines()
    # sdPin_state = sdPin.read()

    # if sdPin_state == 0:  # sdcard insert
    #     sleep(2)
    #     sd = res[0][0:-1]
    #     p = subprocess.Popen("ls /dev/" + sd + "[0-9]", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #     p.wait()
    #     sd = p.stdout.readlines()[0][0:-1]
    #     if SDcard == False:
    #         # mount
    #         cmd = "mount " + sd + ' ' + r"/media/sdcard"
    #         # print cmd
    #         logger.info(cmd)
    #         subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #         SDcard = True
    # elif sdPin_state == 1:  # sdcard remove
    #     if SDcard == True:
    #         # umount
    #         print "umount"
    #         logger.info("umount /media/sdcard")
    #         subprocess.Popen("umount /media/sdcard", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #         SDcard = False

    # p = subprocess.Popen(cmd_check_USBstorage_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p.wait()
    # res = p.stdout.readlines()
    # # print res
    # if len(res) > 0:
    #     if len(res[0]) > 4:  # no USB storage
    #         if USBstorage == True:
    #             logger.info("umount /media/usb")
    #             subprocess.Popen("umount /media/usb", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #             USBstorage = False
    #     else:
    #         if USBstorage == False:
    #             usb = res[0][0:-1]
    #             p = subprocess.Popen("ls /dev/" + usb + "[0-9]", shell=True, stdout=subprocess.PIPE,
    #                                  stderr=subprocess.STDOUT)
    #             p.wait()
    #             usb = p.stdout.readlines()[0][0:-1]
    #             cmd = "mount " + usb + ' ' + r"/media/usb"
    #             print cmd
    #             # mount
    #             logger.info(cmd)
    #             subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #             USBstorage = True

    SDcard = os.path.exists(PATH_SDCARD)
    USBstorage = os.path.exists(PATH_USB)
    usb_files.refresh()
    sdcard_files.refresh()

    if SDcard == False and USBstorage == False:
        main_menu.disable_item(-1)
        p_files_menu.page_disable()
    else:
        main_menu.enable_item(-1)
        p_files_menu.page_enable()

    if SDcard == False:
        menu_files.disable_item(0)
        p_files_sdcard.page_disable()
    else:
        menu_files.enable_item(0)
        p_files_sdcard.page_enable()
    if USBstorage == False:
        menu_files.disable_item(-1)
        p_files_usb.page_disable()
    else:
        menu_files.enable_item(-1)
        p_files_usb.page_enable()


def create_QR(text, file_name):
    import qrcode

    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=1
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(file_name)


def check_wifi(ifname, item_num):
    # print "checking wifi"
    if ifname == "wlan0":
        global currentIP
        file_path = IMG_PATH_QRwlan0
        p = subprocess.Popen("ifconfig wlan0 | grep addr: | cut -d : -f 2 | cut -d ' ' -f 1", shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        res = p.stdout.readlines()[0][0:-1]

        if currentIP == '':
            currentIP = res
        elif currentIP == res:
            return

        if len(res) > 7:
            STA_IP.set_text("http://" + res)
            create_QR("http://" + res, file_path)
            p = subprocess.Popen('iwconfig wlan0 | grep ESSID: | cut -d \\" -f 2', shell=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            res = p.stdout.readlines()[0]
            if res[-1] == '\n' or res[-1] == '\r':
                res = res[0:-1]

            STA_SSID.set_text("SSID:" + res)
            menu_connection.enable_item(item_num)
            Img_QR_STA = image(47, 0, [IMG_PATH_QRwlan0])
            p_QR_STA.add_show(Img_QR_STA)
        else:
            logger.error("get wlan0 ERROR")
            menu_connection.disable_item(item_num)

    elif ifname == "ra0":
        p = subprocess.Popen("cat /sys/class/net/ra0/operstate", shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        res = p.stdout.readlines()[0]

        if "up" in res or "unknown" in res:
            p = subprocess.Popen('cat /etc/Wireless/RT2870AP/RT2870AP.dat | grep ^SSID= | cut -d = -f 2', shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            res = p.stdout.readlines()[0][0:-1]
            AP_SSID.set_text("SSID:" + res)
            menu_connection.enable_item(item_num)
        else:
            logger.error("get wlan0 ERROR")
            menu_connection.disable_item(item_num)


def power_down():
    if g_p_.mostfun.state == "printing" or g_p_.mostfun.state == "pause":
        logger.warning("power down,save running task")
        jump2page(p_power_down)
        save_printing(True)
    else:
        logger.warning("power down")
        jump2page(p_bye)
        # os.system('halt')


def LCDsleep():
    global screen
    global Lcd_sleep
    Lcd_sleep = True
    sleep(0.05)
    screen.save(PATH_FRAME_BUFFER)
    sleep(0.02)
    os.kill(TFT_PID, 2)
    # sleep(0.05)


def bibi(sustain, times):
    p = subprocess.Popen(["/mostfun/buzzer", str(sustain), str(times)], \
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, \
                         stderr=subprocess.PIPE, shell=False)


Black_light.dir(mraa.DIR_OUT)
sdPin.dir(mraa.DIR_IN)
black_light("on")
# UI start

with open("/var/run/TFT_8340.pid","r") as TFT:
    TFT_PID = int(TFT.read())
print "TFT PID:"
print TFT_PID

p_logo = page(PATH_LOGO, enablehoming=False)
p_continue = page(PATH_BLACK, enablehoming=False)
p_connection_menu = page(PATH_BLACK)
p_QR_AP = page(PATH_QR_AP)
p_QR_STA = page(PATH_QR_STA)

p_main_menu = page(PATH_BLACK)
p_files_menu = page(PATH_BLACK)
p_files_local = page(PATH_BLACK)
p_files_sdcard = page(PATH_BLACK)
p_files_usb = page(PATH_BLACK)
p_files_paused = page(PATH_BLACK)

p_setting_menu = page(PATH_BLACK)
p_auto_leveling = page(PATH_LEVELING, enablehoming=True)
p_leveling_set = page(PATH_ADJUSTING, enablehoming=False)
p_refill = page(PATH_REFILLTEST, ("ready", "printing", "pause"), enablehoming=False)
p_pullout = page(PATH_EXTRUD, ("ready", "printing", "pause"), enablehoming=False)
p_feedin = page(PATH_EXTRUD, ("ready", "printing", "pause"), enablehoming=False)
p_test = page(PATH_TEST, ("ready", "printing", "pause"), enablehoming=False)

p_heating = page(PATH_HEATING, ("printing", "pause"), enablehoming=False)
p_printing = page(PATH_BLACK, ("printing", "pause"))
p_printing_ctl_menu = page(PATH_BLACK, ("printing", "pause"))
p_cancel_printing = page(PATH_ATTENTION, ("printing", "pause"))
p_save_printing = page(PATH_ATTENTION, ("printing", "pause"))
p_pause_printing = page(PATH_ATTENTION, ("printing", "pause"))
p_resume_printing = page(PATH_ATTENTION, ("printing", "pause"))

p_power_down = page(PATH_POEWRDOWN, ("ready", "printing", "pause"))
p_bye = page(PATH_BLACK, ("ready", "printing", "pause"))

p_confirm = page(PATH_BLACK,enablehoming=False)
p_waiting = page(PATH_BLACK, ("ready", "printing", "pause"),enablehoming=False)
p_warning = page(PATH_WARNING, ("ready", "printing", "pause"),enablehoming=False)
p_error = page(PATH_ERROR, ("ready", "printing", "pause"),enablehoming=False)
p_upgrading = page(PATH_UPGRADE, ("ready", "printing", "pause"),enablehoming=False)

p_home = p_main_menu

m_encoder = encoder()
p_env = static_p()

UI_printing = [p_printing, p_printing_ctl_menu, p_cancel_printing, p_save_printing, p_pause_printing, p_resume_printing]

# begin build pages

please_waiting = textbox("center", UIconfig["mesg"]["wait"], "middle", font_cn18)
p_waiting.add_show(please_waiting)

warning_info = textbox([5, 72, 215, 175], "", "middle", font_cn18)
p_warning.add_show(warning_info)

error_info = textbox([5,120,215,170], "ERROR", "middle", font_cn18)
p_error.add_show(error_info)

upgrading_info = textbox([5,120,215,170], "geting upgrade...", "middle", font_cn18)
p_upgrading.add_show(upgrading_info)

Btn_contimue_interrupt_YES = button((150, 125), (36, 60), UIconfig["button"]["YES"], continue_interrupt)
Btn_contimue_interrupt_YES.set_warning()
Btn_contimue_interrupt_save = button((80, 125), (36, 60), UIconfig["button"]["save"], save_interrupt)
Btn_contimue_interrupt_skip = button((10, 125), (36, 60), UIconfig["button"]["skip"], skip_interrupt)
p_continue.add_ele(Btn_contimue_interrupt_skip)
p_continue.add_ele(Btn_contimue_interrupt_save)
p_continue.add_ele(Btn_contimue_interrupt_YES)
file_name_rolling = rolling_text(2, Current_gcode_PATH, font_mdcn30_ZH, 'l')
p_continue.add_show(file_name_rolling)
continue_msg = textbox((10, 36, 210, 68), UIconfig["mesg"]["continue"], "middle", font_cn20)
p_continue.add_show(continue_msg)
time_msg = textbox((10, 68, 200, 96), UIconfig["mesg"]["autostart"], "middle", font_cn18)
p_continue.add_show(time_msg)
clock = timer_show((98, 102), 30)
p_continue.add_show(clock)
p_continue.set_timeout(30, continue_interrupt)

local_files = file_list("files", PATH_LOCAL)
local_files_msg = textbox((5, 5, 210, 24), UIconfig["mesg"]["localfiles"], "left", font_cn20)
p_files_local.add_ele(local_files)
p_files_local.add_show(local_files_msg)

sdcard_files = file_list("files", PATH_SDCARD)
sdcard_files_msg = textbox((5, 5, 210, 24), UIconfig["mesg"]["sdfiles"], "left", font_cn20)
p_files_sdcard.add_ele(sdcard_files)
p_files_sdcard.add_show(sdcard_files_msg)

usb_files = file_list("files", PATH_USB)
usb_files_msg = textbox((5, 5, 210, 24), UIconfig["mesg"]["usbfiles"], "left", font_cn20)
p_files_usb.add_ele(usb_files)
p_files_usb.add_show(usb_files_msg)

paused_files = file_list("files", PATH_PAUSED)
paused_files_msg = textbox((5, 5, 210, 24), UIconfig["mesg"]["pausedfiles"], "left", font_cn20)
p_files_paused.add_ele(paused_files)
p_files_paused.add_show(paused_files_msg)

main_menu = menu("mainmenu", [p_connection_menu, p_files_local, p_setting_menu, p_files_paused, p_files_menu])
p_main_menu.add_ele(main_menu)

menu_files = menu("filesmenu", [p_files_sdcard, p_files_usb])
p_files_menu.add_ele(menu_files)

menu_printing_ctl = menu("pctlmenu",
                         [p_pause_printing, p_resume_printing, p_heating, p_save_printing, p_cancel_printing, p_refill])
p_printing_ctl_menu.add_ele(menu_printing_ctl)
p_printing_ctl_menu.set_timeout(15, jump2page, p_home)

menu_connection = menu("wifimenu", [p_QR_AP, p_QR_STA])
p_connection_menu.add_ele(menu_connection)

menu_setting = menu("settingmenu", [p_refill, p_auto_leveling])
p_setting_menu.add_ele(menu_setting)

Img_leveling = image(0, 0, [IMG_LEVELING0, IMG_LEVELING1, IMG_LEVELING2, IMG_LEVELING3, IMG_LEVELING4, IMG_LEVELING5,
                            IMG_LEVELING6, IMG_LEVELING7, IMG_LEVELING8, IMG_LEVELING9, IMG_LEVELING10, IMG_LEVELING9,
                            IMG_LEVELING8, IMG_LEVELING7,
                            IMG_LEVELING6, IMG_LEVELING5], 0)
p_auto_leveling.add_show(Img_leveling)
Btn_check_start = button((139, 30), (36, 78), UIconfig["button"]["start"], level_start)
Btn_check_start.set_warning()
Btn_adjusting = button((139, 130), (36, 78), UIconfig["button"]["adjust"], jump2page, p_leveling_set)
Btn_adjusting.disable()

# p_auto_leveling.add_ele(Btn_check_done)
p_auto_leveling.add_ele(Btn_adjusting)
p_auto_leveling.add_ele(Btn_check_start)

mesg_leveling = textbox((10, 125, 140, 170), UIconfig["mesg"]["leveling"], "middle", font_bdcn20)
p_auto_leveling.add_show(mesg_leveling)

Btn_up = button_img((137, 50), [BTN_PATH_UP0, BTN_PATH_UP1, BTN_PATH_UP0], Z_up)
Btn_down = button_img((137, 90), [BTN_PATH_DOWN0, BTN_PATH_DOWN1, BTN_PATH_DOWN0], Z_down)
Btn_handcheck_apply = button((131, 130), (36, 78), UIconfig["button"]["apply"], level_hand_check_apply)
Btn_handcheck_cancel = button((15, 130), (36, 80), UIconfig["button"]["cancel"], level_hand_check_cancel)
Btn_handcheck_apply.set_warning()
p_leveling_set.add_ele(Btn_down)
p_leveling_set.add_ele(Btn_handcheck_cancel)
p_leveling_set.add_ele(Btn_handcheck_apply)
p_leveling_set.add_ele(Btn_up)

img_bord = shap_line([15,113,132,113],color=COLOR_WHIT,width=3)
img_bord.set_range([-1,1,-20,10])

p_leveling_set.add_show(img_bord)

Btn_heating_back = button((127, 125), (36, 80), UIconfig["button"]["back"], back2printing)
# Btn_heating_back.set_warning()
p_heating.add_ele(Btn_heating_back)
tmper_E_msg = textbox((100, 40, 210, 60), UIconfig["mesg"]["extruder"], "left", font_cn20)
tmper_E_T = textbox((100, 60, 210, 80), u"0/0°C", "left", font_cn20)
tmper_B_msg = textbox((100, 83, 210, 103), UIconfig["mesg"]["bed"], "left", font_cn20)
tmper_B_T = textbox((100, 103, 210, 123), u"0/0°C", "left", font_cn20)
p_heating.add_show(tmper_E_msg)
p_heating.add_show(tmper_E_T)
p_heating.add_show(tmper_B_msg)
p_heating.add_show(tmper_B_T)
Img_heating = image(0, 0, [IMG_HEATING1, IMG_HEATING2])
p_heating.add_show(Img_heating)

printer_state = printing("printer", g_p_.mostfun)
p_printing.add_ele(printer_state)
print_name_rolling = rolling_text(0, Current_gcode_PATH, font_mdcn30_ZH, 'l')
p_printing.add_show(print_name_rolling)

Btn_cancel_print_NO = button((20, 125), (36, 64), UIconfig["button"]["NO"], jumpback)
Btn_cancel_print_YES = button((135, 125), (36, 64), UIconfig["button"]["YES"], cancel_printing)
Btn_cancel_print_YES.set_warning()
p_cancel_printing.add_ele(Btn_cancel_print_YES)
p_cancel_printing.add_ele(Btn_cancel_print_NO)
cancel_msg = textbox("center", UIconfig["mesg"]["cancel"], "middle", font_cn18)
p_cancel_printing.add_show(cancel_msg)

Btn_pause_print_NO = button((20, 125), (36, 64), UIconfig["button"]["NO"], jumpback)
Btn_pause_print_YES = button((135, 125), (36, 64), UIconfig["button"]["YES"], pause_printing)
Btn_pause_print_YES.set_warning()
p_pause_printing.add_ele(Btn_pause_print_NO)
p_pause_printing.add_ele(Btn_pause_print_YES)
pause_msg = textbox("center", UIconfig["mesg"]["pause"], "middle", font_cn18)
p_pause_printing.add_show(pause_msg)

Btn_resume_print_NO = button((20, 125), (36, 64), UIconfig["button"]["NO"], jumpback)
Btn_resume_print_YES = button((135, 125), (36, 64), UIconfig["button"]["YES"], resume_printing)
Btn_resume_print_YES.set_warning()
p_resume_printing.add_ele(Btn_resume_print_NO)
p_resume_printing.add_ele(Btn_resume_print_YES)
resume_msg = textbox("center", UIconfig["mesg"]["resume"], "middle", font_cn18)
p_resume_printing.add_show(resume_msg)

Btn_save_print_NO = button((20, 125), (36, 64), UIconfig["button"]["NO"], jumpback)
Btn_save_print_YES = button((120, 125), (36, 64), UIconfig["button"]["YES"], save_printing)
Btn_save_print_YES.set_warning()
p_save_printing.add_ele(Btn_save_print_NO)
p_save_printing.add_ele(Btn_save_print_YES)
save_msg = textbox("center", UIconfig["mesg"]["stop"], "middle", font_cn18)
p_save_printing.add_show(save_msg)

Btn_refill_quit = button((20, 125), (36, 64), UIconfig["button"]["quit"], jump2page, p_main_menu)
Btn_refill_next = button((135, 125), (36, 64), UIconfig["button"]["next"], jump2page, p_pullout)
Btn_refill_next.set_warning()
Btn_refill_next.disable()
p_refill.add_ele(Btn_refill_quit)
p_refill.add_ele(Btn_refill_next)
refill_msg = textbox((125, 45, 215, 100), UIconfig["mesg"]["heating"], font_cn16)
p_refill.add_show(refill_msg)
# temp_msg = textbox((10,90,210,115),"",font_cn18)
# p_refill.add_show(temp_msg)
temp_bar = process_bar((110, 97), (110, 32), COLOR_RED)
p_refill.add_show(temp_bar)

Btn_pullout_next = button((135, 125), (36, 64), UIconfig["button"]["next"], jump2page, p_feedin)
Btn_pullout_next.set_warning()
p_pullout.add_ele(Btn_pullout_next)
Img_pullout = image(0, 0, [IMG_PATH_PULLOUT, IMG_PATH_PULLOUT1, IMG_PATH_PULLOUT2])
p_pullout.add_show(Img_pullout)
pullout_msg = textbox((133, 30, 210, 120), UIconfig["mesg"]["pullout"], "middle", font_cn16)
p_pullout.add_show(pullout_msg)

Btn_feedin_next = button((135, 125), (36, 64), UIconfig["button"]["next"], jump2page, p_test)
Btn_feedin_next.set_warning()
p_feedin.add_ele(Btn_feedin_next)
Img_feedin = image(0, 0, [IMG_PATH_FEEDIN, IMG_PATH_FEEDIN1, IMG_PATH_FEEDIN2])
p_feedin.add_show(Img_feedin)
feedin_msg = textbox((130, 30, 210, 120), UIconfig["mesg"]["feedin"], "middle", font_cn16)
p_feedin.add_show(feedin_msg)

Btn_refill_finish = button((130, 125), (36, 74), UIconfig["button"]["finish"], jump2page, p_home)
Btn_extrud_test = button((20, 125), (36, 64), UIconfig["button"]["test"], extrud)
Btn_extrud_test.set_warning()
p_test.add_ele(Btn_refill_finish)
p_test.add_ele(Btn_extrud_test)
test_msg = textbox((125, 35, 210, 120), UIconfig["mesg"]["test"], font_cn16)
p_test.add_show(test_msg)
Img_ex_test = image(0, 0, [IMG_PATH_EX1, IMG_PATH_EX2, IMG_PATH_EX3, IMG_PATH_EX4], 0)
p_test.add_show(Img_ex_test)

Btn_confirm_YES = button((135, 125), (36, 64), UIconfig["button"]["print"], begin_printing)
Btn_confirm_YES.set_warning()
Btn_confirm_NO = button((15, 125), (36, 80), UIconfig["button"]["cancel"], jumpback)
comfirm_msg = textbox((10, 10, 210, 120), "", "middle", font_mdcn24_ZH)
p_confirm.add_show(comfirm_msg)
p_confirm.add_ele(Btn_confirm_NO)
p_confirm.add_ele(Btn_confirm_YES)

# check_wifi("wlan0",1)
# check_wifi("wlan1",0)
Img_QR_AP = image(47, 0, [IMG_PATH_QRwlan1])
p_QR_AP.add_show(Img_QR_AP)
AP_SSID = textbox((0, 126, 219, 150), UIconfig["mesg"]["noconnect"], "middle", font_cn16_ZH)
AP_IP = textbox((0, 150, 219, 175), "http://192.168.42.1", "middle", font_cn16_ZH)
p_QR_AP.add_show(AP_SSID)
p_QR_AP.add_show(AP_IP)
p_QR_AP.add_ele(p_env)

Img_QR_STA = image(47, 0, [IMG_PATH_QRwlan0])
p_QR_STA.add_show(Img_QR_STA)
STA_SSID = textbox((0, 126, 219, 150), UIconfig["mesg"]["noconnect"], "middle", font_cn16_ZH)
STA_IP = textbox((0, 150, 219, 175), "http://", "middle", font_cn16_ZH)
p_QR_STA.add_show(STA_IP)
p_QR_STA.add_show(STA_SSID)
p_QR_STA.add_ele(p_env)

power_down_msg = textbox((0, 120, 219, 150), UIconfig["mesg"]["save"], "middle", font_cn20)
p_power_down.add_show(power_down_msg)

bye_msg = textbox("center", UIconfig["mesg"]["bye"], "middle", font_mdcn24)
p_bye.add_show(bye_msg)


def m_UI():
    global Lcd_sleep
    global Current_page

    bibi(100, 2)

    Interrupted = check_interrupt()
    if Interrupted:
        jump2page(p_continue)
    else:
        jump2page(p_main_menu)
    Current_page.flush_page()

    while True:
        # begin = time()
        if Lcd_sleep == False:
            if not g_p_.mostfun.get_state() in Current_page.owner:
                # if Current_page == p_printing:
                #     p_printing.dirty = True
                # sleep(0.02)
                state = g_p_.mostfun.get_state()
                if state == "printing" or state == "pause":
                    p_home = p_printing
                elif state == "error":
                    p_home = p_error
                elif state == "updating":
                    p_home = p_upgrading

                else:
                    p_home = p_main_menu

                jump2page(p_home)

            # if Current_page == p_refill:
            #     # print g_p_.mostfun._extruderTemp/200.0
            #     temp_bar.set_persent(g_p_.mostfun.get_extruderTemp() / 200.0)
            #     if g_p_.mostfun.get_extruderTemp() < 175:
            #         Btn_refill_next.disable()
            #     else:
            #         Btn_refill_next.enable()
            # elif Current_page == p_heating:
            #     tmper_E_T.set_text(
            #             str(g_p_.mostfun.get_extruderTemp()) + '/' + str(g_p_.mostfun.get_extruderTargetTemp()) + u'°C')
            #     tmper_B_T.set_text(
            #         str(g_p_.mostfun.get_bedTemp()) + '/' + str(g_p_.mostfun.get_bedTargetTemp()) + u'°C')
            #     if g_p_.mostfun.is_hot() == True:
            #         p_home = p_printing
            #         jump2page(p_home)

            # elif Current_page == p_printing:
            #     if g_p_.mostfun.is_hot() == False:
            #         p_home = p_heating
            #         jump2page(p_home)

            Current_page.flush_page()
            sleep(0.02)
            os.kill(TFT_PID, 2)
            sleep(0.02)
            # end = time()
            # print 1.0/(end-begin)
        else:
            sleep(0.1)


def input_env():
    global Current_page
    global Lcd_sleep

    while True:
        m_encoder.refresh_state()

        bibi(1, 1)
        # global number
        # Current_page.backgrand.save("/home/"+str(number)+".jpg")
        # number+=1

        if m_encoder.state == '!':
            pass
            # print "power down"
            # Lcd_sleep = False
            # power_down()
            # break

        elif m_encoder.state == 's':
            print "sleep"
            LCDsleep()
            
        elif m_encoder.state == 'w':
            print "weak up"
            Lcd_sleep = False

        else:
            print m_encoder.state
            Current_page.click(m_encoder.state)

        m_encoder.state = 'n'
        sleep(0.05)


def globe_env():
    global Current_page

    while True:
        if Lcd_sleep == False:
            printer_mesgs = g_p_.mostfun.UI_box_getter()
            if len(printer_mesgs)>0:
                print "printer mesgs",printer_mesgs
            for mesg in printer_mesgs:
                if mesg.startswith("leveling"):
                    if "1" in mesg:
                        # Btn_check_start.disable()
                        # Btn_adjusting.disable()
                        Img_leveling.play(-1)

                    elif "0" in mesg:
                        Btn_check_start.enable()
                        Btn_adjusting.enable()
                        Img_leveling.play(0)

            if Current_page == p_main_menu or Current_page == p_files_menu or Current_page == p_files_usb or Current_page == p_files_sdcard:
                check_SD()

            if Current_page == p_connection_menu:
                check_wifi("wlan0", 1)
                check_wifi("ra0", 0)

            # elif Current_page == p_continue:
            #     file_name_rolling.set_text(Current_gcode_PATH.split(r'/')[-1])

            # elif Current_page == p_main_menu or Current_page == p_files_menu:

            elif Current_page == p_refill:
                temp_bar.set_persent(g_p_.mostfun.get_extruderTemp() / 230.0)
                if g_p_.mostfun.get_extruderTemp() < 180:
                    Btn_refill_next.disable()
                else:
                    Btn_refill_next.enable()
            elif Current_page == p_heating:
                # else:
                tmper_E_T.set_text(
                    str(g_p_.mostfun.get_extruderTemp()) + '/' + str(g_p_.mostfun.get_extruderTargetTemp()) + u'°C')
                tmper_B_T.set_text(
                    str(g_p_.mostfun.get_bedTemp()) + '/' + str(g_p_.mostfun.get_bedTargetTemp()) + u'°C')
                if p_heating.enable_autojump:
                    if g_p_.mostfun.is_hot() == True:
                        # p_home = p_printing
                        back2printing()

            elif Current_page == p_printing:
                # if g_p_.mostfun.is_hot() == False:
                #     # print "heating"
                #     p_home = p_heating
                #     jump2page(p_heating)
                # else:
                #     printer_state.refresh_printer_state()
                printer_state.refresh_printer_state()

            # elif Current_page == p_auto_leveling:
            #     if g_p_.mostfun.is_leveling_done() == -1:
            #         Img_leveling.play(0)
            #         Btn_check_start.enable()
            #         Btn_check_start.text = UIconfig["button"]["start"]
            #         Btn_check_start.handle = level_start
            #         # Btn_check_done.disable()
            #         Btn_adjusting.disable()
            #     elif g_p_.mostfun.is_leveling_done() == 0:
            #         Img_leveling.play(-1)
            #         Btn_check_start.disable()
            #         # Btn_check_done.disable()
            #         Btn_adjusting.disable()
            #         Btn_check_start.text = UIconfig["button"]["finish"]
            #         Btn_check_start.handle = level_fihish
            #     elif g_p_.mostfun.is_leveling_done() == 1:
            #         Img_leveling.play(0)
            #         # Btn_check_done.enable()
            #         Btn_adjusting.enable()
            #         Btn_check_start.enable()

            sleep(0.2)
        else:
            sleep(0.2)


def UI_monitor():
    # thread.start_new_thread(m_UI, ())
    # sleep(0.5)
    # thread.start_new_thread(input_env, ())
    # sleep(0.5)
    # thread.start_new_thread(globe_env, ())

    thread_UI = threading.Thread(target=m_UI)
    thread_UI.daemon = True
    thread_UI.start()
    sleep(0.1)

    thread_input_env = threading.Thread(target=input_env)
    thread_input_env.daemon = True
    thread_input_env.start()
    sleep(0.1)

    thread_globe_env = threading.Thread(target=globe_env)
    thread_globe_env.daemon = True
    thread_globe_env.start()
