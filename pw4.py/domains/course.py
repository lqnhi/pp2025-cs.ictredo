class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def add_student_marks(self, student, marks):
        student.input_marks(self.name, marks)
