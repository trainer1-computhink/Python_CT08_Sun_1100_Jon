# ------------------------------------------------------------
# Grading System for a Quiz
# This system automates the grading process for a quiz. It includes:
# 1. Grading all students.
# 2. Calculating the class average.
# 3. Identifying the highest scorer(s).
# 4. Displaying all class results.
# ------------------------------------------------------------

# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

# ------------------------------------------------------------
# Task 1: Grade All Students
# Function: grade_all_students
# Purpose: Compare each student's answers with the answer key 
# and calculate their score.
# Input: 
#   - student_answers: Dictionary with student names as keys 
#       and their answers as values.
#   - answer_key: List of correct answers.
# Output:
#   - quiz_scores: Dictionary with student names as keys and 
#       their scores as values.
# ------------------------------------------------------------
def grade_all_students(student_answers, answer_key):
    """
    Grade all students by comparing their answers with the answer key.
    """
    quiz_scores = {}  # Dictionary to store scores for each student
    
    # Loop through each student and their answers
    for student, answers in student_answers.items():
        score = 0  # Initialize score for the current student
        
        # Compare each answer with the answer key
        for i in range(len(answer_key)):  
            if answers[i] == answer_key[i]:  # Check if the answer matches
                score += 1  # Increment score for a correct answer
                
        quiz_scores[student] = score  # Store the score in the dictionary
    
    return quiz_scores

# ------------------------------------------------------------
# Task 2: Calculate the Class Average
# Function: calculate_average_score
# Purpose: Calculate the average score of the class.
# Input: 
#   - quiz_scores: Dictionary with student names as keys 
#       and their scores as values.
# Output:
#   - average_score: Float representing the class average score.
# ------------------------------------------------------------
def calculate_average_score(quiz_scores):
    """
    Calculate the average score for the class.
    """   
    total_score = 0
    for student in quiz_scores:
        total_score += quiz_scores[student] # Sum all scores

    num_students = len(quiz_scores)  # Count the number of students
    
    average_score = total_score / num_students  # Calculate the average
    return round(average_score, 2)  # Round to 2 decimal places

# ------------------------------------------------------------
# Task 3: Find the Highest Scorer
# Function: find_highest_scorer
# Purpose: Identify the student(s) with the highest score.
# Input: 
#   - quiz_scores: Dictionary with student names as keys and their scores as values.
# Output:
#   - List of student names with the highest score.
# ------------------------------------------------------------
def find_highest_scorer(quiz_scores):
    """
    Find the student(s) with the highest score.
    """    
    max_score = 0
    # Find the maximum score
    # alternate shortcut ---  max_score = max(quiz_scores.values())  
    for student, score in quiz_scores.items():
        if score > max_score:
            max_score = score

    # Get all students with the maximum score
    highest_scorers = []
    for student in quiz_scores:
        if quiz_scores[student] == max_score:
            highest_scorers.append(student)

    return highest_scorers

# ------------------------------------------------------------
# Task 4: Display Class Results
# Function: display_results
# Purpose: Print all students and their respective scores.
# Input: 
#   - quiz_scores: Dictionary with student names as keys and 
#     their scores as values.
# Output:
#   - None (results are printed to the console).
# ------------------------------------------------------------
def display_results(quiz_scores):
    """
    Display all students and their respective scores.
    """
    if not quiz_scores:  # Check if the dictionary is empty
        print("No results to display.")
        return
    
    print("\nClass Results:")
    for student, score in quiz_scores.items():  # Loop through the dictionary
        print("{} : {}".format(student, score)) # Print each student's name and score


# ------------------------------------------------------------
# Task 5: Menu System
def menu_system():
    """
    Interactive menu system for the grading system.
    """
    quiz_scores = {}  # Initialize quiz scores as an empty dictionary

    while True:
        # Display menu options
        print("\nQuiz Grading System Menu")
        print("1. Grade All Students")
        print("2. Calculate Class Average")
        print("3. Find Highest Scorer")
        print("4. Display All Results")
        print("5. Exit")

        # Get user choice
        choice = int(input("Enter your choice: "))

        # Execute based on user choice
        if choice == 1:
            # Grade all students
            quiz_scores = grade_all_students(student_answers, answer_key)
            print("\nAll students have been graded.")

        elif choice == 2:
            # Calculate class average
            if not quiz_scores:
                print("Please grade all students first (Option 1).")
            else:
                average_score = calculate_average_score(quiz_scores)
                print("\nClass Average Score: {}".format(average_score))

        elif choice == 3:
            # Find the highest scorer(s)
            if not quiz_scores:
                print("Please grade all students first (Option 1).")
            else:
                highest_scorers = find_highest_scorer(quiz_scores)
                print("\nHighest Scorer(s): {}".format(highest_scorers))

        elif choice == 4:
            # Display all results
            if not quiz_scores:
                print("Please grade all students first (Option 1).")
            else:
                display_results(quiz_scores)

        elif choice == 5:
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# run the main menu program
menu_system()
