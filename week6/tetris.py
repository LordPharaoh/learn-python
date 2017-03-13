import tetris_grid as tg
import time
from random import randint

def rand_color():
	"""return a random color for tetriminoes"""
	color=randint(0,2)
	if color == 0:
		color = "blue"
	elif color == 1:
		color = "red"
	elif color == 2:
		color = "white"
	return color


def make_shape():
	"""makes a new tetrimino at the top of the screen"""
	WhichShape = randint(1,5)
	colorchosen = rand_color()
	if WhichShape == 1:
		tg.set_tile(5,0,colorchosen)
		tg.set_tile(6,0,colorchosen)
		tg.set_tile(6,1,colorchosen)
		tg.set_tile(5,1,colorchosen)
	elif WhichShape == 2:
		tg.set_tile(5,0,colorchosen)
		tg.set_tile(6,0,colorchosen)
		tg.set_tile(7,0,colorchosen)
		tg.set_tile(8,0,colorchosen)
	elif WhichShape == 3:
		tg.set_tile(5,0,colorchosen)
		tg.set_tile(6,0,colorchosen)
		tg.set_tile(6,1,colorchosen)
		tg.set_tile(7,1,colorchosen)
	elif WhichShape == 4:
		tg.set_tile(5,0,colorchosen)
		tg.set_tile(5,1,colorchosen)
		tg.set_tile(6,1,colorchosen)
		tg.set_tile(4,1,colorchosen)
	elif WhichShape == 5:
		tg.set_tile(3,1,colorchosen)
		tg.set_tile(3,0,colorchosen)
		tg.set_tile(4,0,colorchosen)
		tg.set_tile(5,0,colorchosen)

#kill
def move_down():
	"""moves all not-down tiles one down"""
#this text grey
def check_rows():
	"""Checks if row should be removed"""
make_shape()
while True:
	tg.update()
	time.sleep(1)
