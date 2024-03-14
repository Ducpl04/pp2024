from domains.university import students, courses

#input students and courses
def input_student(number_of_student):
    Students = []            
    for i in range(number_of_student):
        student = students(input("\nEnter the ID of student: "), input("Enter the name of student: "))
        student.date_of_birth(input("Enter the date of birth: "))
        Students.append(student)
    return Students

def input_course(number_of_courses):
    Courses = []            
    for i in range(number_of_courses):
        course = courses(input("\nEnter the ID of course: "), input("Enter the name of course: "), int(input("Enter the credits of course: ")))
        Courses.append(course)
    return Courses
