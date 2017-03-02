# Scope
A *scope* is the length of code that a variable is 'alive' for.
Python has a set of rules for scoping, but we will be learning the most basic (and most important) concepts.

**Variables are valid till the next back indentation.**

```python
#The entire file can see this variable which is not indented at all.
#These types of variables are called *global* variables.
everyone_can_see_me = 5

def function1():
	#Everything in this function can see this variable
	function1_can_see = "whee"

#we have gone back one indent space
#You can *no longer use function1_can_see*. You will get an error if you try.
#function1_can_see has gone *out of scope*.

for i in range(10):
	only_this_loop = i
	print(only_this_loop)

#only_this_loop has now gone out of scope

def function2():
	#function2 can't see function1_can_see. function1_can_see is still not in scope.
	#It can make its own variabls though
	function2_can_see = "cool"
	#you can reuse the name of this variable since its out of scope
	#The computer doesn't need it anymore so you can use it for something else
	function1_can_see = "hi"

def function3(param1):
	#parameters are only in scope for the current function
	print(param1)

#param1 is no longer valid, it has gone out of scope

def function4(param1):
	print(param1)
	#HEY! param1 still works here! what's up
	#this param1 is *different* from the other param1
	#The other param1 is out of scope, so we can reuse the name param1 for something else

#This code will give you an error!
if True:
	message = "mess"
#message has gone out of scope and is undefined
print(message)

#This code will work
message = ""
if True:
	message = "mess"
print(message)
#instead of making a new variable, the if statement just takes the variable 'message' that we declared earlier
#message is a global variable, so the print statement that comes after the if knows what it is
```

#Scoping Quiz
1 Will this code produce an error?
```python
	def example(param1):
		print param1
	def example2(param1):
		print param1
```
Mark one: **T[ ] F[ ]**

2 What will be the output of
```python
	example(5)
	example2(6)
```
Write an answer.
 
3 Which one of these examples would not produce an error?
```python
def example_a(param1, param2):
	return param1 + param2
	print(param1 + param2)

def example_b(param1, param2):
	return param1 + param2
print(param1 + param2)

def example_c(param1, param2):
	return param1 + param2
	param1 = 5
print(param1 + param2)
```
Mark one: **A[ ] B[ ] C[ ]**

4 Will this code produce an error?
```python
for i in range(10):
	count = 0
	for h in range(5):
		count = h
	print count
```
Mark one: **T[ ] F[ ]**

5 *Bonus* What will the previous example print out?
Write an answer




	
