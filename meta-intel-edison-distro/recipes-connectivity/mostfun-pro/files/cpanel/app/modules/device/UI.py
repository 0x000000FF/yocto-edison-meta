# -*- coding:utf-8 -*-
from __future__ import division
from app import PATH_
import os
import Image
import ImageChops
import ImageFont
import ImageDraw
import thread
import time
import subprocess
import mraa
import shutil
	
ENCODER_PATH = '''/dev/ttymcu0'''
FONT_CN   = '''/mostfun/panel/font/HelveticaNeueLTPro-Cn.otf'''
FONT_BDCN = '''/mostfun/panel/font/HelveticaNeueLTPro-BdCn.otf'''
FONT_MDCN = '''/mostfun/panel/font/HelveticaNeueLTPro-MdCn.otf'''
#//font_CN
#FONT_MDCN = '''/mostfun/panel/font/SourceHanSansCN-Medium.otf''' 

PATH_LOCAL 	= '''/home/mostfuncp/gcode/'''
PATH_SDCARD = '''/media/sdcard'''
PATH_PAUSED = '''/home/mostfuncp/paused/'''
PATH_INTERRUPTED = '''/home/mostfuncp/interrupted/'''
PATH_TMP		= '''/home/mostfuncp/tmp/'''

#imgs
ICON_PATH_PRINT = '''/mostfun/panel/bg/start.bmp'''
ICON_PATH_STOP 	= '''/mostfun/panel/bg/stop.bmp'''
ICON_PATH_PAUSE = '''/mostfun/panel/bg/pause.bmp'''
IMG_PATH_FEEDIN = '''/mostfun/panel/bg/feedin.bmp'''
IMG_PATH_PULLOUT = '''/mostfun/panel/bg/pullout.bmp'''
IMG_PATH_FEEDIN1 = '''/mostfun/panel/bg/feedin1.bmp'''
IMG_PATH_PULLOUT1 = '''/mostfun/panel/bg/pullout1.bmp'''
IMG_PATH_FEEDIN2 = '''/mostfun/panel/bg/feedin2.bmp''' 
IMG_PATH_PULLOUT2 = '''/mostfun/panel/bg/pullout2.bmp'''
IMG_PATH_QR		= '''/home/QR.bmp'''
IMG_PATH_EX1	= '''/mostfun/panel/bg/ex1.bmp'''
IMG_PATH_EX2	= '''/mostfun/panel/bg/ex2.bmp'''
IMG_PATH_EX3	= '''/mostfun/panel/bg/ex3.bmp'''
IMG_PATH_EX4	= '''/mostfun/panel/bg/ex4.bmp'''

#backgrands
PATH_QR_AP 			= '''/mostfun/panel/bg/QR_AP.bmp'''
PATH_QR_STA 		= '''/mostfun/panel/bg/QR_STA.bmp'''
PATH_LOGO 			= '''/mostfun/panel/bg/logo.bmp'''
PATH_BLACK 			= '''/mostfun/panel/bg/back.bmp'''
PATH_LOCALFILES 	= '''/mostfun/panel/bg/localfiles.bmp'''
PATH_SDCARDFILES	= '''/mostfun/panel/bg/sdcardfiles.bmp'''
PATH_PAUSEDFILES 	= '''/mostfun/panel/bg/pausedfiles.bmp'''
PATH_ATTENTION		= '''/mostfun/panel/bg/attention.bmp'''
PATH_EXTRUD			= '''/mostfun/panel/bg/extrud.bmp'''
PATH_TEST			= '''/mostfun/panel/bg/test.bmp'''
PATH_POEWRDOWN 		= '''/mostfun/panel/bg/powerdown.bmp'''
PATH_BYE 			= '''/mostfun/panel/bg/bye.bmp'''
PATH_REFILLTEST		= '''/mostfun/panel/bg/refilltest.bmp'''

PATH_FRAME_BUFFER = '''/tmp/page.bmp'''

COLOR_WHIT 			= 0xFFFFFF
COLOR_BLACK 		= 0x00
COLOR_DARK_GRAY 	= 0x666666
COLOR_LIGHT_GRAY 	= 0xAAAAAA
COLOR_RED		 	= 0x0000FF
COLOR_BLUE		 	= 0xFF0000
COLOR_GREEN		 	= 0x00FF00

BUTTON_H = 34
BUTTON_W = 64

TEXT_LIST_W = 160
TEXT_LIST_TEXT_W = 136

LCD_SLEEP_TIMEOUT = 60
Page_timer = 0

Current_gcode = ""
Current_page = None
Local_files = []
SDcard_files =[]
font_cn16 = ImageFont.truetype(FONT_CN,16)
font_cn18 = ImageFont.truetype(FONT_CN,18)
font_cn20 = ImageFont.truetype(FONT_CN,20)
font_bdcn20 = ImageFont.truetype(FONT_BDCN,20)
font_bdcn30 = ImageFont.truetype(FONT_BDCN,30)
font_mdcn24 = ImageFont.truetype(FONT_MDCN,24)
font_mdcn30 = ImageFont.truetype(FONT_MDCN,30)
font_mdcn50 = ImageFont.truetype(FONT_MDCN,50)

