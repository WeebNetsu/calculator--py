def add(x, y, t):
	if t:
		return int(x) + int(y)
	else:
		return float(x) + float(y)

def subtract(x, y, t):
	if t:
		return int(x) - int(y)
	else:
		return float(x) - float(y)

def multi(x, y, t):
	if t:
		return int(x) * int(y)
	else:
		return float(x) * float(y)

def divide(x, y, t):
	if x == 0 or y == 0:
		return "Could not divide by 0"

	if t:
		return int(x) / int(y)
	else:
		return float(x) / float(y)

def pow(x, y, t):
	if t:
		return int(x) ** int(y)
	else:
		return float(x) ** float(y)

def mod(x, y, t):
	if t:
		return int(x) % int(y)
	else:
		return float(x) % float(y)

def calc(num1, num2, integer):
	print("What would you like to do? (add(+), subtract(-), divide(/), multiply(*), power(^), mod(%))")
	action = input("Your answer: ")

	if action.lower() in ["+", "add", "addition", "plus"]:
		print(num1 + " + " + num2 + " = " + str(add(num1, num2, integer)))
	elif action.lower() in ["-", "subtract", "sub", "minus"]:
		print(num1 + " - " + num2 + " = " + str(subtract(num1, num2, integer)))
	elif action.lower() in ["*", "multiply", "x"]:
		print(num1 + " x " + num2 + " = " + str(multi(num1, num2, integer)))
	elif action.lower() in ["/", "divide", "div"]:
		print(num1 + " / " + num2 + " = " + str(divide(num1, num2, integer)))
	elif action.lower() in ["pow", "power", "^"]:
		print(num1 + "^" + num2 + " = " + str(pow(num1, num2, integer)))
	elif action.lower() in ["%", "mod", "modulo"]:
		print(num1 + " % " + num2 + " = " + str(mod(num1, num2, integer)))
	else:
		print("Please enter valid values");
		calc(num1, num2, integer)
		return

def validateType(num1, num2):
	integer = True
	try:
		int(num1)
		int(num2)
	except Exception as e:
		try:
			float(num1)
			float(num2)
			integer = False
		except Exception as e:
			print("Please enter valid values!")
			return validateType(num1, num2)

	return integer

while True:
	num1 = 0;
	num2 = 0;

	num1 = input("Insert your fist number: ")
	if num1.lower() in ["q", "quit", "exit", "close", "end"]:
		print("Exit!")
		break

	bOneLiner = False
	opperator = ""
	for char in num1:
		if char in ["+", "-", "*", "/", "%", "^"]:
			opperator = char
			bOneLiner = True

	if bOneLiner:
		num2 = num1[num1.rfind(" ") + 1:]
		num1 = num1[:num1.find(" ")]
		integer = validateType(num1, num2)
		if opperator == "+":
			print(num1 + " + " + num2 + " = " + str(add(num1, num2, integer)))
		elif opperator == "-":
			print(num1 + " - " + num2 + " = " + str(subtract(num1, num2, integer)))
		elif opperator == "*":
			print(num1 + " x " + num2 + " = " + str(multi(num1, num2, integer)))
		elif opperator == "/":
			print(num1 + " / " + num2 + " = " + str(divide(num1, num2, integer)))
		elif opperator == "^":
			print(num1 + "^" + num2 + " = " + str(pow(num1, num2, integer)))
		else:
			print(num1 + " % " + num2 + " = " + str(mod(num1, num2, integer)))
		continue

	num2 = input("Insert your second number: ")
	if num2.lower() in ["q", "quit", "exit", "close", "end"]:
		print("Exit!")
		break

	integer = validateType(num1, num2)
	calc(num1, num2, integer)