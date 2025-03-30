import sympy as sp
def Cubic():
	A = float (input("Enter your first term: "))
	B = float(input("Enter your second term: "))
	C = float(input("Enter your third term: "))
	D = float(input("Enter your fourth term: "))
	x = sp.symbols('x')
	equation = A*x**3  + B *x**2 + C*x + D
	print("Equation: ", equation)
	solutions = sp.solve(equation,x)
	print("solutions:",solutions)

def Quartic():
	A = float(input("Enter your first term: "))
	B = float(input("Enter your second term: "))
	C = float(input("Enter your third term: "))
	D =float(input("Enter your fourth term: "))
	E = float(input("Enter your last term: "))
	x = sp.symbols('x')
	equation = A*x**4 + B*x**3 + C*x**2 +D*x + E
	print("Equation: ", equation)
	solutions = sp.solve(equation,x)
	print("solutions:",solutions)

def Quadratic():
	A = float(input("Enter your first term: "))
	B = float(input("Enter your second term: "))
	C = float(input("Enter your third term: "))
	x = sp.symbols('x')
	equation =  A*x**2 + B*x + C
	print("Equation: ", equation)
	solutions = sp.solve(equation,x)
	print("solutions:",solutions)



print("1 for Quadratic")
print("2 for Quartic")
print("3 for Cubic")
Z = int(input("Enter the operation to perform: "))

if Z== 1:
	Quadratic()
elif Z== 2:
	Quartic()
elif Z ==3:
	Cubic()
else: print("That is not a valid input")


