print("Enter a person's age: ", end="")
age = int(input())

if age >= 20:
    print("Adult")
elif age >= 13:
    print("Teenager")
elif age > 1:
    print("Child")
elif age >= 0:
    print("Infant")
else:
    print("Age cannot be negative")
