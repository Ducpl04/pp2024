from input import input_course, input_student, readPickle_course, readPickle_student, count_array
import output
import os
import gzip
#input

# Check if students.pickle and courses.pickle exists  //more easy
if os.path.exists('students.pickle') and os.path.exists('courses.pickle'):
    # Decompress and load data from it
    Students = readPickle_student()
    Courses = readPickle_course()

else:
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

#program
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
        output.mark_list_input(Students, count_array(Students), Courses)
    elif choice == "4":
        output.gpa(Students)
    elif choice == "5":
        output.show_mark(Students, count_array(Courses), Courses)
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")    

#Compression
    """
try:
    with open('students.pickle', 'rb') as f_in:
        with gzip.open('students.dat', 'wb') as f_out:
            f_out.writelines(f_in)
    with open('courses.pickle', 'rb') as f_in:
        with gzip.open('students.dat', 'wb') as f_out:
            f_out.writelines(f_in)
except IOError:
    print("Missing file.")            

    """