class Candidate:
    def __init__(self, name, jamb_score, credits, department):
        self.name = name
        self.jamb_score = jamb_score
        self.credits = credits
        self.department = department

def check_admission_requirements(candidate):
    key_subjects = ["English", "Mathematics"]
    if candidate.department.lower() == "computer science":
        if candidate.jamb_score >= 250 and len(candidate.credits) >= 5:
            for subject in key_subjects:
                if subject not in [credit["subject"] for credit in candidate.credits]:
                    return False
            return True
    elif candidate.department.lower() == "mass communication":
        if candidate.jamb_score >= 230 and len(candidate.credits) >= 5:
            for subject in key_subjects:
                if subject not in [credit["subject"] for credit in candidate.credits]:
                    return False
            return True
    return False

def admit_candidate(candidate):
    if check_admission_requirements(candidate):
        admitted.append(candidate)
        print(f"{candidate.name} has been admitted into {candidate.department}.")
    else:
        not_admitted.append(candidate)
        print(f"{candidate.name} has not been admitted into {candidate.department}.")

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
            
            candidate = Candidate(name, jamb_score, credits, department)
            interview = input("Has the candidate passed the interview? (yes/no): ")
            if interview.lower() == "yes":
                admit_candidate(candidate)
            else:
                not_admitted.append(candidate)
                print(f"{candidate.name} has not been admitted into {candidate.department}.")
        elif choice == "2":
            print("Admitted Candidates:")
            for candidate in admitted:
                print(f"Name: {candidate.name}, Department: {candidate.department}")
        elif choice == "3":
            print("Not Admitted Candidates:")
            for candidate in not_admitted:
                print(f"Name: {candidate.name}, Department: {candidate.department}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()