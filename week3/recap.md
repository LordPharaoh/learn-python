# Recap
In our third lesson, we covered
- Functions and how they can save you time
- For loops and number based iteration
- Commenting and how it can improve our code

# Homework
The assignment for this week is to create any grid project that uses functions to draw an object. We did go over the for loop as well, but most students decided to use functions in their projects.

#Github
This recap and the grid code are both hosted on github, a software hosting website. You can download all the code in a [zip file.](https://github.com/LordPharaoh/learn-python/archive/master.zip) There are some more instructions one downloading the software included in the ["Downloading This"](https://github.com/LordPharaoh/learn-python#downloading-this) section of the README.
Folders are sorted by week and you can click on any recap file to see a formatted version in your browser.
# Cheatsheet
#####This continues to build off the [cheatsheet that was distributed last week.](https://github.com/LordPharaoh/learn-python/blob/master/week1/recap.md)[ and the one after that.](https://github.com/LordPharaoh/learn-python/blob/master/week1/recap.md)
##Code Examples
###Functions
Function can do a lot of useful things, but we have primarily used them as a time saving method to draw things onto our grid. The function will run some piece of code for us with any value we give it. We can create a function to draw a 2x2 square at given co-ordinates, for example.
```python
def square(5, 5):
	grid.set_tile(x, y)
	grid.set_tile(x + 1, y)
	grid.set_tile(x, y + 1)
	grid.set_tile(x + 1, y + 1)
#We call the function with its name and the values to substitute for x and y.
square(x, y)
```
We can make a function for any shape by choosing one point to be the point that will be specified in the function, subtracting X value of that point from every other X value and doing the same with Y.
Take the example of a simple line.
I choose the point `(3, 5)` to be the 'origin point'.
```python
grid.set_tile(3, 5)
grid.set_tile(3, 6)
grid.set_tile(3, 7)
```
Since `(3, 5)` is the origin point, I subtract 3 from every x value and 5 from every y value.
```python
def line(x, y):
	grid.set_tile(3 - 3 + x, 5 - 5 + y)
	grid.set_tile(3 - 3 + x, 6 - 5 + y)
	grid.set_tile(3 - 3 + x, 7 - 5 + y)
# and now if I do
line(3, 5)
# it will recreate the original line and
line(6, 7)
# will create it somewhere else
```
### For loop
We can use for loops to do something a given number of times.
```python
>>> for i in range(9):
...		print(i)
0
1
2
3
4
5
6
7
8
9
```
This is helpful in our grid because we can block out whole sections of it at once
```python
for i in range(14):
	grid.set_tile(0, i)
```
will block out the whole top row because the for loop cycles through every possible number for Y.
### Comments
In python, every line prefaced with a `#`, hashtag, crunch, octothorpe, number sign, will be *ignored* by python. You can use these to 'comment' your code, or help describe it to yourself and others.
This makes it easier to pick up where you left off when you start coding again.

