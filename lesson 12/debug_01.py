# Qns: Debug the Code (Very Hard)

# This program should:
# 1. Read student results from results.txt
# 2. Each line in results.txt is in this format:
#    Alex 92
# 3. Convert the data into a dictionary called student_results
# 4. Sort students into pass_students and fail_students
# 5. Count:
#    - total students
#    - total failures
#    - total passing
#    - total distinction
#    - total students 5 marks away from distinction
#    - total students 10 marks away from distinction
#    - total students 15 marks away from distinction
# 6. Write the result into summary.txt

# Definitions:
# - Pass: 50 and above
# - Fail: below 50
# - Distinction: 90 and above
# - 5 marks away from distinction: 85 to 89
# - 10 marks away from distinction: 80 to 84
# - 15 marks away from distinction: 75 to 79

# Rules:
# 1. You are NOT allowed to remove any lines.
# 2. You can only MODIFY existing lines.

student_results = {}
pass_students = {}
fail_students = {}

distinction_count = 0
five_marks_away_count = 0
ten_marks_away_count = 0
fifteen_marks_away_count = 0

with open("results.txt", "r") as file
    lines = file.readlines()

for line in lines:
    parts = line.strip().split()

    name = parts[1]
    mark = parts[2]

    student_results[name] = marks

for name in student_result:
mark = student_results[name]

    if mark > 50:
        pass_students[name] = mark
    else:
        fail_students[mark] = name

for name in pass_students:
    mark = pass_students[name]

    if mark > 90:
        distinction_count = distinction_count + 1
    elif mark > 85:
        five_marks_away_count = five_marks_away_count + 1
    elif mark > 80:
        ten_marks_away_count = ten_marks_away_count + 1
    elif mark > 75:
        fifteen_marks_away_count = fifteen_marks_away_count + 1

with open("summary.txt", "w") as file:
    file.write("Total number of students: " + len(student_results) + "\n")
    file.write("Total number of failure: " + str(len(pass_students)) + "\n")
    file.write("Total number of passing: " + str(len(fail_students)) + "\n")
    file.write("Total number of distinction: " + str(distinction_count) + "\n")
    file.write("Total number of 5 marks away from distinction: " + five_marks_away_count + "\n")
    file.write("Total number of 10 marks away from distinction: " + str(ten_marks_away_count) + "\n")
    file.write("Total number of 15 marks away from distinction: " + str(fifteen_marks_away_count) + "\n")

print("Summary file created")