from tabulate import tabulate

#define the column headers
headers = ["Name","Age","Height","Score"]
#define your data
data = [
["Evelyn",17,5.5,80],
["Jess",16,6.0,85],
["Somto",17,5.4,70],
["Edith",18,5.9,60],
["Liza",16,5.6,76],
["Madonna",18,5.5,66],
["Waje",17,6.1,87],
["Tola",20,6.0,95],
["Aisha",19,5.7,50],
["Latifa",17,5.5,49]
]
# Print the data in tabular form
print (tabulate(data,headers,tablefmt="grid"))


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

# Print the data in tabular form
print (tabulate(data1,headers,tablefmt="grid"))


