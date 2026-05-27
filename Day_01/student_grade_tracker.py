students = {}


def add_student(name, grade):
    students[name] = grade
    print(f"{name} added successfully")


def update_grade(name, grade):

    if name in students:
        students[name] = grade
        print(f"{name}'s grade updated")

    else:
        print("Student not found")


def get_average():

    if len(students) == 0:
        print("No students available")
        return

    total = sum(students.values())
    average = total / len(students)

    print("Average Grade:", average)


def list_students():

    if len(students) == 0:
        print("No students available")

    else:
        print("\nStudent Records:")

        for name, grade in students.items():
            print(name, ":", grade)


while True:

    print("\n--- Student Grade Tracker ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Get Average")
    print("4. List All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))

        add_student(name, grade)

    elif choice == "2":

        name = input("Enter student name: ")
        grade = float(input("Enter new grade: "))

        update_grade(name, grade)

    elif choice == "3":

        get_average()

    elif choice == "4":

        list_students()

    elif choice == "5":

        print("Exiting program...")
        break

    else:
        print("Invalid choice")
        