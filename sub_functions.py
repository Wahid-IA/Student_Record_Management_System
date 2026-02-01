from data_store import created_s, save_students
from student_info import Student_info
from input_validation import *

#To show all the previous stored records of Students
def show_on_start():
    print("\n======== Student List ========")
    for i, s in enumerate(created_s, start=1):
        print(f"\nStudent #{i}\n-----------\nName      : {s.student_name}\nRoll      : {s.student_roll}\nEmail     : {s.student_email}\nDepartment: {s.student_department}\n-----------")
    if not created_s:
        print("No current records.\n")
        return

#Creating new Student record    
def create_student():
    n= input_not_empty("==============================\nEnter Your Name: ")
    r= roll_input()
    e= input_not_empty("Enter Your Email: ")
    d= input_not_empty("Enter Your Department: ")

    student= Student_info(n,r,e,d)
    created_s.append(student)
    save_students(created_s)

    print("Student added successfully!")

#Showing all Student records
def show_student():
    if not created_s:
        print("No student records found.")
        return
    
    print("\n======= Student List =======")
    for i, s in enumerate(created_s, start=1):
        print(f"\nStudent #{i}\n-----------\nName      : {s.student_name}\nRoll      : {s.student_roll}\nEmail     : {s.student_email}\nDepartment: {s.student_department}\n-----------")

#Searching Student by name or email or roll
def student_search(name):
    found = False
    for s in created_s:
        if s.student_name == name or s.student_email == name or str(s.student_roll) == name:
            print(f"\nStudent {name} Found\n-----------\nName      : {s.student_name}\nRoll      : {s.student_roll}\nEmail     : {s.student_email}\nDepartment: {s.student_department}\n-----------")
            found = True
            break
    if not found:
        print("Student not found")

#Deleting Student record corresponding to the roll
def student_del(roll):
    for s in created_s:
        if s.student_roll == roll:
            print(f"\nStudent with roll {roll} Found\n-----------\nName      : {s.student_name}\nRoll      : {s.student_roll}\nEmail     : {s.student_email}\nDepartment: {s.student_department}\n-----------")

            choice = (input(f"Are you sure you want to delete {s.student_name}'s info?\nYes\nNo\n"))

            if choice.lower() == "yes":
                created_s.remove(s)
                save_students(created_s)
                print("Student deleted.")
            elif choice.lower() == "no":
                print("Deletion Canceled")
            else:
                print("Invalid input")
            return
        
    print("Student not found.")

#Checking for duplicate Roll input
def roll_input():
    while True:
        r= input_int("Enter Your Roll: ")
        dup=False

        for s in created_s:
            if s.student_roll == r:
                print("Error: Roll number already exists for another student.")
                dup= True
                break
        
        if not dup:
            return r