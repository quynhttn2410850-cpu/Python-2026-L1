import curses
from domains.school import School
import input as in_mod
import output as out_mod

def main(stdscr):
    school = School()
    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Quit\n")
        stdscr.addstr("Select an option: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        curses.noecho()

        if choice == '1':
            in_mod.input_students(school, stdscr)
        elif choice == '2':
            in_mod.input_courses(school, stdscr)
        elif choice == '3':
            in_mod.input_marks(school, stdscr)
        elif choice == '4':
            out_mod.list_students(school, stdscr)
        elif choice == '5':
            out_mod.show_marks(school, stdscr)
        elif choice == '6':
            break

if __name__ == "__main__":
    curses.wrapper(main)