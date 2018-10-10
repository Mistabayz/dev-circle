#This will print factorial of a given number
#Author : pramodbharti

def factorial(n):
	if( n == 1):
		return n
	else:
		return n*factorial(n-1)

number = int(input("Enter any +ve number: "))
if number < 0:
	print("Factorial does not exist for negative numbers")
elif number == 0:
	print("The factorial of 0 is 1")
else:
	print("The factorial of",number,"is",factorial(number))
