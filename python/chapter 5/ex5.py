print("Enter the property's actual value: ")
actualValue = float(input())

print(
    f"Actual value of a piece of property: {actualValue}\nAssessment value: {actualValue * 0.6}\nProperty tax: {((actualValue * 0.6) / 100) * 0.072}"
)
