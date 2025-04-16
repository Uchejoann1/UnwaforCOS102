w = "GO!"
nw = w*3
slice1 = nw[::2]
slice2 = nw[1::2]
R = slice1 + slice2[::-1]
print("Result:", R)