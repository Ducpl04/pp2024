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
        self.cou = {}
    def date_of_birth(self, DoB):
        self.__DoB = DoB
    def describe(self):
        super().describe()
        print(f"DoB: {self.__DoB}")
    def set_mark_function(self, ID, mark):
        self.cou[ID] = mark
      
class courses(information):
    def describe(self):
        return super().describe()
    
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
    course = courses(input("\nEnter the ID of course: "), input("Enter the name of course: "))
    Courses.append(course)

#functions
def student_list():
    print("Student list:")
    for student in Students:
        student.describe()

def course_list(): 
    print("Course list:")
    for course in Courses:
        course.describe()

def mark_list_input():
    course_id = str(input("\nEnter the course ID for which you want to input marks: "))
    selected_course = next((course for course in Courses if course.ID == course_id), None)
    if selected_course:
        for i in range(number_of_student):
            mark = float(input(f"Enter the mark of {Students[i].name} for {selected_course.name}: "))
            Students[i].set_mark_function(selected_course.ID, mark)
    else:
        print("\nCourse not found.")

def show_mark():
    student_id = str(input("\nEnter the student ID to show mark: "))
    selected_student = next((student for student in Students if student.ID == student_id), None)
    if selected_student:
        course_id = str(input("Enter the id of course you want to show mark: "))
        selected_course = next((course for course in Courses if course.ID == course_id), None)
        if selected_course:
            print(f"\nMark of {selected_student.name} for {selected_course.name}: {selected_student.cou[selected_course.ID]}")
        else: 
            print("\nMark not found.")
    else:
        print("\nStudent not found.")
#main
while True:
    print("\nOptions:")
    print("1. List students")
    print("2. List courses")
    print("3. Enter marks for a course")
    print("4. Show student Mark for a course")
    print("5. Quit")
    
    choice = input("\nEnter your choice (1-5): ")
    if choice == "1":
        student_list()
    elif choice == "2":
        course_list()
    elif choice == "3":
        mark_list_input()
    elif choice == "4":
        show_mark()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")