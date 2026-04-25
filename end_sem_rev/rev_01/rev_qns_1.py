# Qns: Student Results File Processing

# You are given a text file called results.txt.
# Each line contains a student's name and mark, separated by a space.

# Example:
# Alex 92
# Ben 43
# Clara 78

# Your task:

# 1. Read the data from results.txt.

# 2. Convert the data into a dictionary called student_results.
#    The name should be the key.
#    The mark should be the value.

# 3. Create TWO new dictionaries:
#    - pass_students
#    - fail_students

# 4. Loop through student_results.
#    If the student scored 50 or above, store them in pass_students.
#    Otherwise, store them in fail_students.

# 5. From the pass_students dictionary, calculate:

# Definitions:
# - Distinction: 90 marks and above
# - 5 marks away from distinction: 85 to 89
# - 10 marks away from distinction: 80 to 84
# - 15 marks away from distinction: 75 to 79

# 6. Write the summary into a file called summary.txt.

# The output file should contain:

# Total number of students:
# Total number of failure:
# Total number of passing:
# Total number of distinction:
# Total number of 5 marks away from distinction:
# Total number of 10 marks away from distinction:
# Total number of 15 marks away from distinction:
