import tkinter as tk

def calculate_cost():
    try:
        weight = float(weight_entry.get())
        location = location_var.get()

        if location == "Ibeju-Lekki":
            if weight >= 10:
                cost = 5000
            else:
                cost = 3500
        elif location == "Epe":
            if weight >= 10:
                cost = 10000
            else:
                cost = 5000

        elif location == "Isolo":
            if weight >=5:
                cost = 10000
            else:
                cost = 4000
        else:
            if weight >= 10:
               cost = 8000
            else:
                cost = 4000

        result_label.config(text=f"Delivery Cost: N{cost}")
    except ValueError:
        result_label.config(text="Invalid weight. Please enter a number.")

root = tk.Tk()
root.title("Simi Services Delivery Cost Calculator")

location_var = tk.StringVar(root)
location_var.set("Choose a location")  # default value

location_label = tk.Label(root, text="Location:")
location_label.pack()
location_option = tk.Entry(root)
location_option = tk.OptionMenu(root, location_var, "Ibeju-Lekki", "Epe", "Isolo","Surulere")
location_option.pack()

weight_label = tk.Label(root, text="Package Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calculate Cost", command=calculate_cost)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()