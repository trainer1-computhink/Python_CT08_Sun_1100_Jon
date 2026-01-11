# Lesson 5 - School Attendance System (SAS)

## Task 1: Create Student Database
**Create the Initial Attendance Database​**

- Create a dictionary to store the names of students and their attendance records.​
- Initialize a dictionary where each key is a student’s name, and the value is a list of booleans representing attendance ​
- (True for present, False for absent).​
- This dictionary will serve as the database for all subsequent tasks.

## Task 2: Take Student Attendance
**Take Attendance​**

Create a function called take_attendance()​

Params:​
- dictionary containing the student name and previous attendance​

Function purpose:​
- Loop through all the students, and ask if the student present or absence, and update the attendance accordingly.​
- You must validate the input.​

Return:​
- updated dictionary with attendance record

## Task 3: Calculate Attendance Percentage
**Create a function called attendance_percentage()​**

Params:​
- student: String – containing the student name​
- attendance_dict: Dictionary – containing the class names and attendance​

Function purpose:​
- Lookup the student in the dictionary.​
- Calculate the percentage of True values.​
- Return the percentage of True values​

Return:​
- attendance_percentage: Float – containing the attendance percentage.

## Task 4: Notify low attendance
**Identify students with attendance below a defined threshold and notify them.​**

Function : notify_low_attendance()​

Params:​
- attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​
- threshold (float): Minimum attendance percentage required.​

Return:​
- low_attendance_students(list): A list of student names with attendance below the threshold

## Task 5: Create the Menu System
**Build an interactive menu to access the attendance system's features.**​

Display a menu with the following options:​
- 1: Take Attendance​
- 2: Calculate Attendance Percentage for a Student​
- 3: Notify Low Attendance​
- 4: Exit Program​

Based on the user’s choice:​
- Call the respective function with the necessary inputs.​
- Display the results of the chosen action

## Challenge: View All Attendances
Add a view_attendance() function. ​
Params:​
- attendance_dict (dictionary): Attendance database with student names as keys and attendance records as values.​

Return: none

*In this case, this function just needs to print out each student’s attendance.​*
*Remember to add this option to your menu.​*
*This is a challenge! Try this on your own without your Code Mentor’s guidance.*