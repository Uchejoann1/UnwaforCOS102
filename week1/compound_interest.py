print("Compound Interest Calculator")
print(" ")
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))
n = float(input("Enter number of times interest applied per time period: "))

amount = principal * (1 + rate/n)**(n*time)

print("Amount: ", amount)
