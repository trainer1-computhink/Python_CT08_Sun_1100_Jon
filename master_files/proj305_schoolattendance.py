#------------------------------------------------------------
# Exercise 16: School Attendance System
# Build a School Attendance System
# Use Python to design a system that:
# 1. Updates attendance for each student.
# 2. Calculates attendance percentages.
# 3. Identifies and notifies students with low attendance.

# 1. create the initial dictionary database
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

# 2. Updates attendance for each student.
def take_attendance(class_attendance):
    print("Taking Class attendance now...")
    # class_attendance is a dictionary variable
    for student, attendance in class_attendance.items():
        while True:
            attendance = input("Is {} present? y/ n: ".format(student)).lower()

            if attendance == "y":
                class_attendance[student].append(True)
                break
            elif attendance == "n":
                class_attendance[student].append(False)
                break
            else:
                print("Invalid. only y or n.")
    print("Attendance for Class is taken.")
    return class_attendance

# print("Welcome to the School Attendance System.")
# attendance_dict = take_attendance(attendance_dict)
# print(attendance_dict)

# 3. calculate the percentage attendance for a student
def attendance_percentage(student_name, class_attendance):
    if student_name in class_attendance:
        list_attendance = class_attendance[student_name]
        count_present = 0
        for a in list_attendance:
            if a:
                count_present += 1
        
        attendance_pct = (count_present / len(list_attendance))*100
        return round(attendance_pct, 2)
    else:
        print("Student name not found.")
        return None

# student = input("Check attendance for: ").lower()
# att_pct = attendance_percentage(student, attendance_dict)
# print("{}'s attendance is {}%".format(student, att_pct))


#4. Identify students will low attendance for further action
def notify_low_attendance(class_attendance, threshold):
    list_warning = []
    for student, attendance in class_attendance.items():
        att_pct = attendance_percentage(student, class_attendance)
        if att_pct < threshold:
            print("Warning: {}'s attendance is {}%".format(student, att_pct))
            list_warning.append(student)
        
    return list_warning

# list_students_warning = notify_low_attendance(attendance_dict, 75)
# print("List of students to send warning: {}".format(list_students_warning))

# 6. print out each student's attendance
def view_attendance(class_attendance):
    for student, attendance in class_attendance.items():
        print("{} : {}".format(student, attendance))

# 5. Menu system for School Attendance System
def menu_system(class_attendance):
    print("Welcome to the School Attendance System!")
    while True:
        print("\nSchool Attendance System")
        print("0. View All Attendances")
        print("1. Take Attendance")
        print("2. Calculate Attendance Percentage for a Student")
        print("3. Notify Low Attendance")
        print("4. Exit Program")

        choice = int(input("Enter your choice: "))
        if choice == 0:
            view_attendance(class_attendance)
        elif choice == 1:
            class_attendance = take_attendance(class_attendance)

        elif choice == 2:
            student_name = input("Enter the student's name (lowercase): ")
            attendance_pct = attendance_percentage(student_name, class_attendance)
            if attendance_pct is not None:
                print("{}'s attendance percentage: {}%".format(student_name, attendance_pct))

        elif choice == 3:
            threshold = float(input("Enter the attendance threshold (e.g., 75): "))
            low_attendance_students = notify_low_attendance(class_attendance, threshold)
            print("Students with low attendance:", low_attendance_students)

        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

menu_system(attendance_dict)

