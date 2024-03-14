from domains.university import students, courses
import pickle

#input students and courses
def input_student(number_of_student):
    Students = []    
    with open('students.pickle', 'wb') as f:        
        for i in range(number_of_student):
            student = students(input("\nEnter the ID of student: "), input("Enter the name of student: "))
            student.date_of_birth(input("Enter the date of birth: "))
            Students.append(student)
            pickle.dump(student, f)
    return Students

def input_course(number_of_courses):
    Courses = []            
    with open('courses.pickle', 'wb') as f:
        for i in range(number_of_courses):
            course = courses(input("\nEnter the ID of course: "), input("Enter the name of course: "), int(input("Enter the credits of course: ")))
            Courses.append(course)
            pickle.dump(course, f)
    return Courses

def readPickle_student():
    Students = []
    with open('students.pickle', 'rb') as f:
        while True:
            try:
                student : students = pickle.load(f)
                Students.append(student)
            except EOFError:
                break
    return Students

def readPickle_course():
    Courses = []
    with open('courses.pickle', 'rb') as f:
        while True:
            try:
                course : courses = pickle.load(f)
                Courses.append(course)
            except EOFError:
                break
    return Courses

def count_array(array):
    count = 0 
    for arr in array:
        count += 1
    return count
        