Black_light = bl = mraa.Gpio(21)
Lcd_sleep = False
Lcd_wake_time = 0

class button(object):
	def __init__(self,X,Y,h,w,text,handle,args=None):
		self.X = X
		self.Y = Y
		self.h = h
		self.w = w
		self.text = text
		self.selected = 0
		self.container = None
		self.backgrand = None
		self.handle = handle
		self.args = args
		self.isenable = True
		self.warning = False

	def set_warning(self,warning = True):
		self.warning = warning

	def click(self):
		if self.isenable:
			if self.args == None:
				self.handle()
			else:
				self.handle(self.args)
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

	def draw(self):
		textsize = self.container.textsize(self.text,font_bdcn30)
		textlocation = ((self.w-textsize[0])/2+self.X,(self.h-textsize[1])/2+self.Y+8)
		if self.isenable:
			if self.selected == 0:
				self.container.rectangle((self.X,self.Y,self.X+self.w,self.Y+self.h),COLOR_BLACK)
				self.container.text(textlocation,self.text,COLOR_WHIT,font_bdcn30)
			if self.selected == 1:
				if self.warning:
					self.container.rectangle((self.X,self.Y,self.X+self.w,self.Y+self.h),COLOR_RED)
					self.container.text(textlocation,self.text,COLOR_WHIT,font_bdcn30)
				else:
					self.container.rectangle((self.X,self.Y,self.X+self.w,self.Y+self.h),COLOR_WHIT)
					self.container.text(textlocation,self.text,COLOR_BLACK,font_bdcn30)
		else:
			if self.selected == 1:
				self.container.rectangle((self.X,self.Y,self.X+self.w,self.Y+self.h),COLOR_LIGHT_GRAY)
				self.container.text(textlocation,self.text,COLOR_DARK_GRAY,font_bdcn30)
			if self.selected == 0:
				self.container.rectangle((self.X,self.Y,self.X+self.w,self.Y+self.h),COLOR_BLACK)
				self.container.text(textlocation,self.text,COLOR_DARK_GRAY,font_bdcn30)

class menu(object):
	def __init__(self,name, items):
		self.name = name
		self.items = items
		self.current_item = items[0]
		self.container = None
		self.backgrand = None
		self.selected = 0

	def click(self):
		jump2page(self.current_item[1])

	def left_click(self):
		while True:
			self.current_item = self.items[self.items.index(self.current_item)-1]
			if self.current_item[2] == 1:
				break
		
	def right_click(self):
		while True:
			if self.current_item == self.items[-1]:
				self.current_item = self.items[0]
			else:
				self.current_item = self.items[self.items.index(self.current_item)+1]
			if self.current_item[2] == 1:
				break

	def disable_item(self,item_num):
		self.items[item_num][2] = 0

	def enable_item(self,item_num):
		self.items[item_num][2] = 1

	# def drop_item(self,item_num):
	# 	if self.current_item == self.items[item_num]:
	# 		pass
	# 	self.items.remove(item_num)

	# def additem(self,index,item):
	# 	self.items.insert(index,item)

	def redirect_item(self,index,item):
		if self.current_item == self.items[index]:
			self.current_item = item
		self.items[index] = item

	def draw(self):
		rectangle = 20
		self.container.rectangle((0,0,219,175),COLOR_BLACK)
		for item in self.items:
			if self.current_item == item:
				self.container.rectangle((0,rectangle-4,200,rectangle+30),COLOR_WHIT)
				self.container.text((20,rectangle+2),item[0],COLOR_BLACK,font_mdcn30)
				rectangle += 27
			else:
				if item[2] == 1:
					self.container.text((20,rectangle+7),item[0],COLOR_WHIT,font_cn18)
				elif item[2] ==0:
					self.container.text((20,rectangle+7),item[0],COLOR_DARK_GRAY,font_cn18)
				rectangle += 27

