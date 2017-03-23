import tetris_grid as tg
import time
from random import randint

def rand_color():
		"""return a random color for tetriminoes"""
		color=randint(0,5)
		if color == 0:
				color = "blue"
		elif color == 1:
				color = "red"
		elif color == 2:
				color = "pink"
		elif color == 3:
				color = "yellow"
		elif color == 4:
				color = "green"
		elif color == 5:
				color = "orange"
		return color

yhigh = 0;
ylow = 1;
x = 5
WhichShape = randint(1,5)
colorchosen = rand_color()
move_down = True
def draw_shape():
		"""makes a new tetrimino at the top of the screen"""
		global move_down 
		if WhichShape == 1:
				if (ylow > 20) or \
					(tg.get_tile(x, yhigh) != False) or \
					(tg.get_tile(x+1, yhigh) != False) or \
					(tg.get_tile(x+1, ylow) != False) or \
					(tg.get_tile(x, ylow) != False):
					move_down = False
				else: 
					tg.set_tile(x,yhigh,colorchosen)
					tg.set_tile(x+1,yhigh,colorchosen)
					tg.set_tile(x+1,ylow,colorchosen)
					tg.set_tile(x,ylow,colorchosen)
		elif WhichShape == 2:
				if (yhigh > 20) or \
					(tg.get_tile(x, yhigh) != False) or \
					(tg.get_tile(x+1, yhigh) != False) or \
					(tg.get_tile(x+2, yhigh) != False) or \
					(tg.get_tile(x+3, yhigh) != False):
					move_down = False
				else: 
					tg.set_tile(x,yhigh,colorchosen)
					tg.set_tile(x+1,yhigh,colorchosen)
					tg.set_tile(x+2,yhigh,colorchosen)
					tg.set_tile(x+3,yhigh,colorchosen)
		elif WhichShape == x-2:
				if (ylow > 20) or \
					(tg.get_tile(x, yhigh) != False) or \
					(tg.get_tile(x+1, yhigh) != False) or \
					(tg.get_tile(x+1, ylow) != False) or \
					(tg.get_tile(x+2, ylow) != False):
					move_down = False
				else: 
					tg.set_tile(x,yhigh,colorchosen)
					tg.set_tile(x+1,yhigh,colorchosen)
					tg.set_tile(x+1,ylow,colorchosen)
					tg.set_tile(x+2,ylow,colorchosen)
		elif WhichShape == x-1:
				if (ylow > 20) or \
					(tg.get_tile(x, yhigh) != False) or \
					(tg.get_tile(x, ylow) != False) or \
					(tg.get_tile(x+1, ylow) != False) or \
					(tg.get_tile(x-1, ylow) != False):
					move_down = False
				else: 
					tg.set_tile(x,yhigh,colorchosen)
					tg.set_tile(x,ylow,colorchosen)
					tg.set_tile(x+1,ylow,colorchosen)
					tg.set_tile(x-1,ylow,colorchosen)
		elif WhichShape == x:
				if (ylow > 20) or \
					(tg.get_tile(x-2, ylow) != False) or \
					(tg.get_tile(x-2, yhigh) != False) or \
					(tg.get_tile(x-1, yhigh) != False) or \
					(tg.get_tile(x, yhigh) != False):
					move_down = False
				else: 
					tg.set_tile(x-2,ylow,colorchosen)
					tg.set_tile(x-2,yhigh,colorchosen)
					tg.set_tile(x-1,yhigh,colorchosen)
					tg.set_tile(x,yhigh,colorchosen)


def delete_block():
		if WhichShape == 1:
				tg.unset_tile(5,yhigh)
				tg.unset_tile(6,yhigh)
				tg.unset_tile(6,ylow)
				tg.unset_tile(5,ylow)
		if WhichShape == 2:
				tg.unset_tile(5,yhigh)
				tg.unset_tile(6,yhigh)
				tg.unset_tile(7,yhigh)
				tg.unset_tile(8,yhigh)
		if WhichShape == 3:
				tg.unset_tile(5,yhigh)
				tg.unset_tile(6,yhigh)
				tg.unset_tile(6,ylow)
				tg.unset_tile(7,ylow)
		if WhichShape == 4:
				tg.unset_tile(5,yhigh)
				tg.unset_tile(5,ylow)
				tg.unset_tile(6,ylow)
				tg.unset_tile(4,ylow)
		if WhichShape == 5:
				tg.unset_tile(3,ylow)
				tg.unset_tile(3,yhigh)
				tg.unset_tile(4,yhigh)
				tg.unset_tile(5,yhigh)

def move_right():
	global x
	x += 1
	
def move_left():
	global x
	x -= 1
	

#this text grey
def check_rows():
		"""Checks if row should be removed"""

while True:
		tg.update()
		delete_block()
		yhigh += 1
		ylow += 1
		draw_shape()
		if move_down == False:
				yhigh -= 1
				ylow -= 1
				draw_shape()
				yhigh = 0
				ylow = 1
				WhichShape = randint(1,5)
				colorchosen = rand_color()
				move_down = True
				draw_shape()
		time.sleep(.1)

