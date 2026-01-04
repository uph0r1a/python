i = caloriesBurned = 0

while i != 31:
    caloriesBurned += 4.2
    if i == 10 or i == 15 or i == 20 or i == 25 or i == 30:
        print(f"Calories burned after {i} minutes: {4.2 * i}")
    i += 1
