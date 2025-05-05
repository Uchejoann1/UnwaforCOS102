import pandas as pd
# Data for Cadbury Nigeria Plc products and brands
data = {
    "Segment": [
        "Refreshment Beverages", "Refreshment Beverages",
        "Confectionery", "Confectionery", "Confectionery",
        "Intermediate Cocoa Products", "Intermediate Cocoa Products", 
        "Intermediate Cocoa Products", "Intermediate Cocoa Products"
    ],
    "Product": [
        "Bournvita", "Hot Chocolate",
        "Tom Tom", "Buttermint", "Tom Tom Strawberry",
        "Cocoa Powder", "Cocoa Butter", "Cocoa Liquor", "Cocoa Cake"
    ],
    "Brand": [
        "CADBURY BOURNVITA", "CADBURY 3-in-1 HOT CHOCOLATE",
        "TOMTOM CLASSIC", "BUTTERMINT", "TOMTOM STRAWBERRY",
        "COCOA POWDER", "COCOA BUTTER", "COCOA LIQUOR", "COCOA CAKE"
    ],
    "Export": [
        "-", "-",
          "-", "-", "-",
          "International", "International", "International", "Local"
          ]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("cadbury_market.csv")

print(f"Data has been saved to cadbury_market.csv")
print("DataFrame:\n", df)
