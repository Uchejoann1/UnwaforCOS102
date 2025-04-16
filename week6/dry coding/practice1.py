def combine(a,b=[]):
    b.append(a)
    return b

list1 = combine(1)
print(list1)
list2 = combine(2)
print(list1)
print(list2)
