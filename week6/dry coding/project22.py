def check_admission_requirements(jamb_score, department):
    if department.lower() == "computer science":
        return jamb_score >= 250
    elif department.lower() == "mass communication":
        return jamb_score >= 230
    return False

def check_credits(credits):
    key_subjects = ["English", "Mathematics"]
    for subject in key_subjects:
        if subject not in [credit["subject"] for credit in credits]:
            return False
    return len(credits) >= 5

def admit_candidate(name, jamb_score, credits, department, interview):
    if check_admission_requirements(jamb_score, department) and check_credits(credits) and interview:
        admitted.append({"name": name, "department": department})
        print(f"{name} has been admitted into {department}.")
    else:
        not_admitted.append({"name": name, "department": department})
        print(f"{name} has not been admitted into {department}.")

admitted = []
not_admitted = []

def main():
    while True:
        print("1. Admit a candidate")
        print("2. View admitted candidates")
        print("3. View not admitted candidates")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter candidate's name: ")
            jamb_score = int(input("Enter candidate's JAMB score: "))
            department = input("Enter candidate's department (Computer Science or Mass Communication): ")
            num_credits = int(input("Enter number of credits: "))
            credits = []
            for i in range(num_credits):
                subject = input(f"Enter subject {i+1}: ")
                grade = input(f"Enter grade for {subject}: ")
                credits.append({"subject": subject, "grade": grade})
            interview = input("Has the candidate passed the interview? (yes/no): ")
            interview = interview.lower() == "yes"
            admit_candidate(name, jamb_score, credits, department, interview)
        elif choice == "2":
            print("Admitted Candidates:")
            for candidate in admitted:
                print(f"Name: {candidate['name']}, Department: {candidate['department']}")
        elif choice == "3":
            print("Not Admitted Candidates:")
            for candidate in not_admitted:
                print(f"Name: {candidate['name']}, Department: {candidate['department']}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()