class file_list(object):
	def __init__(self,name,dirpath):
		self.name = name
		self.path = dirpath
		self.files = os.listdir(dirpath)
		self.current = 0
		self.offset = 0
		self.container = None
		self.backgrand = None
		self.selected = 0
		self.rolloffset = 0
		self.counter = 0

	def click(self):
		global Current_gcode
		if not len(self.files) == 0:
			Current_gcode = self.path+self.files[self.current]
			comfirming(self.files[self.current])
		else:
			jump2page(p_main_menu)
		self.rolloffset = 0
		self.counter = 0

	def left_click(self):
		if self.current > 0:
			self.current -= 1
		elif self.current == 0:
			self.current = len(self.files)-1
		if self.current < self.offset:
			self.offset = self.current
		elif self.current > self.offset + 4:
			self.offset = self.current - 4
		self.rolloffset = 0
		self.counter = 0
		
	def right_click(self):
		if self.current < len(self.files)-1:
			self.current +=1
		elif self.current == len(self.files)-1:
			self.current = 0
		if self.current < self.offset:
			self.offset = self.current
		elif self.current > self.offset + 4:
			self.offset = self.current - 4
		self.rolloffset = 0
		self.counter = 0

	def draw(self):
		
		self.files = os.listdir(self.path)
		self.container.rectangle((0,34,190,175),COLOR_BLACK)
		if len(self.files) == 0:
			self.container.text((50,45),"Empty!",COLOR_WHIT,font_cn18)
			return
		rectangle = 34

		for item in self.files[self.offset:self.offset+5]:

			if self.current == self.files.index(item):
				#draw selected item
				self.container.rectangle((0,rectangle,TEXT_LIST_W,rectangle+28),COLOR_WHIT)
				if self.container.textsize(item,font_mdcn24)[0] <= TEXT_LIST_TEXT_W:
					#short enough,no rolling
					self.container.text((20,rectangle+3),item,COLOR_BLACK,font_mdcn24)
				else:
					#long enough,rolling
					img_w = self.container.textsize(item,font_mdcn24)[0]+TEXT_LIST_TEXT_W
					img_tmp = Image.new("RGB",(img_w,28),"white")
					draw_tmp = ImageDraw.Draw(img_tmp)
					draw_tmp.text((3,3),item,COLOR_BLACK,font_mdcn24)
					w = img_tmp.size[0]
					box = (self.rolloffset,0,self.rolloffset+TEXT_LIST_TEXT_W,28)
					disp = img_tmp.crop(box)

					self.backgrand.paste(disp,(20,rectangle,20+TEXT_LIST_TEXT_W,rectangle+28))
					# self.container.text((20-self.rolloffset,rectangle+3),item,COLOR_BLACK,font_mdcn24)

					if self.rolloffset >= img_w-TEXT_LIST_TEXT_W:
						self.rolloffset = 0
						self.counter = 0
					
					self.counter += 1
					if self.counter > 10:
						self.rolloffset += 2

				rectangle += 28

			else:
				#pass
				width = self.container.textsize(item,font_cn16)[0]
				#draw unselected item
				if width <= TEXT_LIST_TEXT_W:
					self.container.text((20,rectangle+3),item,COLOR_WHIT,font_cn16)
				else:
					self.container.text((20,rectangle+3),item[:int(len(item)*(TEXT_LIST_TEXT_W/width))-3]+u"…",COLOR_WHIT,font_cn16)
				rectangle += 24

		#draw sidebar
		if len(self.files) - 1 == 0:
			slider = 30
		else:
			slider = self.current/(len(self.files)-1)*102+30

		self.container.rectangle((160,0,219,175),COLOR_BLACK)
		self.container.line(((200,30),(200,146)),fill=COLOR_WHIT,width=2)
		self.container.line(((200,slider),(200,slider+14)),fill=COLOR_WHIT,width=8)

		
class printing(object):
	def __init__(self,name,printer):
		self.container = None 
		self.backgrand = None
		self.selected = -1
		self.current_file = ""
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
		self.icon_start = Image.open(ICON_PATH_PRINT,'r')
		self.icon_stop = Image.open(ICON_PATH_STOP,'r')
		self.icon_pause = Image.open(ICON_PATH_PAUSE,'r')
		self.printer = printer
		#self.rolloffset = 0

	def refresh_printer_state(self):
		global Current_gcode
		self.current_file = self.printer._filePath.split('/')[-1]
		Current_gcode = self.current_file
		self.time = self.printer.get_times()
		self.E_temp = self.printer._extruderTemp
		self.layer_offset = self.printer._g._layer_offset
		self.current_layer = self.printer._g._layerNum - self.layer_offset
		self.layers = self.printer._g._layerCount - self.layer_offset

		if not self.layers == 0:
			self.percent = int(((self.current_layer+1)*100) / (self.layers))

		self.B_temp = self.printer._bedTemp
		self.E_target_temp = self.printer._extruderTargetTemp
		self.B_target_temp = self.printer._bedTargetTemp
		self.state = self.printer.state

	def reset_state(self):
		self.layers = 0
		self.current_layer = 0
		self.percent = 0
		self.time = "00:00:00"

	def click(self):
		if self.state == "printing" or self.state == "pause":
			jump2page (p_printing_ctl_menu)
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
		self.refresh_printer_state()
		self.container.rectangle((0,0,219,175),COLOR_BLACK)
		# size = self.container.textsize(self.current_file.split('.')[0],font_mdcn30)
		
		# if size[0] <= 200:
		# 	self.container.text(((220-size[0])/2,10),self.current_file.split('.')[0],COLOR_WHIT,font_mdcn30)
		# else:

		# 	img_tmp = Image.new("RGB",(size[0]+210,size[1]),"black")
		# 	draw_tmp = ImageDraw.Draw(img_tmp)
		# 	draw_tmp.text((200,3),self.current_file.split('.')[0],COLOR_WHIT,font_mdcn30)
		# 	box = (self.rolloffset,0,self.rolloffset+200,size[1])
		# 	disp = img_tmp.crop(box)

		# 	self.backgrand.paste(disp,(10,10,210,size[1]+10))

		# 	if self.rolloffset >= size[0]+210:
		# 		self.rolloffset = 0

		# 	self.rolloffset += 2

		if self.state == "printing":
			self.backgrand.paste(self.icon_start,(8,115,40,147))

		elif self.state == "pause":
			self.backgrand.paste(self.icon_pause,(8,115,40,147))

		elif self.state == "finished":
			self.current_layer = self.layers
			self.percent = 100
			self.backgrand.paste(self.icon_stop,(8,115,40,147))
			

		self.container.text((10,42),"layers:"+str(self.current_layer)+'/'+str(self.layers),COLOR_WHIT,font_cn18)
		#self.container.text((10,67),"E_Temp:"+str(self.E_temp)+'/'+str(self.E_target_temp)+'C',COLOR_WHIT,font_cn18)
		#self.container.text((10,89),"B_Temp:"+str(self.B_temp)+'/'+str(self.B_target_temp)+'C',COLOR_WHIT,font_cn18)
		self.container.text((10,70),"complete:"+str(self.percent)+'%',COLOR_WHIT,font_cn18)

		#draw time
		self.container.text((210-self.container.textsize(str(self.time),font_mdcn50)[0],110),str(self.time),COLOR_WHIT,font_mdcn50)
		#draw process bar
		self.container.line(((10,155),(210,155)),fill=COLOR_WHIT,width=1)
		self.container.line(((10,166),(210,166)),fill=COLOR_WHIT,width=1)
		self.container.line(((10,155),(10,166)),fill=COLOR_WHIT,width=1)
		self.container.line(((210,155),(210,166)),fill=COLOR_WHIT,width=1)
		#draw process bar process
		if self.percent >= 1:
			self.container.line(((12,161),((12+196.0*self.percent/100.0),161)),fill=COLOR_WHIT,width=8)
		

