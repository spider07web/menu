def add_student(students):
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    department = input("Enter department: ").strip()

    while True:
        cgpa_str = input("Enter CGPA: ").strip()
        try:
            cgpa = float(cgpa_str)
            # Optional sanity check for typical CGPA range (0 to 10)
            if cgpa < 0 or cgpa > 10:
                print("CGPA usually lies between 0 and 10. Please re-enter.")
                continue
            break
        except ValueError:
            print("Invalid CGPA. Please enter a number (e.g., 8.5).")

    student = {
        "name": name,
        "roll_no": roll_no,
        "department": department,
        "cgpa": cgpa,
    }
    students.append(student)
    print("Student added successfully!\n")


def display_students(students):
    if not students:
        print("\nNo student details available. Add a student first.\n")
        return

    print("\nStored Student Details:\n")
    print(f"{'S.No':<6}{'Name':<20}{'Roll No':<15}{'Department':<30}{'CGPA':<6}")
    print("-" * 80)

    for i, s in enumerate(students, start=1):
        print(
            f"{i:<6}{s['name'][:20]:<20}{s['roll_no'][:15]:<15}{s['department'][:30]:<30}{s['cgpa']:<6.2f}"
        )
    print("")


def main():
    students = []

    while True:
        print("student information system")
        print("1. add student details")
        print("2. display stored details")
        print("3. exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()

