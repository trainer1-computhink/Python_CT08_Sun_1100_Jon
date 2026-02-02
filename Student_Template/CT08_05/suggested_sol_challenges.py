import json
import os


# ----------------------------
# (Given) Initial database
# ----------------------------
attendance_dict = {
    "john": [True, False, True],
    "jane": [True, True, True],
    "bob": [False, False, True],
    "alice": [True, True, False],
    "sam": [True, True, True],
    "eve": [False, True, False],
    "tom": [True, False, False],
    "daisy": [True, True, True],
    "mike": [False, False, False],
    "lily": [True, False, True]
}


# ============================================================
# Task 1 — Input Validation Helpers (Solution)
# ============================================================

def normalize_name(name: str) -> str:
    return name.strip().lower()


def ask_int_range(prompt, min_val, max_val):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            value = int(raw)
            if min_val <= value <= max_val:
                return value
        print(f"Invalid. Enter a number from {min_val} to {max_val}.")


def ask_float_range(prompt, min_val, max_val):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if min_val <= value <= max_val:
                return value
        except ValueError:
            pass
        print(f"Invalid. Enter a number from {min_val} to {max_val}.")


def ask_yes_no(prompt):
    # Accept y/n/yes/no/1/0 (case-insensitive)
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("y", "yes", "1"):
            return True
        if raw in ("n", "no", "0"):
            return False
        print("Invalid. Enter y/n (or yes/no, 1/0).")


# ============================================================
# Task 2 — Attendance Percentage (Loop + accumulator) (Solution)
# ============================================================

def attendance_percentage(student_name, class_attendance):
    student_name = normalize_name(student_name)
    if student_name not in class_attendance:
        print("Student name not found.")
        return None

    records = class_attendance[student_name]
    if len(records) == 0:
        # If a student has no records yet, define as 0%
        return 0.0

    present_count = 0
    for was_present in records:
        if was_present:
            present_count += 1

    pct = (present_count / len(records)) * 100
    return round(pct, 2)


def present_total(student_name, class_attendance)
    student_name = normalize_name(student_name)
    if student_name not in class_attendance:
        return None
    records = class_attendance[student_name]
    present_count = 0
    for was_present in records:
        if was_present:
            present_count += 1
    return present_count, len(records)


# ============================================================
# Task 2 — Take Attendance (validated y/n) (Solution)
# ============================================================

def take_attendance(class_attendance):
    print("Taking class attendance now...")

    # Optional: enforce consistent lesson lengths (all students same number of lessons)
    # For Sec 2/3, it’s okay to keep it simple and just append.

    for student in class_attendance:
        is_present = ask_yes_no(f"Is {student} present? (y/n): ")
        class_attendance[student].append(is_present)

    print("Attendance for class is taken.")
    return class_attendance


# ============================================================
# Task 2 — View Attendance (✅/❌) (Solution)
# ============================================================

def format_attendance_list(record):
    out = []
    for was_present in records:
        out.append("✅" if was_present else "❌")
    return " ".join(out)


def view_attendance(class_attendance):
    print("\n--- All Attendances ---")
    for student, records in class_attendance.items():
        print(f"{student:<10} : {format_attendance_list(records)}")


# ============================================================
# Task 3 — Class Statistics (Solution)
# ============================================================

def class_statistics(class_attendance):
    print("\n--- Class Statistics ---")

    if len(class_attendance) == 0:
        print("No students in the system.")
        return

    # Calculate each student's percentage once
    results = []
    for student in class_attendance:
        pct = attendance_percentage(student, class_attendance)
        # pct cannot be None because student exists
        results.append((student, pct))

    # Class average
    total_pct = 0.0
    for _, pct in results:
        total_pct += pct
    avg_pct = round(total_pct / len(results), 2)

    # Find highest and lowest
    highest = results[0][1]
    lowest = results[0][1]
    for _, pct in results:
        if pct > highest:
            highest = pct
        if pct < lowest:
            lowest = pct

    top_students = []
    bottom_students = []
    for student, pct in results:
        if pct == highest:
            top_students.append(student)
        if pct == lowest:
            bottom_students.append(student)

    print(f"Class average attendance: {avg_pct}%")
    print(f"Highest attendance ({highest}%): {', '.join(top_students)}")
    print(f"Lowest attendance ({lowest}%): {', '.join(bottom_students)}")


# ============================================================
# Task 4 — Add/Remove Student (Solution)
# ============================================================

def get_current_sessions_count(class_attendance):
    # Assume most students have the same number of lessons;
    # Use the max length as "current sessions"
    max_len = 0
    for records in class_attendance.values():
        if len(records) > max_len:
            max_len = len(records)
    return max_len


