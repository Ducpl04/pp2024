#functions
def student_list(Students):
    print("Student list:")
    for student in Students:
        student.describe()

def gpa(Students):
    sorted_students = sorted(Students, key=lambda student: student.calculate_gpa(), reverse=True)
    print("\nDescending GPA list: ")
    for student in sorted_students:
        print(f"{student.name}: {student.calculate_gpa()}")

def course_list(Courses): 
    print("Course list:")
    for course in Courses:
        course.describe()

def show_mark(Students, number_of_courses, Courses):
    student_id = str(input("\nEnter the student ID you want to show mark: "))
    selected_student = next((student for student in Students if student.ID == student_id), None)
    if selected_student:   
        print(f"{selected_student.name}'s marks: ") 
        for i in range(number_of_courses):
            print(f"{Courses[i].name}: {selected_student.arr_mark[i]}")
    else:
        print("\nStudent not found.")

def mark_list_input(Students, number_of_student, Courses):
    course_id = str(input("\nEnter the course ID for which you want to input marks: "))
    selected_course = next((course for course in Courses if course.ID == course_id), None)
    if selected_course:
        for i in range(number_of_student):
            mark = float(input(f"Enter the mark of {Students[i].name} for {selected_course.name}: "))
            Students[i].set_mark_function(mark, selected_course.credit)
    else:
        print("\nCourse not found.")