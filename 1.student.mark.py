university = {
    "students":[], 
    "courses":[]
}

#funtions
def input_number_of_students():
    while True:
        num = int(input("Enter the number of students: "))
        if num > 0:
            return num
        else: print("Please enter a positive interger.")

def input_number_of_courses():
    while True:
        num = int(input("Enter the number of courses: "))
        if num > 0:
            return num
        else: print("Please enter a positive interger.")
        
def input_student_information():
    student_data = {}
    student_data["ID"] = str(input("\nEnter the ID of student: "))
    student_data["Name"] = str(input("Enter the name of student: "))
    student_data["DoB"] = str(input("Enter the date of birth of student: "))
    return student_data

def input_course_information():
    course_data = {}
    course_data["grades"]:[]
    course_data["ID"] = str(input("\nEnter the ID of course: "))
    course_data["Name"] = str(input("Enter the name of course: "))
    return course_data

def Students():
    print("\nStudent list: ")
    for students in university["students"]:
        print("\nID: " + students["ID"])
        print("Name: " + students["Name"])
        print("Dob: " + students["DoB"])
        
def Courses():
    print("\nCourse list: ")
    for courses in university["courses"]:
        print("\nID: " + courses["ID"])
        print("Name: " + courses["Name"])
    
def select_course_and_input_marks(university):
    course_id = str(input("Enter the course ID for which you want to input marks: "))
    selected_course = next((course for course in university["courses"] if course["ID"] == course_id), None)
    if selected_course:
        for student in university["students"]:
            while True:
                try:
                    mark = float(input(f"Enter marks for {student['Name']} in {selected_course['Name']}: "))
                    if mark < 0:
                        print("Grade can't be negative. Please enter again.")
                    else:
                        student.setdefault("marks", {})[course_id] = mark
                        break
                except ValueError:
                    print("Grade must be a number. Please enter again.")
    else:
        print("Course not found.")

def show_student_marks_for_course():
    student_id = str(input("Enter student ID to show marks: "))
    selected_student = next((student for student in university["students"] if student["ID"] == student_id), None)
    if selected_student:
        course_id = str(input("Enter course ID to show marks: "))
        marks = selected_student.get("marks", {}).get(course_id, None)
        if marks is not None:
            print(f"\nMarks for {selected_student['Name']} in {course_id}: {marks}")
        else:
            print(f"Marks not found.")
    else:
        print("Student not found.")

#input 
number_of_students =  input_number_of_students()
for i in range(number_of_students):
    student_data = input_student_information()
    university["students"].append(student_data)

number_of_courses = input_number_of_courses()
for i in range(number_of_courses):
    course_data = input_course_information()
    university["courses"].append(course_data)
    
#main
while True:
    print("\nOptions:")
    print("1. List Courses")
    print("2. List Students")
    print("3. Input Marks for a Course")
    print("4. Show Student Marks for a Course")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        Courses()
    elif choice == "2":
        Students()
    elif choice == "3":
        select_course_and_input_marks(university)
    elif choice == "4":
        show_student_marks_for_course()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")