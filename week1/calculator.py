print("CALCULATOR")

number1 = int(input("Enter your first number:"))
number2 = int(input("Enter your second number:"))
operator = input("+, -, /. or * ? :")

if operator == "+":
	answer = number1 + number2
	print("ANS = " + str(answer))

