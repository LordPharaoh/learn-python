from Tkinter import *

master = Tk()

width = 600
height = 600
tile_size = 40
dark_color = "#050505"
light_color = "#bbbbbb"
line_color = "#888888"
text_color = "#888888"
text_offset = tile_size / 2
show_coords = True

canvas = Canvas(master, width=width, height=height)
canvas.pack()

grid = []
for x in range(int(width/tile_size)):
	yapp = [False] * int((height/tile_size))
	grid.append(yapp)

#backgrid = list(grid)

def set_tile(x, y):
	grid[x][y] = True
def unset_tile(x, y):
	grid[x][y] = False
def toggle_tile(x, y):
	grid[x][y] = not grid[x][y]
def get_tile(x, y):
	return grid[x][y]

def update():
	canvas.delete("all")
	for x, col in enumerate(grid):
		for y, tile in enumerate(col):
			color = dark_color if tile else light_color
			canvas.create_rectangle(int(x * tile_size), int(y * tile_size), int(tile_size * (x + 1)), int(tile_size * (y + 1)), fill=color, outline=line_color)
			if show_coords:
				canvas.create_text(int(x * tile_size) + text_offset, int(y * tile_size) + text_offset, fill=text_color, text=(str(x) + "," + str(y)))
	canvas.update()
			

def clear():
	for x, col in enumerate(grid):
		for y, tile in enumerate(col):
			tile = False

#clear()
#set_tile(0, 0)

#update()

#uncomment if testing, comment to use as library
#while True:
	#update()


