# pw8/output.py
import gzip
import pickle
import os
import threading

def decompress_data():
    """Decompress and load data from the students.dat file"""
    if os.path.exists('students.dat'):
        with gzip.open('students.dat', 'rb') as file:
            data = pickle.load(file)
            return data
    return None

def compress_data(students, courses, marks):
    """Serialize and compress data into students.dat using a background thread."""
    def background_compression():
        with gzip.open('students.dat', 'wb') as file:
            data = {
                'students': students,
                'courses': courses,
                'marks': marks
            }
            pickle.dump(data, file)
        print("Data saved in the background.")

    compression_thread = threading.Thread(target=background_compression)
    compression_thread.start()

def display_student_info(stdscr, student):
    """Display student info using curses"""
    stdscr.clear()
    stdscr.addstr(f"ID: {student.student_id}, Name: {student.name}, GPA: {student.gpa:.2f}\n")
    for course, marks in student.marks.items():
        stdscr.addstr(f"{course}: {marks}\n")
    stdscr.refresh()
    stdscr.getch()