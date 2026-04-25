# =========================
# Student Results Solution (Split Version)
# =========================
import os

folder = os.getcwd()
student_results = {}
pass_students = {}
fail_students = {}

distinction_count = 0
five_marks_away_count = 0
ten_marks_away_count = 0
fifteen_marks_away_count = 0

# Read from results.txt
file_name = "results.txt"

full_path = os.path.join(folder, file_name)
with open(full_path, "r") as file:
    for line in file:
        parts = line.strip().split()

        name = parts[0]
        mark = int(parts[1])

        student_results[name] = mark

# Sort into pass/fail
for name in student_results:
    mark = student_results[name]

    if mark >= 50:
        pass_students[name] = mark
    else:
        fail_students[name] = mark

# Count categories
for name in pass_students:
    mark = pass_students[name]

    if mark >= 90:
        distinction_count += 1
    elif mark >= 85:
        five_marks_away_count += 1
    elif mark >= 80:
        ten_marks_away_count += 1
    elif mark >= 75:
        fifteen_marks_away_count += 1

# Write output
output_file_name = "summary1.txt"
output_full_path = os.path.join(folder, output_file_name)
with open(output_file_name, "w") as file:
    file.write("Total number of students: " + str(len(student_results)) + "\n")
    file.write("Total number of failure: " + str(len(fail_students)) + "\n")
    file.write("Total number of passing: " + str(len(pass_students)) + "\n")
    file.write("Total number of distinction: " + str(distinction_count) + "\n")
    file.write("Total number of 5 marks away from distinction: " + str(five_marks_away_count) + "\n")
    file.write("Total number of 10 marks away from distinction: " + str(ten_marks_away_count) + "\n")
    file.write("Total number of 15 marks away from distinction: " + str(fifteen_marks_away_count) + "\n")

print("summary.txt has been created.")
