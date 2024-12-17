# pw4/output.py
def display_info(self, stdscr):
        """Display student info using curses"""
        stdscr.clear()
        stdscr.addstr(f"ID: {self.student_id}, Name: {self.name}, GPA: {self.gpa:.2f}\n")
        for course, marks in self.marks.items():
            stdscr.addstr(f"{course}: {marks}\n")
        stdscr.refresh()
        stdscr.getch()  