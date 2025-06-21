import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load the employee dataset
try:
    employee_df = pd.read_csv("GIG-logistics.csv")
except FileNotFoundError:
    messagebox.showerror("File Error", "Could not find GIG-logistics.csv")
    exit()

# Function to validate the employee
def verify_employee():
    name = name_entry.get().strip().title()
    dept = dept_entry.get().strip().title()

    match = employee_df[(employee_df['Name'].str.title() == name) & 
                        (employee_df['Department'].str.title() == dept)]

    if not match.empty:
        # Get other employees in the same department
        colleagues = employee_df[(employee_df['Department'].str.title() == dept) &
                                 (employee_df['Name'].str.title() != name)]

        welcome_msg = f"Welcome, {name} from {dept} Department!"
        if not colleagues.empty:
            colleague_list = ", ".join(colleagues['Name'].values)
            welcome_msg += f"\nYour colleagues are: {colleague_list}"
        else:
            welcome_msg += "\nYou are the only one in this department."

        messagebox.showinfo("Employee Verified", welcome_msg)
    else:
        messagebox.showwarning("Not Found", f"Sorry, {name} from {dept} is not found in our records.")

# Set up the GUI
root = tk.Tk()
root.title("GIG Logistics - Employee Checker")
root.geometry("400x250")

tk.Label(root, text="Employee Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Department:").pack(pady=5)
dept_entry = tk.Entry(root, width=40)
dept_entry.pack()

tk.Button(root, text="Verify", command=verify_employee).pack(pady=20)

root.mainloop()