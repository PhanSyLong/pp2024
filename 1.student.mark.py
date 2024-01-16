def inputNumberOfStudents():
    numOfStudent = input("Enter number of students:")
    return int(numOfStudent)

def inputOneStudent():
    id = input("id: ")
    name = input("name: ")
    dob = input("dob: ")
    student = {
        'id': id,
        'name': name,
        'dob' : dob
    }
    return student

def inputNumberOfCourses():
    numOfCourses = input("Enter number of courses:")
    return int(numOfCourses)

def inputOneStudent():
    id = input("id: ")
    name = input("name: ")
    courses = {
        'id': id,
        'name': name
    }
    return courses

def selectCoursesAndInputsMarks(course, marks, students):
    print(f"Enter marks for student in courses {course['name']}")
    marks = {}
    marks[course['id']] = []
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']}"))
        studentMark = {
            'studentid': student['id'],
            'mark': mark
        }
        marks[course['id']] += [studentMark]
