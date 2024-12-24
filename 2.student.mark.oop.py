
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  
    
 
    def input_marks(self, course, marks):
        self.marks[course] = marks
    
  
    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Date of Birth: {self.dob}")
        for course, marks in self.marks.items():
            print(f"{course}: {marks}")

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []  

  
    def add_student(self, student):
        self.students.append(student)
    
    def display_course_info(self):
        print(f"Course ID: {self.course_id}, Course Name: {self.name}")
        print("Enrolled Students:")
        for student in self.students:
            student.display_info()


def main():
    
    num_students = int(input("Enter the number of students in the class: "))
    students = []
    
   
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth: ")
        student = Student(student_id, name, dob)
        students.append(student)
    
   
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    
    
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course = Course(course_id, course_name)
        courses.append(course)
    
    
    for course in courses:
        print(f"Enter marks for course {course.name}")
        for student in students:
            marks = float(input(f"Enter marks for {student.name}: "))
            student.input_marks(course.name, marks)
            course.add_student(student)
    
   
    print("\nList of Students and their marks:")
    for student in students:
        student.display_info()
    
    print("\nList of Courses and their enrolled students:")
    for course in courses:
        course.display_course_info()


if __name__ == "__main__":
    main()