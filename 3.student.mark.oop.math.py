import math
import numpy as np
import curses

def get_valid_input(stdscr, prompt, input_type):
    """Get valid input from the user with curses interface"""
    curses.echo()
    stdscr.clear()  
    stdscr.addstr(prompt)
    stdscr.refresh()  
    user_input = stdscr.getstr().decode()
    while True:
        try:
            return input_type(user_input)
        except ValueError:
            stdscr.clear()
            stdscr.addstr("Invalid input. Please enter a valid value.\n")
            stdscr.addstr(prompt)
            stdscr.refresh()
            user_input = stdscr.getstr().decode()

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0

    def input_marks(self, course, marks):
        """Input marks and round down to 1 decimal place"""
        self.marks[course] = math.floor(marks * 10) / 10

    def calculate_gpa(self, courses):
        """Calculate GPA using numpy for weighted sum of credits and marks"""
        course_names = list(self.marks.keys())
        marks = np.array([self.marks[course] for course in course_names])
        credits = np.array([course.credits for course in courses if course.name in course_names])

        if credits.size > 0:  
            weighted_sum = np.sum(marks * credits)
            total_credits = np.sum(credits)
            self.gpa = weighted_sum / total_credits
        else:
            self.gpa = 0

    def display_info(self, stdscr):
        """Display student info using curses"""
        stdscr.clear()
        stdscr.addstr(f"ID: {self.student_id}, Name: {self.name}, GPA: {self.gpa:.2f}\n")
        for course, marks in self.marks.items():
            stdscr.addstr(f"{course}: {marks}\n")
        stdscr.refresh()
        stdscr.getch()  

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def add_student_marks(self, student, marks):
        student.input_marks(self.name, marks)


def main(stdscr):
    
    curses.curs_set(0)
    stdscr.clear()

   
    num_students = get_valid_input(stdscr, "Enter the number of students: ", int)
    students = [Student(get_valid_input(stdscr, f"Enter student {i+1} ID: ", str),
                        get_valid_input(stdscr, f"Enter student {i+1} name: ", str),
                        get_valid_input(stdscr, f"Enter student {i+1} DOB: ", str)) for i in range(num_students)]

  
    num_courses = get_valid_input(stdscr, "Enter the number of courses: ", int)
    courses = [Course(get_valid_input(stdscr, f"Enter course {i+1} ID: ", str),
                      get_valid_input(stdscr, f"Enter course {i+1} name: ", str),
                      get_valid_input(stdscr, f"Enter course {i+1} credits: ", int)) for i in range(num_courses)]

    
    for course in courses:
        for student in students:
            marks = get_valid_input(stdscr, f"Enter marks for {student.name} in {course.name}: ", float)
            course.add_student_marks(student, marks)

    for student in students:
        student.calculate_gpa(courses)

    students = sorted(students, key=lambda s: s.gpa, reverse=True)

    stdscr.clear()
    stdscr.addstr("Sorted students by GPA:\n")
    for student in students:
        student.display_info(stdscr)

    avg_gpa = np.mean([student.gpa for student in students])
    stdscr.clear()
    stdscr.addstr(f"Average GPA: {avg_gpa:.2f}\n")
    stdscr.refresh()
    stdscr.getch()  

if __name__ == "__main__":
    curses.wrapper(main)
    