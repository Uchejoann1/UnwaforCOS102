admitted_students = []
not_admitted_students = []

def check_jamb_score(score, department):
    if department == "Computer Science" and score >= 250:
        return True
    elif department == "Mass Communication" and score >= 230:
        return True
    else:
        return False

def check_credits(credits):
     if department == "Computer Science":
        required_subjects = ["English", "Mathematics", "Physics", "Chemistry", "F.Maths"]
        for subject in required_subjects:
            if subject not in credits:
                return False
        return True
     else:
        required_subjects =["English", 'Mathematics', 'History', 'Government', 'Literature'] 
        for subject in required_subjects:
            if subject not in credits:
                return False
        return True
    

def admit_student(name, score, credits, department, interview):
    if check_jamb_score(score, department) and check_credits(credits) and interview:
        admitted_students.append([name, department])
        print(f"{name} has been admitted into {department}.")
    else:
        not_admitted_students.append([name, department])
        print(f"{name} has not been admitted into {department}.")

while True:
    print("1. Admit a student")
    print("2. View admitted students")
    print("3. View not admitted students")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student's name: ")
        score = int(input("Enter student's JAMB score: "))
        department = input("Enter student's department (Computer Science or Mass Communication): ")
        if department == "Computer Science":
             print ("Required subjects = English, Mathematics, Physics, Chemistry, F.Maths")
             num_credits = int(input("Enter number of credits: "))
             credits = []
             for i in range(num_credits):
                subject = input(f"Enter subject {i+1}: ")
                credits.append(subject)
             interview = input("Has the student passed the interview? (yes/no): ")
             interview = interview.lower() == "yes"
             admit_student(name, score, credits, department, interview)
        else:
           print (" Required subjects = English, Mathematics, History, Government, Literature")
           num_credits = int(input("Enter number of credits: "))
           credits = []
           for i in range(num_credits):
               subject = input(f"Enter subject {i+1}: ")
               credits.append(subject)
           interview = input("Has the student passed the interview? (yes/no): ")
           interview = interview.lower() == "yes"
           admit_student(name, score, credits, department, interview)
        
    elif choice == "2":
        print("Admitted Students:")
        for student in admitted_students:
            print(f"Name: {student[0]}, Department: {student[1]}")
    elif choice == "3":
        print("Not Admitted Students:")
        for student in not_admitted_students:
            print(f"Name: {student[0]}, Department: {student[1]}")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")