class static_p(object):
	def __init__(self):
		self.selected = -1

	def click(self):
		jump2page (p_main_menu)

	def left_click(self):
		jump2page (p_main_menu)

	def right_click(self):
		jump2page (p_main_menu)

	def draw(self):
		pass

# class empty_p(object):
# 	def __init__(self):
# 		self.selected = -1

# 	def click(self):
# 		pass

# 	def left_click(self):
# 		pass

# 	def right_click(self):
# 		pass

# 	def draw(self):
# 		pass

class textbox(object):
	def __init__(self,position,textshow,fontb = font_mdcn24,fonts = font_cn18):
		if position == "center":
			self.X = 10
			self.Y = 36
			self.XX = 210
			self.YY = 106
		else:
			self.X = position[0]
			self.Y = position[1]
			self.XX = position[2]
			self.YY = position[3]
		self.textstr = textshow
		self.selected = -1
		self.container = None
		self.backgrand = None
		self.fontb = fontb
		self.fonts = fonts
		self.font = fontb
		self.cursor = [0,0]
		self.char_H = 0
		self.char_W = 0

	def set_text(self,text):
		self.textstr = text

	def type_a_char(self,char):
		width = self.container.textsize(char,self.font)[0]
		height = self.container.textsize(char,self.font)[1]
		if height+self.cursor[1] > self.YY-self.Y:
			return

		if width+self.cursor[0] > self.XX-self.X:
			self.cursor[0] = 0
			self.cursor[1] += height
		
		self.container.text((self.cursor[0]+self.X,self.cursor[1]+self.Y),char,COLOR_WHIT,self.font)
		self.cursor[0] += width

	def draw(self):
		size = self.container.textsize(self.textstr,self.font)
		if size[0]*size[1] > (self.XX-self.X)*(self.YY-self.Y):
			self.font = self.fonts

		self.container.rectangle((self.X,self.Y,self.XX,self.YY),COLOR_BLACK)
		if size[0] <= self.XX-self.X: 
			self.container.text((self.X+((self.XX-self.X-size[0])/2),(self.Y+(self.YY-self.Y)/2)),self.textstr,COLOR_WHIT,self.font)
		else:
			#self.cursor[1] = self.YY-self.Y-(size[1]*int(size[0]/(self.XX-self.X)))/2
			for c in self.textstr:
				self.type_a_char(c)
			self.cursor = [0,0]

class timer_show(object):
	def __init__(self,position,count,font=font_cn20): #only Y coordinate is needed
		self.position = position
		self.counter = count
		self.selected = -1
		self.container = None
		self.backgrand = None
		self.font = font

	def draw(self):
		current_T = self.counter - int(time.time()-Page_timer)
		size = self.container.textsize(str(current_T)+"s",self.font)
		self.container.rectangle((self.position[0],self.position[1],self.position[0]+size[0]+12,self.position[1]+size[1]),COLOR_BLACK)
		self.container.text(self.position,str(current_T)+"s",COLOR_WHIT,self.font)

