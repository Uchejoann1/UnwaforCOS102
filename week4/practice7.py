#variable arguments
def printinfo(arg1,*vartuple):
	print("Output is: ")
	print(arg1)
	for var in vartuple:
		print(var)

printinfo(10)
printinfo(70,60,50)

"""regular expression pattern 
* infront of a variable means 0 or more
+ infront of a variable means 1 or more"""

def add(*vartuple):
	total =0
	for var in vartuple:
		total += var
	return total

sum_of_numbers = add(3,5,9)
print(sum_of_numbers)