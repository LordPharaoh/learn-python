#I can import another file or a library by using the grid command
import grid
import time

#sets a specific tile to dark
grid.set_tile(0, 0)
grid.set_tile(1, 1)
#sets a specific tile to light
grid.unset_tile(1, 1)
#makes the tile dark if its light and vice versa
#prints if tile is dark
print(grid.get_tile(1, 1))
#makes everything in the grid light
grid.clear()

#we can't let the program end or the window will close
x_pos = 0
y_pos = 0
while True:
	grid.set_tile(x_pos, y_pos)
	x_pos = x_pos + 1
	y_pos = y_pos + 1
	grid.update()
	#loops every 1 second
	time.sleep(1)
