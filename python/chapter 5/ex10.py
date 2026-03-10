def feet_to_inches(feet):
    return feet * 12


print("Enter a number of feet: ", end="")
feet = float(input())

print(f"Number of inches: {feet_to_inches(feet)}")
