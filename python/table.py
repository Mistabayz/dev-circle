# This will print table of any given number
# Author : pramodbharti
def print_table(x):
	for i in range(1,11):
    		print(x,"x",i,"=",x*i)
print_table(int(input("Enter any number: ")))