def add_student(class_attendance):
    print("\n--- Add Student ---")
    name = normalize_name(input("Enter new student name: "))

    if name == "":
        print("Invalid name.")
        return

    if name in class_attendance:
        print("Student already exists. No changes made.")
        return

    # Decide how to initialize:
    # Option A (recommended): match existing sessions with False placeholders (absent by default)
    sessions = get_current_sessions_count(class_attendance)
    class_attendance[name] = [False] * sessions

    print(f"Added {name}. (Initialized with {sessions} past session(s) as absent.)")


def remove_student(class_attendance):
    print("\n--- Remove Student ---")
    name = normalize_name(input("Enter student name to remove: "))

    if name not in class_attendance:
        print("Student not found.")
        return

    confirm = ask_yes_no(f"Confirm delete {name}? (y/n): ")
    if confirm:
        del class_attendance[name]
        print(f"{name} removed.")
    else:
        print("Deletion cancelled.")


# ============================================================
# Task 5 — Consecutive Absence Detection (Solution)
# ============================================================

def has_consecutive_absences(records, n)
    # Must use loop, no slicing shortcuts
    streak = 0
    for was_present in records:
        if was_present:
            streak = 0
        else:
            streak += 1
            if streak >= n:
                return True
    return False


def list_consecutive_absences(class_attendance, n):
    flagged = []
    for student, records in class_attendance.items():
        if has_consecutive_absences(records, n):
            flagged.append(student)
    return flagged


# ============================================================
# Task 3/4 — Low Attendance Notification (kept + improved) (Solution)
# ============================================================

def notify_low_attendance(class_attendance, threshold)
    warnings = []
    for student in class_attendance:
        pct = attendance_percentage(student, class_attendance)
        if pct is not None and pct < threshold:
            print(f"Warning: {student}'s attendance is {pct}%")
            warnings.append(student)
    return warnings


# ============================================================
# Task 6 — Save/Load JSON (Solution)
# ============================================================

DATA_FILE = "attendance.json"


def save_data(class_attendance, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(class_attendance, f, indent=4)
    print(f"Saved to {filename}.")


def load_data(filename):
    if not os.path.exists(filename):
        print(f"No save file found: {filename}")
        return None

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Basic validation: ensure lists are booleans
    for student, records in data.items():
        cleaned = []
        for x in records:
            cleaned.append(bool(x))
        data[student] = cleaned

    print(f"Loaded from {filename}.")
    return data


# ============================================================
# Menu System — integrates Tasks 1–6 (Solution)
# ============================================================

def menu_system(class_attendance):
    print("Welcome to the School Attendance System!")

    while True:
        print("\nSchool Attendance System")
        print("0. View All Attendances")
        print("1. Take Attendance")
        print("2. Calculate Attendance Percentage for a Student")
        print("3. Notify Low Attendance")
        print("4. View Class Statistics")
        print("5. Add Student")
        print("6. Remove Student")
        print("7. List Consecutive Absences")
        print("8. Save to File (JSON)")
        print("9. Load from File (JSON)")
        print("10. Exit Program")

        choice = ask_int_range("Enter your choice: ", 0, 10)

        if choice == 0:
            view_attendance(class_attendance)

        elif choice == 1:
            class_attendance = take_attendance(class_attendance)
            # Bonus: auto-save after taking attendance
            auto = ask_yes_no("Auto-save after attendance? (y/n): ")
            if auto:
                save_data(class_attendance)

        elif choice == 2:
            name = input("Enter the student's name: ")
            pct = attendance_percentage(name, class_attendance)
            if pct is not None:
                pt = present_total(name, class_attendance)
                present_count, total = pt
                name_norm = normalize_name(name)
                print(f"{name_norm}'s attendance: {present_count}/{total} = {pct}%")

        elif choice == 3:
            threshold = ask_float_range("Enter the attendance threshold (0–100): ", 0.0, 100.0)
            low_students = notify_low_attendance(class_attendance, threshold)
            print("Students with low attendance:", low_students)

        elif choice == 4:
            class_statistics(class_attendance)

        elif choice == 5:
            add_student(class_attendance)

        elif choice == 6:
            remove_student(class_attendance)

        elif choice == 7:
            n = ask_int_range("Flag students absent N times in a row. Enter N: ", 1, 50)
            flagged = list_consecutive_absences(class_attendance, n)
            print(f"Students with {n} consecutive absences:", flagged)

        elif choice == 8:
            save_data(class_attendance)

        elif choice == 9:
            loaded = load_data()
            if loaded is not None:
                class_attendance = loaded

        elif choice == 10:
            print("Exiting the program. Goodbye!")
            break


# ----------------------------
# Run program
# ----------------------------
menu_system(attendance_dict)


# ============================================================
# OPTIONAL EXTENSION (Not required) — Ideas only
# (A) Late state: store "P/A/L" instead of True/False
# (B) Export CSV report
# (C) Refactor into OOP
# ============================================================

