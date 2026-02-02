answer_key = ["A", "B", "B", "D"]
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}

question_marks = [2, 1, 3, 4]


# ----------------------------
# Helper input functions
# ----------------------------
def ask_int_range(prompt, min_val, max_val):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit():
            value = int(raw)
            if min_val <= value <= max_val:
                return value
        print(f"Invalid. Enter a number from {min_val} to {max_val}.")


# ============================================================
# Task 1 — Safe grading (uneven answer lists)
# ============================================================
def grade_all_students_safe(student_answers, answer_key):
    quiz_scores = {}

    for student, answers in student_answers.items():
        score = 0
        for i in range(len(answer_key)):
            if i < len(answers) and answers[i] == answer_key[i]:
                score += 1
        quiz_scores[student] = score

    return quiz_scores


# ============================================================
# Task 2 — Weighted grading
# ============================================================
def grade_all_students_weighted(student_answers, answer_key, question_marks):
    quiz_scores = {}

    for student, answers in student_answers.items():
        marks = 0
        for i in range(len(answer_key)):
            if i < len(answers) and answers[i] == answer_key[i]:
                marks += question_marks[i]
        quiz_scores[student] = marks

    return quiz_scores


def total_possible_marks(question_marks):
    total = 0
    for m in question_marks:
        total += m
    return total


# ============================================================
# Task 3 — Percentage + grade
# ============================================================
def grade_letter(pct):
    if pct >= 75:
        return "A"
    elif pct >= 60:
        return "B"
    elif pct >= 50:
        return "C"
    else:
        return "D"


def student_percentage(marks_scored, total_marks):
    if total_marks == 0:
        return 0.0
    return round((marks_scored / total_marks) * 100, 2)


# ============================================================
# Task 4 — Class performance summary
# ============================================================
def class_average_percentage_weighted(quiz_scores_weighted, question_marks):
    total_marks = total_possible_marks(question_marks)

    if len(quiz_scores_weighted) == 0 or total_marks == 0:
        return 0.0

    total_pct = 0.0
    for student, marks in quiz_scores_weighted.items():
        total_pct += (marks / total_marks) * 100

    return round(total_pct / len(quiz_scores_weighted), 2)


def class_performance_summary(quiz_scores_weighted, question_marks):
    total_marks = total_possible_marks(question_marks)
    avg_pct = class_average_percentage_weighted(quiz_scores_weighted, question_marks)

    above = 0
    below = 0
    full = 0

    for student, marks in quiz_scores_weighted.items():
        pct = 0.0
        if total_marks > 0:
            pct = (marks / total_marks) * 100

        if pct > avg_pct:
            above += 1
        elif pct < avg_pct:
            below += 1

        if marks == total_marks:
            full += 1

    print("\n--- Class Performance Summary ---")
    print("Class average (%):", avg_pct)
    print("Above average:", above)
    print("Below average:", below)
    print("Full marks:", full)


# ============================================================
# Task 5 — Hardest question(s)
# ============================================================
def hardest_questions(student_answers, answer_key):
    wrong_counts = []

    for i in range(len(answer_key)):
        wrong = 0
        for student, answers in student_answers.items():
            if i >= len(answers) or answers[i] != answer_key[i]:
                wrong += 1
        wrong_counts.append(wrong)

    max_wrong = wrong_counts[0]
    for w in wrong_counts:
        if w > max_wrong:
            max_wrong = w

    hardest = []
    for i in range(len(wrong_counts)):
        if wrong_counts[i] == max_wrong:
            hardest.append(i + 1)

    return hardest, max_wrong


# ============================================================
# Task 6 — Inconsistency detection
# ============================================================
def inconsistent_students(student_answers, answer_key):
    n = len(answer_key)
    first_half_end = n // 2
    flagged = []

    for student, answers in student_answers.items():
        first_correct = 0
        for i in range(first_half_end):
            if i < len(answers) and answers[i] == answer_key[i]:
                first_correct += 1

        second_correct = 0
        for i in range(first_half_end, n):
            if i < len(answers) and answers[i] == answer_key[i]:
                second_correct += 1

        first_pct = 0
        if first_half_end > 0:
            first_pct = (first_correct / first_half_end) * 100

        if first_pct >= 80 and second_correct == 0:
            flagged.append(student)

    return flagged


