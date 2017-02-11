# Recap
In our second lesson, we covered
- The `grid` environment
- Setting and coloring tiles
- the 'forever' `while True:` loop
- Using variables to move and animate tiles

Our students were free to work on any project that interested them. Some of the creations included a blinking face, a moving rainbow, and a bouncing ball.

# Homework
The assignment for this week is to create any grid project that includes both a flashing and a moving tile. All of our students have done at least one of these things, and further assistance is provided below in learning the other.

#Github
This recap and the grid code are both hosted on github, a software hosting website. You can download all the code in a [zip file.](https://github.com/LordPharaoh/learn-python/archive/master.zip) There are some more instructions one downloading the software included in the ["Downloading This"](https://github.com/LordPharaoh/learn-python#downloading-this) section of the README.
Folders are sorted by week and you can click on any recap file to see a formatted version in your browser.
# Cheatsheet
#####This continues to build off the [cheatsheet that was distributed last week.](https://github.com/LordPharaoh/learn-python/blob/master/week1/recap.md)
##Code Examples

These are meant to be typed into file that contains a `while True:` loop, not the python interpreter.
####Importing Grid
You *must* have the grid.py file **in the same folder** for this to work.
```python
import grid
```
introduces the functionality of the grid file.
####Setting a Tile
The grid is numbered to facilitate finding grid locations.
```python
grid.set_tile(1, 1)
grid.set_tile(1, 2, "green")
#A few of our students were able to work with hexadecimal colors yesterday
grid.set_tile(1, 3, "#fe4a2a")
```
####Unset a tile
```python
grid.unset_tile(1, 1)
```
####Set a tile to the opposite
This does not work for colored tiles
```python
grid.toggle(1, 1)
```
####Get the value of a tile
```python
grid.get_tile(1, 1)
```
####Clearing or unsetting all tiles
```python
grid.clear()
```
####Painting the grid
Every time you call update, the grid will display the set tiles. **If you do not call this function in your loop, your grid will never change.**
```python
grid.update()
``` ####While 
If the program quits, the window will close and we won't be able to see our work. Every program needs to end in 
```python
while True:
	#your code goes here
	grid.update()
	#1 frame per second, this number can be whatever makes you feel comfortable testing with
	time.sleep(1)
```
####Using variables for movement
You can use variables to save the position of your square.
```python
x_pos = 0
while True:
	x_pos = x_pos + 1
	grid.set_tile(x_pos, 3)
	grid.update()
	time.sleep(1)
```
Every time you go through the loop, x_pos is increased by one so the tile is painted one to the right. You can also use `if` statements in conjunction with this to 'bounce' off walls like so:
```python
x_pos = 0
go_right = True
while True:
	#if we are supposed to be going right, add 1 to x
	if go_right == True:
		x_pos = x_pos + 1
	#if not subtract one from x
	else:
		x_pos = x_pos - 1

	grid.set_tile(x_pos, 3)
	grid.update()
	time.sleep(1)
	#if we are at an edge, start going the other direction
	if x_pos == 14:
		go_right = False
	if x_pos == 0:
		go_right = True
```
Now every time you hit the edge of the grid, we begin going to other direction (subtracting instead of adding to x)
####Toggling colors
Toggling colors is a little bit trickier; you need to keep track of what the color is and what it should be and then set it to that color.
```python
while True:
	if grid.get_tile(1, 1) == "green":
		grid.set_tile(1, 1, blue)
	if grid.get_tile(1, 1) == "blue":
		grid.set_tile(1, 1, green)
	grid.update()
	time.sleep(1)
```