class rolling_text(object):
	def __init__(self,position_Y,textshow,font,style = 'm'): #only Y coordinate is needed
		self.position = position_Y
		self.textstr = textshow
		self.selected = -1
		self.container = None
		self.backgrand = None
		self.font = font
		self.cursor = [0,0]
		self.width = 0#self.container.textsize(self.textstr,self.font)
		self.rolloffset = 0
		self.style = style

	def set_text(self,text):
		self.textstr = text
		self.width = self.container.textsize(self.textstr,self.font)[0]

	def draw(self):
		if self.width <= 220:
			if self.style == 'm':
				self.container.text(((220-self.width)/2,self.position),self.textstr,COLOR_WHIT,self.font)
			elif self.style == 'l':
				self.container.text((10,self.position),self.textstr,COLOR_WHIT,self.font)
			elif self.style == 'r':
				self.container.text(((220-self.width),self.position),self.textstr,COLOR_WHIT,self.font)
		else:
			#long enough,rolling
			img_size = self.container.textsize(self.textstr,self.font)
			img_tmp = Image.new("RGB",img_size,"black")
			draw_tmp = ImageDraw.Draw(img_tmp)
			draw_tmp.text((0,3),self.textstr,COLOR_WHIT,self.font)
			box = (self.rolloffset,0,self.rolloffset+220,img_size[1])
			disp = img_tmp.crop(box)

			self.backgrand.paste(disp,(0,self.position,220,self.position+img_size[1]))
			if self.rolloffset >= img_size[0]:
				self.rolloffset = 0
			
			self.rolloffset += 2


class image(object):
	def __init__(self,X,Y,imgpath,times = -1):
		self.X = X
		self.Y = Y
		self.img = list()
		for path in imgpath:
			self.img.append(Image.open(path))
		self.selected = -1
		self.container = None
		self.backgrand = None
		self.xx = self.X+self.img[0].size[0]
		self.yy = self.Y+self.img[0].size[1]
		self.frame = 0
		self.times = times

	def play(self,times):
		self.times = times*len(self.img)*5

	def draw(self):
		if self.times == 0:
			self.backgrand.paste(self.img[0],(self.X,self.Y,self.xx,self.yy))
		else:
			if self.frame == len(self.img)*5:
				self.frame = 0
			self.container.rectangle((self.X,self.Y,self.xx,self.yy),COLOR_BLACK)
			self.backgrand.paste(self.img[int(self.frame/5)],(self.X,self.Y,self.xx,self.yy))
			self.frame += 1
			if self.times > 0:
				self.times -= 1

class process_bar(object):
	def __init__(self,(X,Y),(XX,YY)):
		self.start = (X,Y)
		self.end = (XX,YY)
		self.persent = 0.0
		self.selected = -1
		self.container = None
		self.backgrand = None

	def set_persent(self,persent):
		self.persent = persent

	def draw(self):
		#print self.persent
		self.container.line((self.start,self.end),fill=COLOR_BLACK,width=5)
		endx = int((self.end[0]-self.start[0])*self.persent+self.start[0])
		endy = int((self.end[1]-self.start[1])*self.persent+self.start[1])

		self.container.line((self.start,(endx,endy)),fill=COLOR_WHIT,width=5)

class page(object):	
	def __init__(self,backgrand_path,owner = ("ready",)):
		self.backgrand 	= Image.open(backgrand_path)
		self.container 	= ImageDraw.Draw(self.backgrand)
		self.elements 	= []
		self.shows		=[]
		self.current_element = None
		self.dirty = True
		self.owner = owner
		self.timeout = 0
		self.handle = None
		self.args = None

	def set_timeout(self,timeout,handle,args = None):
		self.timeout = timeout
		self.handle = handle
		self.args = args

	def add_ele(self,ele):
		self.elements.append(ele)
		ele.container = self.container
		ele.backgrand = self.backgrand
		self.current_element = self.elements[-1]

	def add_show(self,show):
		self.shows.append(show)
		show.container = self.container
		show.backgrand = self.backgrand

	def change_focus(self,focus):
		self.focus = focus

	def draw_page(self):
		pass

	def flush_page(self):
		if not self.timeout == 0:
			if time.time() - Page_timer > self.timeout:
				if not self.args == None:
					self.handle(self.args)
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
			self.current_element = self.elements[self.elements.index(self.current_element)-1]

	def next_element(self):
		if self.current_element == self.elements[-1]:
			self.current_element = self.elements[0]
		else:
			self.current_element = self.elements[self.elements.index(self.current_element)+1]

	def click(self):
		pass

class encoder(object):
	def __init__(self,dev=ENCODER_PATH):
		self._device = open(dev,'r')
		self.state = 'n'

	def refresh_state(self):
		self.state = self._device.read(1)

def black_light(state):
	if state == "on":
		Black_light.write(1)
	elif state == "off":
		Black_light.write(0)

def begin_printing(gcode = None):
	waiting("Loading...")
	menu_printing_ctl.redirect_item(0,["Pause",p_pause_printing,1])
	if gcode == None:
		global Current_gcode
		gcode = Current_gcode
	PATH_['m'].beginTask(gcode)
	print gcode
	p_home = p_printing
	jump2page (p_home)

def cancel_printing():
	waiting("Cancel printing...")
	PATH_['m'].cancelTask()
	p_home = p_main_menu
	jump2page (p_home )

