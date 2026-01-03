print("Enter rectangle 1's length: ", end="")
length1 = float(input())

print("Enter rectangle 1's width: ", end="")
width1 = float(input())

print("Enter rectangle 2's length: ", end="")
length2 = float(input())

print("Enter rectangle 2's width: ", end="")
width2 = float(input())

print("Rectangle 1" if width1 * length1 > width2 * length2 else "Rectangle 2")
