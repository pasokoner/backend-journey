answer_sheet = ["A", "A", "C", "D", "D", "B", "C"]
student_answers = ["A", "B", "C", "A", "D", "B", "C"]

# Don't touch above this line

correct_count = 0
for i in range(len(answer_sheet)):
    if answer_sheet[i] == student_answers[i]:
        correct_count += 1

percentage = correct_count / len(answer_sheet) * 100

# Don't touch below this line

print(f"The student answered correctly on {percentage:2f}% of the questions")
