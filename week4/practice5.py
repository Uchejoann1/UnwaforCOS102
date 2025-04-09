def printinfo(name,age):
	print("Name: ",name)
	print("Age: ",age)
	return

printinfo(age=50, name ="miki")
"""line 6 uses key-word arguement so order doesn't matter age 
can come before name"""
printinfo(50,"miki")
"""line 8 uses required arguement so order matters name must 
come before age if you run this the result is:
name: 50
age:miki
:.order is important"""
printinfo("miki",50)