def pause_printing():
	PATH_['m'].pauseTask()
	menu_printing_ctl.redirect_item(0,["Resume",p_resume_printing,1])
	jump2page (p_home)

def resume_printing():
	PATH_['m'].resumeTask()
	menu_printing_ctl.redirect_item(0,["Pause",p_pause_printing,1])
	jump2page (p_home)

def save_printing():
	waiting("Saving")
	PATH_['m'].saveTask()
	p_home = p_main_menu
	jump2page (p_home)

def jump2page(page):
	global Current_page
	global Last_page
	global Page_timer
	Page_timer = time.time()
	
	if page == p_printing:
		printer_state.refresh_printer_state()
		print_name_rolling.set_text(Current_gcode)
	elif page == p_printing_ctl_menu:
		if PATH_['m'].state == 'pause':
			menu_printing_ctl.enable_item(-1)
		else:
			menu_printing_ctl.disable_item(-1)
	elif page == p_main_menu:
		PATH_['m'].sendCommand("M109 S0.000000")
		check_SD()
	elif page == p_connection_menu:
		check_wifi()
	elif page == p_refill:
		PATH_['m'].sendCommand("M109 S180.000000")
	
	if len(page.elements) >= 1:
		page.current_element = page.elements[-1]
	Last_page = Current_page
	Current_page = page

def jumpback():
	global Last_page
	jump2page (Last_page)

def extrud():
	#extrud test gcode
	# M109 S100.000000
	# G91
	# G1 F1200 E10
	# G90
	Img_ex_test.play(20)
	PATH_['m'].sendCommand("G91")
	PATH_['m'].sendCommand("G1 F1200 E10")
	PATH_['m'].sendCommand("G90")

def waiting(text):
	p_waiting.shows[0].textstr = text
	jump2page (p_waiting)

def comfirming(text):
	comfirm_msg.set_text(text)
	jump2page (p_confirm)

def attention(text):
	p_attention.shows[0].textstr = text
	jump2page (p_attention)

def check_interrupt():
	interrupted_file = os.listdir(PATH_INTERRUPTED)
	if len(interrupted_file) == 0:
		return False
	file_name_rolling.set_text(interrupted_file[0])
	global Current_gcode
	Current_gcode = PATH_INTERRUPTED+interrupted_file[0]
	tmp_files = os.listdir(PATH_TMP)
	for f in tmp_files:
		os.remove(PATH_TMP+f)
	return True

def save_interrupt():
	waiting("Saving,plase wait a sec...")
	files = os.listdir(PATH_INTERRUPTED)
	for f in files:
		shutil.move(PATH_INTERRUPTED+f,PATH_PAUSED)
	jump2page(p_main_menu)

def skip_interrupt():
	waiting("Removing,plase wait a sec...")
	files = os.listdir(PATH_INTERRUPTED)
	for f in files:
		os.remove(PATH_INTERRUPTED+f)
	jump2page(p_main_menu)

def continue_interrupt():
	global Current_gcode
	files = os.listdir(PATH_INTERRUPTED)
	for f in files:
		shutil.move(PATH_INTERRUPTED+f,PATH_TMP)
	Current_gcode = PATH_TMP+files[0]
	begin_printing()

def check_SD():
	sd_file = os.listdir(PATH_SDCARD)
	if len(sd_file) == 0:
		main_menu.disable_item(-1)
		return False
	else:
		main_menu.enable_item(-1)
		return True

def check_wifi():
	pass

p_logo 				= page(PATH_LOGO)
p_continue			= page(PATH_BLACK)
p_connection_menu	= page(PATH_BLACK)
p_QR_AP 			= page(PATH_QR_AP)
p_QR_STA 			= page(PATH_QR_STA)

p_main_menu 		= page(PATH_BLACK)
p_files_local 		= page(PATH_LOCALFILES)
p_files_sdcard 		= page(PATH_SDCARDFILES)
p_files_paused 		= page(PATH_PAUSEDFILES)

p_refill			= page(PATH_REFILLTEST,("ready","printing","pause"))
p_pullout 			= page(PATH_EXTRUD,("ready","printing","pause"))
p_feedin 			= page(PATH_EXTRUD,("ready","printing","pause"))
p_test 				= page(PATH_TEST,("ready","printing","pause"))

p_printing 			= page(PATH_BLACK,("printing","pause"))
p_printing_ctl_menu = page(PATH_BLACK,("printing","pause"))
p_cancel_printing 	= page(PATH_ATTENTION,("printing","pause"))
p_save_printing		= page(PATH_ATTENTION,("printing","pause"))
p_pause_printing 	= page(PATH_ATTENTION,("printing","pause"))
p_resume_printing 	= page(PATH_ATTENTION,("printing","pause"))

p_power_down		= page(PATH_POEWRDOWN,("ready","printing","pause"))
p_bye				= page(PATH_BYE,("ready","printing","pause"))

p_confirm			= page(PATH_BLACK)
p_waiting			= page(PATH_BLACK,("ready","printing","pause"))

p_home				= p_main_menu

m_encoder = encoder()
p_env = static_p()

