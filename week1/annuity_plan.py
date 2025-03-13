print("Annuity Plan Calculator")
print(" ")
PMT = float(input("Enter Payment Amount: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))
n = float(input("Enter number of times interest applied per time period: "))
if rate == 0:
 amount= PMT * time * n
else:
 amount = PMT * ((1 + rate/n)**(n*time) - 1) / (rate/n)

print("Amount: ", amount)
