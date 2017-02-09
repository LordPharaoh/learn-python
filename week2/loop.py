from random import randint
# ># these are comments
#They are greyed out and not read by the interpreter
#They don't count as code
#A boolean variable holds true or false
#A while loop repeats the code until a boolean becomes false
my_number = randint(1, 100)
guess_num = 0
number_guessed = False

print("Guessing Game")
while number_guessed == false:
	guess = int(input("Enter your guess from 1-100: "))
	guess_num = guess_num + 1
	if my_number > guess:
		#what should I print here?
		print("")
	#what goes in this if statement?
	if put_your_code_here:
		print("Lower")
	if my_number == guess:
		print("You guessed the number in " + guess_num + " guesses!")
		#what can I write here to stop the loop?

