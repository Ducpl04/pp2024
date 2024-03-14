from input import input_course, input_student
import output
import numpy as np

while True:
    number_of_student = int(input("Enter the number of students: "))
    if number_of_student > 0:
        break
    else: 
        print("Enter a positive interger!")

Students = input_student(number_of_student)

while True:
    number_of_courses = int(input("\nEnter the number of courses: "))
    if number_of_courses > 0:
        break
    else: 
        print("Enter a positive interger!")

Courses = input_course(number_of_courses)
    
while True:
    print("\nOptions:")
    print("1. List students")
    print("2. List courses")
    print("3. Enter marks for a course")
    print("4. Sorted GPA list")
    print("5. Show marks of a student")
    print("6. Quit")
    
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        output.student_list(Students)
    elif choice == "2":
        output.course_list(Courses)
    elif choice == "3":
        output.mark_list_input(Students, number_of_student, Courses)
    elif choice == "4":
        output.gpa(Students)
    elif choice == "5":
        output.show_mark(Students, number_of_courses, Courses)
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")