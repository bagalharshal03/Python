marks_list =[]

while True:
    print("--- Student Marks Menu ---")
    print("1. Add a mark (append)")
    print("2. Insert a mark at a specific position")
    print("3. Delete a mark (Remove)")
    print("4. Sort all marks")
    print("5. Display all mark")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        new_mark = int(input("Enter mark to add: "))
        marks_list.append(new_mark)
        print(f"{new_mark} added to the end.")

    elif choice == '2':
        pos = int(input("Enter index position: "))
        new_mark = int(input("Enter mark to insert: "))
        
        if pos <= len(marks_list):
            marks_list.insert(pos, new_mark)
            print(f"{new_mark} inserted at position {pos}.")

        else:
            print("Invalid Position!")

    elif choice == '3':
        del_mark = int(input("Enter mark value to remove: "))
        if del_mark in marks_list:
            marks_list.remove(del_mark)
            print(f"{del_mark} removed successfully.")
        else:
            print("Mark not found in the list!")

    elif choice == '4':
        marks_list.sort()
        print("Marks sortedin accending order:", marks_list)

    elif choice == '5':
        print("Current Marks List:", marks_list)

    elif choice == '6':
        print("Exitingm program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a number from 1 to 6.")
        
