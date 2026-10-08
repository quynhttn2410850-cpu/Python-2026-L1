import numpy as np
import curses

def calculate_gpa_and_sort(school):
    for s in school.students:
        marks_list = []
        credits_list = []
        for c in school.courses:
            if c.id in school.marks and s.id in school.marks[c.id]:
                marks_list.append(school.marks[c.id][s.id])
                credits_list.append(c.credits)
        
        if marks_list:
            m_arr = np.array(marks_list)
            c_arr = np.array(credits_list)
            s.gpa = np.sum(m_arr * c_arr) / np.sum(c_arr)
        else:
            s.gpa = 0.0
            
    school.students.sort(key=lambda x: x.gpa, reverse=True)

def list_students(school, stdscr):
    stdscr.clear()
    calculate_gpa_and_sort(school)
    try:
        stdscr.addstr("--- Student List (Sorted by GPA) ---\n")
        for s in school.students:
            stdscr.addstr(f"ID: {s.id} | Name: {s.name} | DoB: {s.dob} | GPA: {s.gpa:.1f}\n")
    except curses.error:
        pass
    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()

def show_marks(school, stdscr):
    stdscr.clear()
    stdscr.addstr("Input course ID to show marks: ")
    curses.echo()
    c_id = stdscr.getstr().decode('utf-8')
    curses.noecho()

    if c_id in school.marks:
        stdscr.addstr(f"\n--- Marks for Course {c_id} ---\n")
        for s in school.students:
            mark = school.marks[c_id].get(s.id, 'No mark yet')
            stdscr.addstr(f"Student {s.name}: {mark}\n")
    else:
        stdscr.addstr("\nNo mark data for this course.\n")

    stdscr.addstr("\nPress any key to return...")
    stdscr.getch()