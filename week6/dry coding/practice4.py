a = 10
b = 20
c = 30
while a<b<c:
    if a==10:
        a,b,c=b,c,a
    elif b==20:
        b,c=c,b
    else:
        a,c =c,a

print(f"a:{a}, b: {b},c: {c}")