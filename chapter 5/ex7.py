print("Enter number of tickets for class A: ", end="")
classA = int(input())

print("Enter number of tickets for class B: ", end="")
classB = int(input())

print("Enter number of tickets for class C: ", end="")
classC = int(input())

print(
    f"Total income generated from ticket sale: {classA * 20 + classB * 15 + classC * 10}"
)
