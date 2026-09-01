students = [
    {
        "id": 1,
        "name": "vamsi",
        "age":21,
        "branch":"csm" 
    }
]


def add_student():
    student_id = int(input("Enter Student Id: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    branch = input("Enter Student Branch: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("----------------")


def search_student():
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            print("Student Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            return

    print("Student not found.")


def update_student():
    student_id = int(input("Enter Student Id: "))

    for student in students:
        if student["id"] == student_id:

            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            branch = input("Enter Student Branch: ")

            student["name"] = name
            student["age"] = age
            student["branch"] = branch

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = int(input("Enter Student Id: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")

        # Here use the break statement to exit the loop and terminate the program execution.