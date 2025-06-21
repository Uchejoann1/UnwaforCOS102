import random

class Employee:
    def __init__(self,name):
        self.name = name
        self.employees = [
            "Mary Evans", "Eyo Ishan", "Durojaiye Dare", "Adams Ali", "Andrew Ugwu",
            "Stella Mankinde", "Jane Akibo", "Ago James", "Michell Taiwo", "Abraham Jones",
            "Nicole Anide", "Kosi Korso", "Adele Martins", "Emmanuel Ojo", "Ajayi Fatima"
        ]
        self.tasks = ["Loading", "Transporting", "Reviewing Orders", "Customer Service", "Delivering Items"]
        self.attendance = []

    def check_employee(self):
        return self.name in self.employees

    def take_attendance(self):
        if self.name not in self.attendance:
            self.attendance.append(self.name)
            return f"Attendance taken for {self.name}."
        else:
            return f"Attendance already taken for {self.name}."

    def assign_task(self):
        if self.check_employee():
            return random.choice(self.tasks)
        else: 
            return self.refuse_access()

    def refuse_access(self):
        return "Access Denied. You are not an employee."
    

name = Employee(input("Enter your name: ") ) 
if name.check_employee():
    print(f"Welcome, {name}!")
    print(name.take_attendance())
    print(f"Your assigned task is: {name.assign_task()}")
else: print(name.refuse_access())