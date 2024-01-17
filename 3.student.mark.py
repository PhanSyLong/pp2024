class Person:
    def __init__(self, name):
        self._name = name

class Student(Person):
    def __init__(self, name, student_id, dob):
        super().__init__(name)
        self._id = student_id
        self._dob = dob

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
        self._id = course_id
        self._name = name

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
        self._students = []
        self._courses = []
        self._marks = {}

    def select_courses_and_input_marks(self):
        for course in self._courses:
            print(f"\nEnter marks for students in course {course._name}")
            self._marks[course._id] = []
            for student in self._students:
                mark = float(input(f"Enter mark for student {student._name}: "))
                student_mark = {
                    'student_id': student._id,
                    'mark': mark
                }
                self._marks[course._id].append(student_mark)

    def collect_data(self):
        num_of_students = Student.input_number_of_students()
        self._students = Student.input_students(num_of_students)

        num_of_courses = Course.input_number_of_courses()
        self._courses = Course.input_courses(num_of_courses)

        self.select_courses_and_input_marks()

    def display_collected_data(self):
        print("\nCollected data:")

        # Display Students
        print("\nStudents:")
        for student in self._students:
            print(f"  Student ID: {student._id}, Name: {student._name}, DoB: {student._dob}")

        # Display Courses
        print("\nCourses:")
        for course in self._courses:
            print(f"  Course ID: {course._id}, Name: {course._name}")

        # Display Marks
        print("\nMarks:")
        for course_id, student_marks in self._marks.items():
            for mark in student_marks:
                print(f"  Student ID: {mark['student_id']}, Course ID: {course_id}, Mark: {mark['mark']}")

        print("\n")

# Main
mark_collector = MarkCollector()
mark_collector.collect_data()
mark_collector.display_collected_data()
