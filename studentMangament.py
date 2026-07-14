students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[roll] = {
        "Name": name,
        "Marks": marks
    }

    print("Student Added Successfully!")

def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 35)

    for roll, details in students.items():
        print("Roll :", roll)
        print("Name :", details["Name"])
        print("Marks:", details["Marks"])
        print("-" * 35)

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Name :", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
    else:
        print("Student Not Found!")

def update_marks():
    roll = input("Enter Roll Number: ")

    if roll in students:
        marks = float(input("Enter New Marks: "))
        students[roll]["Marks"] = marks
        print("Marks Updated Successfully!")
    else:
        print("Student Not Found!")

def delete_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

def find_topper():
    if not students:
        print("No student records found.")
        return

    topper = max(students, key=lambda x: students[x]["Marks"])

    print("Topper Details")
    print("Roll :", topper)
    print("Name :", students[topper]["Name"])
    print("Marks:", students[topper]["Marks"])

def average_marks():
    if not students:
        print("No student records found.")
        return

    total = 0

    for details in students.values():
        total += details["Marks"]

    avg = total / len(students)
    print("Average Marks =", avg)

def count_students():
    print("Total Students =", len(students))

while True:
    print("\n******** STUDENT MANAGEMENT SYSTEM ********")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Find Topper")
    print("7. Find Average Marks")
    print("8. Count Students")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_marks()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        find_topper()

    elif choice == 7:
        average_marks()

    elif choice == 8:
        count_students()

    elif choice == 9:
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")