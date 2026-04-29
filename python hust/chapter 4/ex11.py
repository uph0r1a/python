print("Enter the starting weight: ", end="")
weight = float(input())

print(f"{"Month":<10}{"Weight"}\n----------------")
for i in range(7):
    print(f"{i:<10}{weight}")
    weight -= 4