UI_printing = [p_printing,p_printing_ctl_menu,p_cancel_printing,p_save_printing,p_pause_printing,p_resume_printing]

#begin build pages
p_QR_AP.add_ele(p_env)
Img_QR_STA = image(47,0,[IMG_PATH_QR])
p_QR_STA.add_ele(p_env)
p_QR_STA.add_show(Img_QR_STA)

please_waiting = textbox("center","Please wait a sec...",font_cn18)
p_waiting.add_show(please_waiting)

Btn_contimue_interrupt_YES = button(150,125,36,60,"YES",continue_interrupt)
Btn_contimue_interrupt_YES.set_warning()
Btn_contimue_interrupt_save = button(80,125,36,60,"Save",save_interrupt)
Btn_contimue_interrupt_skip = button(10,125,36,60,"Skip",skip_interrupt)
p_continue.add_ele(Btn_contimue_interrupt_skip)
p_continue.add_ele(Btn_contimue_interrupt_save)
p_continue.add_ele(Btn_contimue_interrupt_YES)
file_name_rolling = rolling_text(0,"",font_mdcn24)
p_continue.add_show(file_name_rolling)
continue_msg = textbox((10,36,210,72),"was interrupted,continue?",font_cn20)
p_continue.add_show(continue_msg)
time_msg = textbox((10,85,180,110),"auto-start after" ,font_cn18)
p_continue.add_show(time_msg)
clock = timer_show((160,96),20)
p_continue.add_show(clock)
p_continue.set_timeout(20,continue_interrupt)

local_files = file_list("files",PATH_LOCAL)
p_files_local.add_ele(local_files)

sdcard_files = file_list("files",PATH_SDCARD)
p_files_sdcard.add_ele(sdcard_files)

paused_files = file_list("files",PATH_PAUSED)
p_files_paused.add_ele(paused_files)

main_menu = menu("mainme",[["Connect info",p_connection_menu,1],["Files in printer",p_files_local,1],["Refill & Test",p_refill,1],["Paused files",p_files_paused,1],["Files in SD card",p_files_sdcard,0]])
p_main_menu.add_ele(main_menu)

menu_printing_ctl = menu("pctlme",[["Pause",p_pause_printing,1],["Stop & Save",p_save_printing,1],["Cancel Printing",p_cancel_printing,1],["Refill & Test",p_refill,0]])
p_printing_ctl_menu.add_ele(menu_printing_ctl)
p_printing_ctl_menu.set_timeout(30,jump2page,p_home)

menu_connection = menu("pctlme",[["AP-mode",p_QR_AP,1],["STA-mode",p_QR_STA,1]])
p_connection_menu.add_ele(menu_connection)

printer_state = printing("printer",PATH_['m'])
p_printing.add_ele(printer_state)
print_name_rolling = rolling_text(0,Current_gcode,font_mdcn30,'l')
p_printing.add_show(print_name_rolling)

Btn_cancel_print_NO = button(20,125,36,64,"NO",jumpback)
Btn_cancel_print_YES = button(135,125,36,64,"YES",cancel_printing)
Btn_cancel_print_YES.set_warning()
p_cancel_printing.add_ele(Btn_cancel_print_YES)
p_cancel_printing.add_ele(Btn_cancel_print_NO)
cancel_msg = textbox("center","Printing will be cancel",font_cn18)
p_cancel_printing.add_show(cancel_msg)

Btn_pause_print_NO = button(20,125,36,64,"NO",jumpback)
Btn_pause_print_YES = button(135,125,36,64,"YES",pause_printing)
Btn_pause_print_YES.set_warning()
p_pause_printing.add_ele(Btn_pause_print_NO)
p_pause_printing.add_ele(Btn_pause_print_YES)
pause_msg = textbox("center","Printing will be pause",font_cn18)
p_pause_printing.add_show(pause_msg)

Btn_resume_print_NO = button(20,125,36,64,"NO",jumpback)
Btn_resume_print_YES = button(135,125,36,64,"YES",resume_printing)
Btn_resume_print_YES.set_warning()
p_resume_printing.add_ele(Btn_resume_print_NO)
p_resume_printing.add_ele(Btn_resume_print_YES)
resume_msg = textbox("center","Resume printing",font_cn18)
p_resume_printing.add_show(resume_msg)

Btn_save_print_NO = button(20,125,36,64,"NO",jumpback)
Btn_save_print_YES = button(120,125,36,64,"YES",save_printing)
Btn_save_print_YES.set_warning()
p_save_printing.add_ele(Btn_save_print_NO)
p_save_printing.add_ele(Btn_save_print_YES)
save_msg = textbox("center","Stop printing and save",font_cn18)
p_save_printing.add_show(save_msg)

Btn_refill_quit = button(20,125,36,64,"Quit",jump2page,p_main_menu)
Btn_refill_next = button(135,125,36,64,"Next",jump2page,p_pullout)
Btn_refill_next.set_warning()
p_refill.add_ele(Btn_refill_quit)
p_refill.add_ele(Btn_refill_next)
# refill_msg = textbox((10,46,210,90),"Please wait for extruder heating up",font_cn18)
# p_refill.add_show(refill_msg)
# temp_msg = textbox((10,90,210,115),"",font_cn18)
# p_refill.add_show(temp_msg)
temp_bar = process_bar((110,97),(110,32))
p_refill.add_show(temp_bar)

