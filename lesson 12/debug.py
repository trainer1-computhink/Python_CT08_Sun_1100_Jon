# Qns: Debug the Code

# This program should:
# 1. Calculate each student's total score
# 2. Store all total scores in total_scores
# 3. Find the highest, lowest, number of students, and average score
# 4. Create a 1D list called result_summary:
#    name, total score, status
# 5. Convert result_summary into a 2D list called result_table using slicing
# 6. Print each row neatly

# Rules:
# 1. You are NOT allowed to remove any lines.
# 2. You can only MODIFY existing lines.

students = [
    ["Alex", 85, 92, 78],
    ["Ben", 42, 55, 61],
    ["Clara", 73, 80, 69],
    ["Dylan", 91, 88, 95],
    ["Eva", 58, 63, 70],
    ["Farah", 67, 72, 66],
    ["George", 81, 79, 84],
    ["Hannah", 95, 97, 93]
]

total_scores = []

for i in range(len(students))
    total = students[i][1] + students[i][2] + students[i][4]
    total_scores.append(total)

highest = max(total_score)
lowest = min(total_scores)
count = len(students[0])
average = total_scores / count

print("Highest total score: " + highest)
print("Lowest total score: " + str(lowest))
print("Number of students: " + str(count))
print("Average total score: " + str(average))

result_summary = []

for i in range(len(students)):
    name = students[i][0]
    total = total_scores[i]

    if total > 150:
        status = "Pass"
    else:
    status = "Fail"

    result_summary.append(name)
    result_summary.append(status)
    result_summary.append(total)

result_table = []

for i in range(0, len(result_summary), 2):
    row = result_summary[i:i+3]
    result_table.append(row)

for i in range(len(result_table)):
    name = result_table[i][0]
    total = result_table[i][1]
    status = result_table[i][2]

    print(name + " - " + total + " - " + status)