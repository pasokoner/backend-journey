def test_score(answer_sheet, student_answers):
    score = 0
    for i in range(len(answer_sheet)):
        if answer_sheet[i] == student_answers[i + 1]:
            score += 1

    return student_answers[0], score / len(answer_sheet) * 100


# Don't touch below this line


def test(answer_sheet, student_1_answers):
    name, percentage = test_score(answer_sheet, student_1_answers)
    print(f"{name}: {percentage:.1f}%")


def main():
    answer_sheet = [
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_1_answers = [
        "Allan",
        "A",
        "C",
        "C",
        "B",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_2_answers = [
        "John",
        "A",
        "D",
        "A",
        "A",
        "D",
        "A",
        "C",
        "B",
        "D",
        "A",
        "F",
        "A",
        "C",
        "B",
        "D",
        "C",
        "D",
        "C",
        "D",
        "A",
    ]
    student_3_answers = [
        "Jeremy",
        "A",
        "B",
        "D",
        "C",
        "D",
        "B",
        "D",
        "A",
        "C",
        "C",
        "D",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "F",
        "A",
    ]
    student_4_answers = [
        "Sally",
        "A",
        "A",
        "D",
        "A",
        "A",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "F",
        "A",
        "D",
        "A",
    ]
    student_5_answers = [
        "Tim",
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]

    test(answer_sheet, student_1_answers)
    test(answer_sheet, student_2_answers)
    test(answer_sheet, student_3_answers)
    test(answer_sheet, student_4_answers)
    test(answer_sheet, student_5_answers)


main()