Btn_pullout_next = button(135,125,36,64,"Next",jump2page,p_feedin)
Btn_pullout_next.set_warning()
p_pullout.add_ele(Btn_pullout_next)
Img_pullout =image(0,0,[IMG_PATH_PULLOUT,IMG_PATH_PULLOUT1,IMG_PATH_PULLOUT2])
p_pullout.add_show(Img_pullout)
pullout_msg = textbox((130,30,210,120),"Pull out the filament gently",font_cn18)
p_pullout.add_show(pullout_msg)

Btn_feedin_next = button(135,125,36,64,"Next",jump2page,p_test)
Btn_feedin_next.set_warning()
p_feedin.add_ele(Btn_feedin_next)
Img_feedin =image(0,0,[IMG_PATH_FEEDIN,IMG_PATH_FEEDIN1,IMG_PATH_FEEDIN2])
p_feedin.add_show(Img_feedin)
feedin_msg = textbox((130,30,210,120),"Feed in new filament",font_cn18)
p_feedin.add_show(feedin_msg)

Btn_refill_finish = button(130,125,36,74,"Finish",jump2page,p_home)
Btn_extrud_test = button(20,125,36,64,"Test",extrud)
Btn_extrud_test.set_warning()
p_test.add_ele(Btn_refill_finish)
p_test.add_ele(Btn_extrud_test)
# test_msg = textbox((130,45,210,120),"Extruder testing...",font_cn18)
# p_test.add_show(test_msg)
Img_ex_test = image(0,0,[IMG_PATH_EX1,IMG_PATH_EX2,IMG_PATH_EX3,IMG_PATH_EX4],0)
p_test.add_show(Img_ex_test)

Btn_confirm_YES = button(135,125,36,64,"Print",begin_printing)
Btn_confirm_YES.set_warning()
Btn_confirm_NO = button(20,125,36,64,"Back",jumpback)
comfirm_msg = textbox((10,10,210,120),"",font_mdcn24)
p_confirm.add_show(comfirm_msg)
p_confirm.add_ele(Btn_confirm_NO)
p_confirm.add_ele(Btn_confirm_YES)


def m_UI():
	global Lcd_sleep
	global Lcd_wake_time
	global Current_page
	
	Black_light.dir(mraa.DIR_OUT)
	m_pages = range(0,20)

	#UI start
	black_light("on")
	tft = subprocess.Popen("/mostfun/TFT_8340", stdin = subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
	time.sleep(2)

	Interrupted = check_interrupt()
	if Interrupted:
		jump2page (p_continue)
	else:
		jump2page (p_main_menu)
	Current_page.flush_page()
	Lcd_wake_time = time.time()

	while True:

		#begin = time.time()
		if Lcd_sleep == False:
			if time.time()-Lcd_wake_time > LCD_SLEEP_TIMEOUT:
				Lcd_sleep = True
				black_light("off")
			
			if not PATH_['m'].state in Current_page.owner:
				# if Current_page == p_printing:
				# 	p_printing.dirty = True
					#time.sleep(0.02)
				if PATH_['m'].state  == "printing" or PATH_['m'].state  == "pause":
					p_home = p_printing
				else:
					p_home = p_main_menu

				jump2page(p_home)

			if Current_page == p_refill:
				#print PATH_['m']._extruderTemp/200.0
				temp_bar.set_persent(PATH_['m']._extruderTemp/200.0)
				if PATH_['m']._extruderTemp < 175:
					Btn_refill_next.disable()
				else:
					Btn_refill_next.enable()

			Current_page.flush_page()
			time.sleep(0.01)
			tft.send_signal(2)
			time.sleep(0.01)
		# end = time.time()
		#print 1.0/(end-begin)

def input_env():
	global Current_page
	global Lcd_sleep
	global Lcd_wake_time

	while True:
		m_encoder.refresh_state()

		if Lcd_sleep == True:
			Lcd_wake_time = time.time()
			Lcd_sleep = False
			black_light("on")

		else:
			if m_encoder.state == '<':
				try:
					Current_page.current_element.left_click()
					# Current_page.dirty = True
					print '<'
				except :
					pass

			elif m_encoder.state == '>':
				try:
					Current_page.current_element.right_click()
					# Current_page.dirty = True
					print '>'
				except :
					pass

			elif m_encoder.state == '0':
				try:
					Current_page.current_element.click()
					# Current_page.dirty = True
					print '0'
				except :
					pass

			elif m_encoder.state == '1':
				if not Current_page == p_continue:
					jump2page (p_home)
				# Current_page.dirty = True
				print '1'

			elif m_encoder.state == '!':
				pass #power down
			Lcd_wake_time = time.time()
			m_encoder.state = 'n'

def UI_monitor():
	thread.start_new_thread(m_UI, ())
	time.sleep(1)
	thread.start_new_thread(input_env, ())





