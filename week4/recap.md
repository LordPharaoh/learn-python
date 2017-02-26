# Recap
In our fourth lesson, we covered
- Returning values from functions
- Continued to work on for loops, including nested for loops
- Ethan and Chris used the internet to find out how to make sounds, and taught the other students as well.

# Homework
The assignment for this week is to create two functions: 
1. Return a random color: `set_tile(0, 0, random_color())`
2. Make a block of the given size and shape and return its area. If your student has not yet learned multiplication, then have them return the color of the top-right tile. `block(x, y, width, height)`

#Github
This recap and the grid code are both hosted on github, a software hosting website. You can download all the code in a [zip file.](https://github.com/LordPharaoh/learn-python/archive/master.zip) There are some more instructions one downloading the software included in the ["Downloading This"](https://github.com/LordPharaoh/learn-python#downloading-this) section of the README.
Folders are sorted by week and you can click on any recap file to see a formatted version in your browser.
# Cheatsheet
#####This continues to build off the previous cheat sheets 
-[Week 1](https://github.com/LordPharaoh/learn-python/blob/master/week1/recap.md)
-[Week 2](https://github.com/LordPharaoh/learn-python/blob/master/week2/recap.md)
-[Week 3](https://github.com/LordPharaoh/learn-python/blob/master/week3/recap.md)
##Code Examples
###Returning from a function
Last week we learned how functions can work as 'shorcuts' in our code. We were able to use them to accomplish tasks quicker with less typing.
This week, we extend that to learn how to use them to replace values, or give us 'answers', instead of just doing a task quicker.
```python
def multiply(x, y):
	ans = x * y
	return ans
#We call the function with its name and the values to substitute for x and y.
#Wherever we type the function name followed by parenthes, it replaces that with the answer (in this case, 25)
print(square(5, 5))
```
###Nested for loops
We learned how to make blocks of tiles by putting for loops inside other for loops.
Last week, students learned how to make a bar across the screen with a for loop.
```
for i in range(5):
	grid.set_tile(1, i)
```
Creates a 1x5 bar at the postion (1, 0). Each iteration of the for loop, the loop set a tile with a different value of i.
We can put this inside another for loop to make a bar for each value of i, creating a bunch of bars: a rectangle.
```
for x in range(5):
	#Be careful not to use the same variable for the inner and outer for loops
	for y in range(7):
		grid.set_tile(x, y)
```
creates a 5x7 rectangle.
###Sound
Last week, two of our students were able to make sounds using python. Unfortunately, this is very system-dependent. 
A solution is presented for Windows computers only; attaining similar functionality for Mac and Linux is possible, but a much more involved process.
```
import winsound
#frequency, duration in milliseconds (1000=1 second)
winsound.beep(1000, 500)
``



