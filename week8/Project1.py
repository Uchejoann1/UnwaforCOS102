import pandas as pd

# Load the datasets (update the file paths with the actual paths of the downloaded datasets)
top_apps = pd.read_csv('path_to_top_apps_dataset.csv')
crypto_ai = pd.read_csv('path_to_crypto_ai_dataset.csv')
programming_trends = pd.read_csv('path_to_programming_trends_dataset.csv')

# Task 1: Display the first 7 rows of each dataset
print("First 7 rows of Top Apps dataset:")
print(top_apps.head(7))
print("\nFirst 7 rows of Cryptocurrency AI dataset:")
print(crypto_ai.head(7))
print("\nFirst 7 rows of Programming Trends dataset:")
print(programming_trends.head(7))

# Task 2: Select the first 3 columns of each dataset
print("\nFirst 3 columns of Top Apps dataset:")
print(top_apps.iloc[:, :3])
print("\nFirst 3 columns of Cryptocurrency AI dataset:")
print(crypto_ai.iloc[:, :3])
print("\nFirst 3 columns of Programming Trends dataset:")
print(programming_trends.iloc[:, :3])

# Task 3: Display only one row and header of each dataset
print("\nOne row and header of Top Apps dataset:")
print(top_apps.head(1))
print("\nOne row and header of Cryptocurrency AI dataset:")
print(crypto_ai.head(1))
print("\nOne row and header of Programming Trends dataset:")
print(programming_trends.head(1))