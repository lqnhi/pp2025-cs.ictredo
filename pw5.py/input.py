# pw5/input.py
import curses
import os

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

def write_students_to_file(students):
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f"{student.student_id},{student.name},{student.dob},{student.gpa}\n")

def write_courses_to_file(courses):
    with open('courses.txt', 'w') as file:
        for course in courses:
            file.write(f"{course.course_id},{course.name},{course.credits}\n")

def write_marks_to_file(students, courses):
    with open('marks.txt', 'w') as file:
        for student in students:
            for course in courses:
                marks = student.marks.get(course.name, 'N/A')
                file.write(f"{student.student_id},{course.course_id},{marks}\n")