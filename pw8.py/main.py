# pw8/main.py
import curses
import os
from input import get_valid_input, write_students_to_file, write_courses_to_file, write_marks_to_file
from output import display_student_info, decompress_data, compress_data
from domains.student import Student
from domains.course import Course

def main(stdscr):
    
    data = decompress_data()
    if data:
        students = data['students']
        courses = data['courses']
        marks = data['marks']
    else:
        students = []
        courses = []
        marks = []

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

        write_students_to_file(students)
        write_courses_to_file(courses)
        write_marks_to_file(students, courses)

        compress_data(students, courses, marks)

    stdscr.addstr("Sorted students by GPA:\n")
    for student in students:
        display_student_info(stdscr, student)

    avg_gpa = sum(student.gpa for student in students) / len(students)
    stdscr.addstr(f"\nAverage GPA: {avg_gpa:.2f}\n")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)