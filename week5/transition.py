#I can import another file or a library by using the grid command
import grid
import time
from random import randint

def rand_color():
	rand = randint(0, 6)
	color = ""
	if rand == 0:
		color = "pink"	
	if rand == 1:
		color = "purple"	
	if rand == 2:
		color = "red"	
	if rand == 3:
		color = "green"	
	if rand == 4:
		color = "blue"	
	if rand == 5:
		color = "yellow"	
	if rand == 6:
		color = "orange"	
	return color	

def set_all_random():
	for x in range(15):
		for y in range(15):
			grid.set_tile(x, y, rand_color())

def wipe_from_top(color):
	for y in range(15):
		for x in range(15):
			grid.set_tile(x, y, color)
		grid.update()
		time.sleep(.3)

def spiral_from_out(color):
	length = 14
	xpos = 0
	ypos = 0
	for r in range(31):
		for k in range(length):
			grid.set_tile(xpos, ypos, color)
			if r % 4 == 0:
				xpos = xpos + 1
			elif r % 4 == 1:
				ypos = ypos + 1
			elif r % 4 == 2:
				xpos = xpos - 1
			elif r % 4 == 3:
				ypos = ypos - 1
			grid.update()
			time.sleep(.005)
		if r % 2 == 0 and not r == 0:
			length -= 1
while True:
	set_all_random()
	grid.update()
	spiral_from_out("red")
	#loops every 1 second
	time.sleep(1)
