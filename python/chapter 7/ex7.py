correct_answers = [
    "A",
    "C",
    "A",
    "A",
    "D",
    "B",
    "C",
    "A",
    "C",
    "B",
    "A",
    "D",
    "C",
    "A",
    "D",
    "C",
    "B",
    "B",
    "D",
    "A",
]

student_answers = []

try:
    with open("files/student_answers.txt") as file:
        for line in file:
            student_answers.append(line.strip().upper())

except Exception as e:
    print(f"\nError: {e}")

correct_count = 0
incorrect_questions = []

for i in range(len(correct_answers)):
    if student_answers[i] == correct_answers[i]:
        correct_count += 1
    else:
        incorrect_questions.append(i + 1)

incorrect_count = len(correct_answers) - correct_count

if correct_count >= 15:
    result = "PASSED"
else:
    result = "FAILED"

print(
    f"\nExam Result: {result}\n"
    f"Correct answers: {correct_count}\n"
    f"Incorrect answers: {incorrect_count}\n"
    f"Questions missed: {incorrect_questions}"
)
