# pw8/domains/student.py
import math
import numpy as np 

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