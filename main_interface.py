from sub_functions import *

#Showing starting comments and all previously kept Student records
print("Welcome to the Student Record Management System! \nLoading student records from stored_students.json... Done!")
show_on_start()

#Main Menu
while True:
    print("\n============ MENU ============\n1. Add Student\n2. View Students\n3. Search Student\n4. Remove Student\n5. Exit\n==============================")

    choice = (input("Enter your Choice: "))

    #Add Student
    if choice == '1':
        create_student()

    #Show Student record
    elif choice == '2':
        show_student()

    #Search Student
    elif choice == '3':
        search_input= input_not_empty("Student to Search: ")
        student_search(search_input)

    #Delete Student
    elif choice == '4':
        del_roll= input_int("Student Roll to Delete: ")
        student_del(del_roll)

    #Exit        
    elif choice == '5':
        print("\nThank you for using the Student Record Management System. Goodbye!\n")
        break

    #Invalid
    else:
        print("Invalid Input. Try again.")
