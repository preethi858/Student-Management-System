students=[]
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
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        department = input("Enter Department: ")
        cgpa = input("Enter CGPA: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "department": department,
            "cgpa": cgpa
            }

        students.append(student)

        print("Student Added Successfully!")

    

    elif choice == "2":
        print("View Students Selected")

    elif choice == "3":
        print("Search Student Selected")

    elif choice == "4":
        print("Update Student Selected")

    elif choice == "5":
        print("Delete Student Selected")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")