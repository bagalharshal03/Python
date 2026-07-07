def attendance():

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    print("\nAttendance Status")
    print("1. Present")
    print("2. Absent")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
       print("\n----- Attendance Report -----")
       print("Student Name:", name)
       print("Roll Number:", roll)
       print("Status : Present")

    elif choice == "2":
       print("\n----- Attendance Report -----")
       print("Student Name:", name)
       print("Roll Number:", roll)
       print("Status : Absent")

    else:
        print("Invalid Choice!")
attendance()