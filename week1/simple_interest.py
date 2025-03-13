print("Simple Interest Calculator")
print(" ")

P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
A = P + SI

print("Amount: ", A)

print("simple_interest:", SI)