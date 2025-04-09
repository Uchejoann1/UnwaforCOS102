import math
import cmath

def Cubic():
    A = float(input("Enter your first term: "))
    B = float(input("Enter your second term: "))
    C = float(input("Enter your third term: "))
    D = float(input("Enter your fourth term: "))
    
    # Calculate the coefficients for the cubic formula
    Q = (3*A*C - B**2) / (9*A**2)
    R = (9*A*B*C - 27*A**2*D - 2*B**3) / (54*A**3)
    D_ = Q**3 + R**2
    
    if D_ > 0:
        # One real root
        S = (R + math.sqrt(D_)) ** (1/3)
        T = (R - math.sqrt(D_)) ** (1/3)
        root1 = S + T - B / (3*A)
        print("One real root: ", root1)
    elif D_ == 0:
        # Three real roots
        S = R ** (1/3)
        root1 = 2*S - B / (3*A)
        root2 = -S - B / (3*A)
        print("Three real roots: ", root1, root2, root2)
    else:
        # Three real roots
        theta = math.acos(R / math.sqrt(-Q**3))
        root1 = 2*math.sqrt(-Q)*math.cos(theta/3) - B / (3*A)
        root2 = 2*math.sqrt(-Q)*math.cos((theta+2*math.pi)/3) - B / (3*A)
        root3 = 2*math.sqrt(-Q)*math.cos((theta+4*math.pi)/3) - B / (3*A)
        print("Three real roots: ", root1, root2, root3)

def Quartic():
    A = float(input("Enter your first term: "))
    B = float(input("Enter your second term: "))
    C = float(input("Enter your third term: "))
    D = float(input("Enter your fourth term: "))
    E = float(input("Enter your fifth term: "))
    
    # Calculate the coefficients for the quartic formula
    a = B/A
    b = C/A
    c = D/A
    d = E/A
    
    # Calculate the resolvent cubic coefficients
    P = -b**2/12 + c/2
    Q = b**3/108 - b*c/8 + d/4
    R = -Q/2 + math.sqrt(Q**2/4 + P**3/27)
    S = R ** (1/3)
    T = Q / (2*S) + S
    
    # Calculate the roots
    root1 = -b/4 + (T + cmath.sqrt(T**2 - 4*P)) / 2
    root2 = -b/4 + (T - cmath.sqrt(T**2 - 4*P)) / 2
    root3 = -b/4 + (-T + cmath.sqrt(T**2 - 4*P)) / 2
    root4 = -b/4 + (-T - cmath.sqrt(T**2 - 4*P)) / 2
    
    print("Four roots: ", root1, root2, root3, root4)

def Quadratic():
    A = float(input("Enter your first term: "))
    B = float(input("Enter your second term: "))
    C = float(input("Enter your third term: "))
    
    # Calculate the discriminant
    D = B**2 - 4*A*C
    
    if D > 0:
        # Two distinct real roots
        root1 = (-B + math.sqrt(D)) / (2*A)
        root2 = (-B - math.sqrt(D)) / (2*A)
        print("Two distinct real roots: ", root1, root2)
    elif D == 0:
        # One repeated real root
        root = -B / (2*A)
        print("One repeated real root: ", root)
    else:
        # Two complex roots
        real_part = -B / (2*A)
        imaginary_part = math.sqrt(-D) / (2*A)
        root1 = f"{real_part} + {imaginary_part}i"
        root2 = f"{real_part} - {imaginary_part}i"
        print("Two complex roots: ", root1, root2)

print("1 for Quadratic")
print("2 for Quartic")
print("3 for Cubic")
Z = int(input("Enter the operation to perform: "))

if Z == 1:
    Quadratic()
elif Z == 2:
    Quartic()
elif Z == 3:
    Cubic()
else: print("That is not a valid input")
