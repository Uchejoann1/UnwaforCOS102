s = "ABCDEFGHIJ"
part1 = s[2:8:2]
part2 = s[-1:-6:-2]
final = part1 + part2[::-1]
print("Final: " ,final)