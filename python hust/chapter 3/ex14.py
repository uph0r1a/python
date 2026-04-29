print("Enter weight: ", end="")
weight = float(input())

print("Enter height: ", end="")
height = float(input())

BMI = weight * 703 / height**2

if BMI > 25:
    print("Overweight")
elif 18.5 <= BMI <= 25:
    print("Optimal")
else:
    print("Underweight")
