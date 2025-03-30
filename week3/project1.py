# Define the data
data = [
    ["Name", "Age", "Height", "Score"],
    ["Evelyn", 17, 5.5, 80],
    ["Jess", 16, 6.0, 85],
    ["Somto", 17, 5.4, 70],
    ["Edith", 18, 5.9, 60],
    ["Liza", 16, 5.6, 76],
    ["Madonna", 18, 5.5, 66],
    ["Waje", 17, 6.1, 87],
    ["Tola", 20, 6.0, 95],
    ["Aisha", 19, 5.7, 50],
    ["Latifa", 17, 5.5, 49]
]

# Print the header
print(f"| {' | '.join(data[0])} |")

# Print the separator
print("-" * 40)

# Print the data
for row in data[1:]:
    print(f"| {row[0]:<8} | {row[1]:<3} | {row[2]:<6} | {row[3]:<5} |")


data1 = [
['Chinedu', 19,5.7,74],
['Liam',16,5.9,87],
['Wale',18,5.8,75],
['Gbenga', 17,6.1,68],
['Abiola',20,5.9,66],
['Kola',19,5.5,78],
['Kunle',16,6.1,87],
['George',18,5.4,98],
['Thomas',17,5.8,54],
['Wesley',19,5.7,60]
]


# Print the header
print(f"| {' | '.join(data[0])} |")

# Print the separator
print("-" * 40)

# Print the data
for row in data1[0:]:
    print(f"| {row[0]:<8} | {row[1]:<3} | {row[2]:<6} | {row[3]:<5} |")