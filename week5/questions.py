#Question 1: What line does 'bananas' go out of scope?
if 5 > 3:
	bananas = "Five is bigger than three. Checks out."
	print(bananas)
#Question 2: What line does 'oranges' go out of scope?
oranges = 0;
for i in range(7):
	oranges = "I have " + str(i) + " oranges."
#Question 3: What value is printed out?
coffee = "hi"
for i in range(2):
	coffee = coffee + " " + str(i)
print(coffee)
#Question 4: What line does 'monkeys' go out of scope?
def flying_monkeys(monkeys):
	print("MORE MONKEYS")
	return str(monkeys) + "THERE WILL ALWAYS BE MORE MONKEYS"
#Question 5: What line does 'burgers' go out of scope?
def moar_burgers():
	burgers = "moar"
	return burgers
#Question 6: What is printed after these lines?
for i in range(6):
	cats = i
	for j in range(10):
		cats = i + j
		print(cats)
	print(cats)

