# pw4/input.py
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