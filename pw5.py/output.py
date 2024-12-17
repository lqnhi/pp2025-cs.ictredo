# pw5/output.py
import gzip
import pickle
import os

def decompress_data():
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as file:
            data = pickle.load(file)
            return data
    return None

def compress_data(students, courses, marks):
    with gzip.open('students.dat', 'wb') as file:
        data = {
            'students': students,
            'courses': courses,
            'marks': marks
        }
        pickle.dump(data, file)

def display_student_info(stdscr, student):
    """Display student info using curses"""
    stdscr.clear()
    stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa:.2f}\n")
    for course, marks in student.marks.items():
        stdscr.addstr(f"{course}: {marks}\n")
    stdscr.refresh()
    stdscr.getch()