total = 50; #global
def sum(arg1, arg2):
	# add both
	total = arg1 + arg2
	print("Inside the function local total: ",total)
	return total

#now you can call sum
sum (10,20)
print("Outside the function global total: ",total)