# ============================================================
# Task 7 — Competition ranking (NO lambda)
# ============================================================
def competition_ranking(quiz_scores):
    items = []

    for student in quiz_scores:
        items.append([student, quiz_scores[student]])

    # Manual sort: highest score first, name as tie-breaker
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]
            elif items[j][1] == items[i][1]:
                if items[j][0] < items[i][0]:
                    items[i], items[j] = items[j], items[i]

    ranked = []
    prev_score = None
    prev_rank = 0

    for index in range(len(items)):
        student = items[index][0]
        score = items[index][1]

        if prev_score is None:
            rank = 1
        elif score == prev_score:
            rank = prev_rank
        else:
            rank = index + 1

        ranked.append((rank, student, score))
        prev_score = score
        prev_rank = rank

    return ranked


# ============================================================
# Display helpers
# ============================================================
def display_results_raw(quiz_scores):
    if not quiz_scores:
        print("No results to display.")
        return

    print("\n--- Raw Scores ---")
    for student, score in quiz_scores.items():
        print(f"{student} : {score}")


def display_results_weighted_with_grades(quiz_scores_weighted, question_marks):
    if not quiz_scores_weighted:
        print("No results to display.")
        return

    total_marks = total_possible_marks(question_marks)
    print("\n--- Weighted Scores + Grade ---")
    for student, marks in quiz_scores_weighted.items():
        pct = student_percentage(marks, total_marks)
        grade = grade_letter(pct)
        print(f"{student} : {marks}/{total_marks} ({pct}%) Grade: {grade}")


# ============================================================
# Integrated Menu System
# ============================================================
def menu_system():
    quiz_scores_raw = {}
    quiz_scores_weighted = {}

    while True:
        print("\nQuiz Grading System Menu")
        print("1. Grade All Students (Raw)")
        print("2. Grade All Students (Weighted)")
        print("3. Display Raw Results")
        print("4. Display Weighted Results + Grade")
        print("5. Class Performance Summary")
        print("6. Highest Scorer(s) (Raw)")
        print("7. Hardest Question(s)")
        print("8. Inconsistency Detection")
        print("9. Competition Ranking (Weighted)")
        print("10. Exit")

        choice = ask_int_range("Enter your choice: ", 1, 10)

        if choice == 1:
            quiz_scores_raw = grade_all_students_safe(student_answers, answer_key)
            print("Students graded (raw).")

        elif choice == 2:
            quiz_scores_weighted = grade_all_students_weighted(
                student_answers, answer_key, question_marks
            )
            print("Students graded (weighted).")

        elif choice == 3:
            if quiz_scores_raw:
                display_results_raw(quiz_scores_raw)
            else:
                print("Please grade students first.")

        elif choice == 4:
            if quiz_scores_weighted:
                display_results_weighted_with_grades(
                    quiz_scores_weighted, question_marks
                )
            else:
                print("Please grade students first.")

        elif choice == 5:
            if quiz_scores_weighted:
                class_performance_summary(
                    quiz_scores_weighted, question_marks
                )
            else:
                print("Please grade students first.")

        elif choice == 6:
            if quiz_scores_raw:
                max_score = 0
                for s in quiz_scores_raw:
                    if quiz_scores_raw[s] > max_score:
                        max_score = quiz_scores_raw[s]

                highest = []
                for s in quiz_scores_raw:
                    if quiz_scores_raw[s] == max_score:
                        highest.append(s)

                print("Highest scorer(s):", highest, "Score:", max_score)
            else:
                print("Please grade students first.")

        elif choice == 7:
            hardest, wrong = hardest_questions(student_answers, answer_key)
            print("Hardest question(s):", hardest, "| Wrong by:", wrong)

        elif choice == 8:
            flagged = inconsistent_students(student_answers, answer_key)
            print("Inconsistent students:", flagged)

        elif choice == 9:
            if quiz_scores_weighted:
                ranked = competition_ranking(quiz_scores_weighted)
                for rank, student, score in ranked:
                    print(f"{rank}. {student} ({score})")
            else:
                print("Please grade students first.")

        elif choice == 10:
            print("Goodbye!")
            break


# Run program
menu_system()
