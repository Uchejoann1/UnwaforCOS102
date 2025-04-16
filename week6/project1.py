import tkinter as tk

def calculate_cost():
    try:
        weight = float(weight_entry.get())
        location = location_var.get()
        if location == "Other":
            location = custom_location_entry.get()

        if location == "Ibeju-Lekki":
            cost = 5000 if weight >= 10 else 3500
        elif location == "Epe":
            cost = 10000 if weight >= 10 else 5000
        elif location == "Isolo":
            cost = 10000 if weight >= 5 else 4000
        elif location == "Surulere":
            cost = 8000 if weight >= 10 else 4000
        else:
            cost = 8000 if weight >= 10 else 4000  # default cost for custom locations

        result_label.config(text=f"Delivery Cost to {location}: N{cost}")
    except ValueError:
        result_label.config(text="Invalid weight. Please enter a number.")

root = tk.Tk()
root.title("Simi Services Delivery Cost Calculator")

location_var = tk.StringVar(root)
location_var.set("Choose a location")  # default value

location_label = tk.Label(root, text="Location:")
location_label.pack()
location_option = tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe", "Isolo", "Surulere", "Other")
location_option.pack()

custom_location_label = tk.Label(root, text="If 'Other', please specify:")
custom_location_label.pack()
custom_location_entry = tk.Entry(root)
custom_location_entry.pack()

weight_label = tk.Label(root, text="Package Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()