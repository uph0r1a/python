import random

number_of_streaks = 0

for experiment_number in range(10000):
    ls = [random.randint(0, 1) for _ in range(100)]

    for i in range(len(ls) - 5):
        if ls[i : i + 6] == [1] * 6 or ls[i : i + 6] == [0] * 6:
            number_of_streaks += 1
            break

print(f"Chance of streak: {number_of_streaks / 100} %")
