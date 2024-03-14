import numpy as np
import math

class information:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def describe(self):
        print(f"\nID: {self.ID}")
        print (f"Name: {self.name}")
        
class students(information):
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.arr_mark = np.array([],'f')
        self.arr_credit = np.array([], 'i')
    def date_of_birth(self, DoB):
        self.__DoB = DoB
    def describe(self):
        super().describe()
        print(f"DoB: {self.__DoB}")
    def set_mark_function(self, mark, credits):
        self.arr_mark = np.append(self.arr_mark , mark)
        self.arr_credit = np.append(self.arr_credit , credits)
    def calculate_gpa(self):
        weighted_sum = self.arr_credit * self.arr_mark
        gpa = np.sum(weighted_sum) / np.sum(self.arr_credit)    
       #return round(gpa,1)     idk why mr.son ask me to use floor() function but okay
        return math.floor(gpa)

class courses(information):
    def __init__(self, ID, name, credit):
        super().__init__(ID, name)
        self.credit = credit
    def describe(self):
        super().describe()
        print(f"Credits: {self.credit}")
        
#input students and courses
while True:
    number_of_student = int(input("Enter the number of students: "))
    if number_of_student > 0:
        break
    else: 
        print("Enter a positive interger!")

Students = []            
for i in range(number_of_student):
    student = students(input("\nEnter the ID of student: "), input("Enter the name of student: "))
    student.date_of_birth(input("Enter the date of birth: "))
    Students.append(student)

while True:
    number_of_courses = int(input("\nEnter the number of courses: "))
    if number_of_courses > 0:
        break
    else: 
        print("Enter a positive interger!")

Courses = []            
for i in range(number_of_courses):
    course = courses(input("\nEnter the ID of course: "), input("Enter the name of course: "), int(input("Enter the credits of course: ")))
    Courses.append(course)

#functions
def student_list():
    print("Student list:")
    for student in Students:
        student.describe()

def gpa():
    sorted_students = sorted(Students, key=lambda student: student.calculate_gpa(), reverse=True)
    print("\nDescending GPA list: ")
    for student in sorted_students:
        print(f"{student.name}: {student.calculate_gpa()}")

def course_list(): 
    print("Course list:")
    for course in Courses:
        course.describe()

def show_mark():
    student_id = str(input("\nEnter the student ID you want to show mark: "))
    selected_student = next((student for student in Students if student.ID == student_id), None)
    if selected_student:   
        print(f"{selected_student.name}'s marks: ") 
        for i in range(number_of_courses):
            print(f"{Courses[i].name}: {selected_student.arr_mark[i]}")
    else:
        print("\nStudent not found.")

def mark_list_input():
    course_id = str(input("\nEnter the course ID for which you want to input marks: "))
    selected_course = next((course for course in Courses if course.ID == course_id), None)
    if selected_course:
        for i in range(number_of_student):
            mark = float(input(f"Enter the mark of {Students[i].name} for {selected_course.name}: "))
            Students[i].set_mark_function(mark, selected_course.credit)
    else:
        print("\nCourse not found.")

#design terminal
"""
def main(stdsrc):
    while True:
        stdsrc.clear()
        stdsrc.addstr(10, 10, "Options:")
        stdsrc.addstr(10, 20, "1. List students")
        stdsrc.addstr(10, 40, "2. List courses")
        stdsrc.addstr(10, 60, "3. Enter marks for a course")
        stdsrc.addstr(10, 80, "4. Sorted GPA list")
        stdsrc.addstr(10, 100, "5. Show marks of a student")
        stdsrc.addstr(10, 120, "6. Quit")
        stdsrc.refresh()

        choice = stdsrc.getch()
        if choice == ord('1'):
            student_list()
        elif choice == ord('2'):
            course_list()
        elif choice == ord('3'):
            mark_list_input()
        elif choice == ord('4'):
            gpa()
        elif choice == ord('5'):
            show_mark()
        elif choice == ord('6'):
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
#main
"""
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
        student_list()
    elif choice == "2":
        course_list()
    elif choice == "3":
        mark_list_input()
    elif choice == "4":
        gpa()
    elif choice == "5":
        show_mark()
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")