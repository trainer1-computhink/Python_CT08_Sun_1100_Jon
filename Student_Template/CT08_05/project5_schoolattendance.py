students = {
    "jonny": [True, True, True],
    "sally": [False, False, True],
    "becky": [False, True, True],
    "mark": [True, True, True],
    "linda": [False, False, False]
}

# ## Task 2: Take Student Attendance
# **Take Attendance​**

# Create a function called take_attendance()​

# Params:​
# - dictionary containing the student name and previous attendance​

# Function purpose:​
# - Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
# - You must validate the input.​

# Return:​

# def take_attendance(students_dict):
#     for name in students_dict:
#         ans = input(f"{name} is present?: ")
#         while ans != "y" and ans != "n":
#             print("reply y or n")
#             ans = input(f"Is {name} is present?: ")

#         if ans == "y":
#             students_dict[name].append(True)
#         else:
#             students_dict[name].append(False)


# take_attendance(students)

def take_attendance(attendance):
    for student in attendance:
        attendanceChecker = input(f"Is {student} present? Y/N ").lower().strip()
        while True:
            if attendanceChecker == "y":
                attendance[student].append(True)
                break

            if attendanceChecker == "n":
                attendance[student].append(False)
                break

            if attendanceChecker != "n" and attendanceChecker != "y":
                print("Please type your answer properly.")
                attendanceChecker = input(f"Is {student} present? Y/N ").lower().strip()
                continue

    return attendance
        
# print(takeAttendance(students))
# print(students)


## Task 3: Calculate Attendance Percentage
# **Create a function called attendance_percentage()​**

# Params:​
# - student: String – containing the student name​
# - attendance_dict: Dictionary – containing the class names and attendance​

# Function purpose:​
# - Lookup the student in the dictionary.​
# - Calculate the percentage of True values.​
# - Return the percentage of True values​

# Return:​
# - attendance_percentage: Float – containing the attendance percentage.

def attendance_percentage(student, attendance_dict):
    attendance_list = attendance_dict[student]
    sum_present = 0
    for status in attendance_list:
        if status:
            sum_present += 1
    return sum_present/len(attendance_list) * 100

# print(attendance_percentage("sally", students))

## Task 4: Notify low attendance
# **Identify students with attendance below a defined threshold and notify them.​**

# Function : notify_low_attendance()​

# Params:​
# - attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​
# - threshold (float): Minimum attendance percentage required.​

# Return:​
# - low_attendance_students(list): A list of student names with attendance below the threshold

def notify_low_attendance(attendance_dict, threshold):
    # declare an empty list inside the function for the low attendance students
    low_attendance_students = []
    # loop through the student in the dictionary
    for name in attendance_dict:
        #calculate for each student what is their attendance percentage
        attendance_percentage_student = attendance_percentage(name, attendance_dict)
        # check if that students attendance is below threshold
        if attendance_percentage_student < threshold:
            low_attendance_students.append(name)
    return low_attendance_students

# print(notify_low_attendance(students, 50))
## Challenge: View All Attendances
# Add a view_attendance() function. ​
# Params:​
# - attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​

def view_attendance(students):
    for student in students:
        print(f"{student} : {students[student]}")
    

    
## Task 5: Create the Menu System
# **Build an interactive menu to access the attendance system's features.**​

# Display a menu with the following options:​
# - 1: Take Attendance​
# - 2: Calculate Attendance Percentage for a Student​
# - 3: Notify Low Attendance​
# - 4: Exit Program​

# Based on the user’s choice:​
# - Call the respective function with the necessary inputs.​
# - Display the results of the chosen action

def menu():
    while True: 
        print("Attendance System")
        print("0: View Attendance")
        print("1: Take Attendance")
        print("2: Calculate Attendance Percentage for a Student")
        print("3: Notify Low Attendance")
        print("4: Exit Program")
        choice = input("Enter your choice: ")
        while choice not in ("0", "1", "2", "3", "4"):
            print("Please enter only  0 - 4.")
            choice = input("Enter your choice: ")

        
        if choice == "0":
            print(view_attendance(students))
        elif choice == "1":
            take_attendance(students)
        elif choice == "2":
            student_name = input("Enter the student's name: ").lower().strip()
            while student_name not in students:
                print("the student is not in the list.")
                student_name = input("Enter the student's name: ").lower().strip()

            student_attendance_percentage = attendance_percentage(student_name, students)
            print(f"{student_name}'s attendance percentage: {student_attendance_percentage}")
        elif choice == "3":
            threshold = int(input("Enter the attendance threshold: "))
            print(notify_low_attendance(students, threshold))

        else:
            break


menu()

