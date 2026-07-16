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
        print("Add Student Selected")

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