import os

# # get current working directory
# filepath = os.getcwd()
# print(f"filepath: {filepath}")

# fullpath = os.path.join(filepath, "lesson71.py")
# print(f"fullpath: {fullpath}")

# # check existence of a file
# if os.path.exists(fullpath):
#     print(f"{fullpath} exists.")
# else:
#     print(f"{fullpath} does not exist.")

# file = open("output.txt", "w")
# file.write("Manual write example")
# file.close()

# file = open("output.txt", "r")
# content = file.read()
# print(f"File content:\n{content}")
# file.close()

# with open("output.txt","r") as file:
#     content = file.read()
#     print(f"File content with 'with':\n{content}")

with open("output3.txt","w") as file:
    file.write("Hello, world!")

# with open("output1.txt", "a") as file:
#     file.write("\nThis will add a new line to the file.")
#     file.write("\nThis will add another line")

lines = ["Line 1\n","Line 2\n","Line 3\n"]
with open("output2.txt","w") as file:
    file.writelines(lines)

with open("output1.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("Line:" + line.strip())