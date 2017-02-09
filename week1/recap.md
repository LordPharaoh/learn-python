# Recap
In our first lesson, we covered
- basic Python syntax
- printing `"strings" and variables`
- requesting and storing input with the `input` command
- simple usage of the `if` statement

Many of our students are at different stages, but most of them have the basic idea behind these four concepts. There is a cheatsheet for your usage below.

# Homework
The homework for the first week is to create a simple calculator that asks for two inputs and prints the sum of the two numbers. Students that wish to go above and beyond can adapt this project to work with multiple operations (+, \*, -, /). This includes requesting a number input. Some students who chose to make a simple guessing game have covered this concept; some have not. Students can use the `input` command they are familiar with in conjunction with `int()` (which stands for integer, another word for number), to change a *string* input (like a name, or 'yes' or no' as in the examples students were working with) to an *integer*.
Here's a complete example.
```python
number1 = int(input("Enter your first number."))
```

When completing the homework, its important to remember a few things:
- Errors are common, especially when starting programming. It's important not to get discouraged!
- The red error text can be scary and hard to read, but it will tell you important things you need to know to fix your program.
- If you have any questions at any time, you can always send me an email.

#Downloading Python
You can get [Python 2.7](https://www.python.org/downloads/release/python-2713/) for any platform on the Python website. The download should include the command line version as well as the IDLE that the students have been using. You should be able to open the IDLE immediately by clicking on the icon in Windows and Mac. To use the command line, however, the Python directory must be added to the PATH. This is system specific; the [Python installation documentation](https://docs.python.org/2/using/windows.html) can provide more help than I. If you have any questions or are having trouble with this, please let me know. As a last resort, online environments such as [repl.it](repl.it) are available as well.
# Cheatsheet
##Vocabulary
- Variable: A 'box' in which the computer stores information. Variables can be set with the `=` operator. `my_number = 5` sets the variable `my_number` to 5. Later, if we see `my_number` in our code, it replaces it with `5`. For example,
```python
>>> print(my_number - 2)
3
```
- `>>>`: The python interpreter's command prompt. Anything in this cheatsheet preceded by `>>>` can be typed directly into the IDLE to see an example.
- String: A string is a *type* of variable that represents text. Anything in quotation marks is a type of string. Strings can also be stored in variables, like `name`, as students saw earlier today.
- Integer: An integer is a *type* of variable that holds a whole number. When students created their guessing game, `rand`, the number they were trying to guess, and `guess`, the user's guess, were both integers.
##Code Examples

####Print a String
```python
>>> print("Hello World!")
"Hello World!"
```
####Get String Input
```python
>>> your_name = input("What's your name? ")
What's your name? Varun
>>> print("Hello " + your_name)
Hello Varun
```
####Convert String to Integer (number)
```python
>>> guess = int(input("Guess a number: "))
Guess a number: 7
>>> print(guess)
7
```
####Add Two Integer Variables Together
```python
>>> number1 = 5
>>> number2 = 7
>>> answer = number1 + number2
>>> print(answer)
12
```
####Add Two String Variables Together
```python
>>> name = "Varun"
>>> print("Hi " + name)
Hi Varun
```
####If Statement
*Note: The prompt for indentation in the `if` statement (`...` in this case) will vary by system. It is `...` in the command line but may be blank in the IDLE.*
```python
>>> x = 4
>>> if x > 3:
...    print("X is bigger than 3")
...
X is bigger than 3
```
Indentation matters in python. Everything that you are asking the computer to do if x is greater than 3 is *indented*, or moved over by four spaces. When you are done with the if statement and want to move to the next instruction, you continue *without* the four spaces.
####Equality
In python `>` and `<` can be used in `if` statements; we will learn more about these expressions (known as *booleans*) in the next session. It's important to note, however, that **`x = 5` is *incorrect* in an `if` statement**. This is a common mistake when beginning programming; the correct syntax is `x == 5`.

