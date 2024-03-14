from domains.university import students, courses

#input students and courses
def input_student(number_of_student):
    Students = []    
    with open('students.txt', 'w') as f:        
        for i in range(number_of_student):
            student = students(input("\nEnter the ID of student: "), input("Enter the name of student: "))
            student.date_of_birth(input("Enter the date of birth: "))
            Students.append(student)
            f.write(f"{student.ID} \n{student.name} \n{student.DoB}")   
            f.write("\n") 
    return Students

def input_course(number_of_courses):
    Courses = []            
    with open('courses.txt', 'w') as f:
        for i in range(number_of_courses):
            course = courses(input("\nEnter the ID of course: "), input("Enter the name of course: "), int(input("Enter the credits of course: ")))
            Courses.append(course)
            f.write(f"ID: {course.ID} |Name: {course.name} |Credits: {course.credit}")
            f.write("\n")
    return Courses

def read_Student_Data():
    Students = []
    try:
        with open('students.dat', 'rb') as f:
            while True:
                if not f.readline():
                    break
                id = f.readline().decode()
                name = f.readline().decode()
                student = students(id, name)
                student.date_of_birth(f.readline().decode())
                Students.append(student)
    except IOError:
        print("Error file.")
    return Students