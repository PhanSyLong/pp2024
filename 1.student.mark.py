def inputNumberOfStudents():
    numOfStudents = input("Enter number of students: ")
    return int(numOfStudents)

def inputOneStudent():
    student_id = input("id: ")
    name = input("name: ")
    dob = input("dob: ")
    student = {
        'id': student_id,
        'name': name,
        'dob': dob
    }
    return student

def inputNumberOfCourses():
    numOfCourses = input("Enter number of courses: ")
    return int(numOfCourses)

def inputOneCourse():
    course_id = input("id: ")
    name = input("name: ")
    course = {
        'id': course_id,
        'name': name
    }
    return course
//
def selectCoursesAndInputsMarks(courses, students):
    marks = {}
    for course in courses:
        print(f"Enter marks for students in course {course['name']}")
        marks[course['id']] = []
        for student in students:
            mark = float(input(f"Enter mark for student {student['name']}: "))
            studentMark = {
                'student_id': student['id'],
                'mark': mark
            }
            marks[course['id']].append(studentMark)
    return marks

num_of_students = inputNumberOfStudents()
students = [inputOneStudent() for _ in range(num_of_students)]

num_of_courses = inputNumberOfCourses()
courses = [inputOneCourse() for _ in range(num_of_courses)]

marks = selectCoursesAndInputsMarks(courses, students)

print("Collected data:")
print("Students:", students)
print("Courses:", courses)
print("Marks:", marks)
