class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id, dob):
        super().__init__(name)
        self.id = student_id
        self.dob = dob

    @staticmethod
    def input_number_of_students():
        num_of_students = input("Enter number of students: ")
        return int(num_of_students)

    @staticmethod
    def input_one_student():
        student_id = input("id: ")
        name = input("name: ")
        dob = input("dob: ")
        return Student(name, student_id, dob)

    @staticmethod
    def input_students(num_of_students):
        students = []
        for i in range(1, num_of_students + 1):
            print(f"\nEnter information for student {i}:")
            student = Student.input_one_student()
            students.append(student)
        return students

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name

    @staticmethod
    def input_number_of_courses():
        num_of_courses = input("Enter number of courses: ")
        return int(num_of_courses)

    @staticmethod
    def input_one_course():
        course_id = input("id: ")
        name = input("name: ")
        return Course(course_id, name)

    @staticmethod
    def input_courses(num_of_courses):
        courses = []
        for i in range(1, num_of_courses + 1):
            print(f"\nEnter information for course {i}:")
            course = Course.input_one_course()
            courses.append(course)
        return courses
    
class MarkCollector:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def select_courses_and_input_marks(self):
        for course in self.courses:
            print(f"\nEnter marks for students in course {course.name}")
            self.marks[course.id] = []
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name}: "))
                student_mark = {
                    'student_id': student.id,
                    'mark': mark
                }
                self.marks[course.id].append(student_mark)

    def collect_data(self):
        num_of_students = Student.input_number_of_students()
        self.students = Student.input_students(num_of_students)

        num_of_courses = Course.input_number_of_courses()
        self.courses = Course.input_courses(num_of_courses)

        self.select_courses_and_input_marks()

    def display_collected_data(self):
        print("\nCollected data:")
        print("\nStudents:", [vars(student) for student in self.students])
        print("\nCourses:", [vars(course) for course in self.courses])
        print("\nMarks:", self.marks)

# Main
mark_collector = MarkCollector()
mark_collector.collect_data()
mark_collector.display_collected_data()
