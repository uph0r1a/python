def calc_average(sum):
    return sum / 5


def determine_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score <= 59:
        return "F"


sum = 0

for i in range(5):
    print(f"Enter scores {i + 1}: ", end="")
    sum += float(input())

print(f"Score: {calc_average(sum)}\nLetter grade: {determine_grade(calc_average(sum))}")
