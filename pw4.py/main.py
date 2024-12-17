# pw4/main.py

import curses
import numpy as np
from input import get_valid_input
from output import display_info
from domains.student import Student
from domains.course import Course

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