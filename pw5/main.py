import os
import zipfile
import curses
from domains.school import School
from domains.student import Student
from domains.course import Course
import input as in_mod
import output as out_mod

DAT_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def compress_files():
    with zipfile.ZipFile(DAT_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in TXT_FILES:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)

def decompress_and_load(school):
    if os.path.exists(DAT_FILE):
        with zipfile.ZipFile(DAT_FILE, 'r') as zipf:
            zipf.extractall()

    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    school.students.append(Student(parts[0], parts[1], parts[2]))

    if os.path.exists("courses.txt"):
        with open("courses.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    school.courses.append(Course(parts[0], parts[1], int(parts[2])))

    if os.path.exists("marks.txt"):
        with open("marks.txt", "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                    if c_id not in school.marks:
                        school.marks[c_id] = {}
                    school.marks[c_id][s_id] = mark

def main(stdscr):
    school = School()
    decompress_and_load(school)

    while True:
        stdscr.clear()
        stdscr.addstr("--- USTH Student Mark Management (PW5) ---\n")
        stdscr.addstr("1. Input Students\n")
        stdscr.addstr("2. Input Courses\n")
        stdscr.addstr("3. Input Marks\n")
        stdscr.addstr("4. List Students (Sorted by GPA)\n")
        stdscr.addstr("5. Show Marks\n")
        stdscr.addstr("6. Quit & Save (Compress Data)\n")
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
            compress_files()
            break

if __name__ == "__main__":
    curses.wrapper(main)