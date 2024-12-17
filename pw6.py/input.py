# pw6/input.py
import os
import pickle
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

def write_students_to_file(students):
    """Serialize and save student data using pickle"""
    with open('students.pkl', 'wb') as file:
        pickle.dump(students, file)

def write_courses_to_file(courses):
    """Serialize and save course data using pickle"""
    with open('courses.pkl', 'wb') as file:
        pickle.dump(courses, file)

def write_marks_to_file(students, courses):
    """Serialize and save marks data using pickle"""
    with open('marks.pkl', 'wb') as file:
        pickle.dump({'students': students, 'courses': courses}, file)