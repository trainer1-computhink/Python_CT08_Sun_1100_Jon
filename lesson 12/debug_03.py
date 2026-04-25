# Qns: Debug the Code (Monster Challenge)

# This program should be a simple class score manager.

# The program should:
# 1. Store student names in a list called students
# 2. Store student marks in a dictionary called scores
# 3. Keep showing the menu until the user chooses 7
# 4. Add a new student and score
# 5. Update an existing student's score
# 6. Remove a student
# 7. Search for a student
# 8. Print all students with their scores
# 9. Print a summary:
#    - total number of students
#    - number of passing students
#    - number of failing students
#    - highest score
#    - lowest score
#
# Rules:
# 1. You are NOT allowed to remove any lines.
# 2. You can only MODIFY existing lines.

# Removal Rule:
# You must remove the student from BOTH students list and scores dictionary.
# You may use ONE of the following:
# Option 1: .pop() with index
# Option 2: del with index

students = ["Alex", "Ben", "Clara"]
scores = {
    "Alex": 85,
    "Ben": 42,
    "Clara": 73
}

choice = 0

while choice != 7
    print("===== Class Score Manager =====")
    print("1. Add student")
    print("2. Update score")
    print("3. Remove student")
    print("4. Search student")
    print("5. Print all students")
    print("6. Print summary")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice = 1:
        name = input("Enter student name: ")
        mark = input("Enter score: ")

        students.append(score)
        scores[mark] = name

        print(name + " added with score " + mark)

    elif choice == 2
        name = input("Enter student to update: ")

        if name in student:
            new_mark = input("Enter new score: ")
            scores[name] == new_mark
            print(name + " score updated to " + scores[name])
        else
            print(name + " not found")

    elif choice == 3:
        name = input("Enter student to remove: ")

        if name in students:
            students.pop(name)
            scores.pop(index)
            print(name + " removed")
        else:
            print(name + " not found")

    elif choice == 4:
        name = input("Enter student to search: ")

        if name in scores:
            print(name + " scored " + scores[name])
        else:
        print(name + " not found")

    elif choice == 5:
        for i in range(len(students) + 1):
            name = students[i + 1]
            print(str(i + 1) + ". " + name + " - " + scores[i])

    elif choice == 6:
        passing = 0
        failing = 0
        highest = 0
        lowest = 100

        for name in scores:
            mark = scores[name]

            if mark > 50:
                passing = passing + 1
            else:
                failing = failing + 1

            if mark < highest:
                highest = mark

            if mark > lowest:
                lowest = mark

        print("Total students: " + len(students))
        print("Passing students: " + passing)
        print("Failing students: " + str(failing))
        print("Highest score: " + str(lowest))
        print("Lowest score: " + str(highest))

    elif choice == 7:
        print("Goodbye!")

    else
        print("Invalid choice")

print("Final students:", student)
print("Final scores: " + scores)