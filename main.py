import json

try:
    with open("data.json", "r") as file:
        students = json.load(file)
except:
    students = []
def add_student():
    global students

    student_id = input("Enter Student ID: ")
    duplicate = False

    for student in students:
        if student["id"] == student_id:
            duplicate = True
            break

    if duplicate:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")

    if name.strip() == "":
        print("Name cannot be empty!")
        return

    try:
        age = int(input("Enter Age: "))

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    department = input("Enter Department: ")

    try:
        cgpa = float(input("Enter CGPA: "))

        if cgpa < 0 or cgpa > 10:
            print("CGPA should be between 0 and 10.")
            return

    except ValueError:
        print("Please enter a valid CGPA.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "cgpa": cgpa
    }

    students.append(student)

    with open("data.json", "w") as file:
        json.dump(students, file, indent=4)

    print("Student Added Successfully!")

while True:
    print("\n==============================")
    print(" Student Management System")
    print("==============================")
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
        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Details")
            print("-----------------------------")

            for student in students:
                print("ID :", student["id"])
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Department :", student["department"])
                print("CGPA :", student["cgpa"])
                print("-----------------------------")

    elif choice == "3":
        search_id = input("Enter Student ID to Search: ")

        found = False

        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found")
                print("-----------------------------")
                print("ID :", student["id"])
                print("Name :", student["name"])
                print("Age :", student["age"])
                print("Department :", student["department"])
                print("CGPA :", student["cgpa"])
                print("-----------------------------")
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "4":
        update_id = input("Enter Student ID to Update: ")

        found = False

        for student in students:
            if student["id"] == update_id:

                print("\nEnter New Details")

                student["name"] = input("Enter New Name: ")
                student["age"] = input("Enter New Age: ")
                student["department"] = input("Enter New Department: ")
                student["cgpa"] = input("Enter New CGPA: ")

                print("Student Updated Successfully!")
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "5":
        delete_id = input("Enter Student ID to Delete: ")

        found = False

        for student in students:
            if student["id"] == delete_id:
                students.remove(student)
                print("Student Deleted Successfully!")
                found = True
                break

        if found == False:
            print("Student Not Found")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")