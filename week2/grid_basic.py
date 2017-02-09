#I can import another file or a library by using the grid command
import grid
import time

#sets a specific tile to dark
grid.set_tile(0, 0)
grid.set_tile(1, 1)
#sets a specific tile to light
grid.unset_tile(1, 1)
grid.set_tile(1, 2, "green")
#makes the tile dark if its light and vice versa
#prints if tile is dark
print(grid.get_tile(1, 1))
#makes everything in the grid light
#grid.clear()

#we can't let the program end or the window will close
while True:
	grid.toggle_tile(1, 1)
	grid.update()
	#loops every 1 second
	time.sleep(1)
