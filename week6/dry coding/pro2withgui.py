import tkinter as tk
from tkinter import messagebox

admitted_students = []
not_admitted_students = []

def check_jamb_score(score, department):
    if department == "Computer Science" and score >= 250:
        return True
    elif department == "Mass Communication" and score >= 230:
        return True
    else:
        return False

def check_credits(credits, department):
    if department == "Computer Science":
        required_subjects = ["English", "Mathematics", "Physics", "Chemistry", "F.Maths"]
    else:
        required_subjects = ["English", "Mathematics", "History", "Government", "Literature"]

    for subject in required_subjects:
        if subject not in credits:
            return False
    return True

def admit_student(name, score, credits, department, interview):
    if check_jamb_score(score, department) and check_credits(credits, department) and interview:
        admitted_students.append([name, department])
        result_label.config(text=f"{name} has been admitted into {department}.")
    else:
        not_admitted_students.append([name, department])
        result_label.config(text=f"{name} has not been admitted into {department}.")

def submit():
    name = name_entry.get()
    score = int(score_entry.get())
    department = department_var.get()
    credits = credits_entry.get().split(", ")
    interview = interview_var.get()

    admit_student(name, score, credits, department, interview)

def view_admitted():
    admitted_text.delete(1.0, tk.END)
    admitted_text.insert(tk.END, "Admitted Students:\n")
    for student in admitted_students:
        admitted_text.insert(tk.END, f"Name: {student[0]}, Department: {student[1]}\n")

def view_not_admitted():
    not_admitted_text.delete(1.0, tk.END)
    not_admitted_text.insert(tk.END, "Not Admitted Students:\n")
    for student in not_admitted_students:
        not_admitted_text.insert(tk.END, f"Name: {student[0]}, Department: {student[1]}\n")

root = tk.Tk()
root.title("Student Admission System")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

score_label = tk.Label(root, text="JAMB Score:")
score_label.pack()
score_entry = tk.Entry(root)
score_entry.pack()

department_var = tk.StringVar(root)
department_var.set("Computer Science")
department_option = tk.OptionMenu(root, department_var, "Computer Science", "Mass Communication")
department_option.pack()

credits_label = tk.Label(root, text="Credits (comma separated):")
credits_label.pack()
credits_entry = tk.Entry(root)
credits_entry.pack()

interview_var = tk.BooleanVar(root)
interview_checkbox = tk.Checkbutton(root, text="Passed Interview", variable=interview_var)
interview_checkbox.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

admitted_button = tk.Button(root, text="View Admitted Students", command=view_admitted)
admitted_button.pack()
admitted_text = tk.Text(root, height=10, width=40)
admitted_text.pack()

not_admitted_button = tk.Button(root, text="View Not Admitted Students", command=view_not_admitted)
not_admitted_button.pack()
not_admitted_text = tk.Text(root, height=10, width=40)
not_admitted_text.pack()

root.mainloop()