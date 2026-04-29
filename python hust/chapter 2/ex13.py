print("Enter the length of the row, in feet: ", end="")
rowLength = float(input())

print("Enter the amount of space used by an end-post assembly, in feet: ", end="")
endpostAssemblySpace = float(input())

print("Enter the amount of space between the vines, in feet: ", end="")
vinesSpace = float(input())

print(
    f"The number of grapevines that will fit in the row: {(rowLength - 2*endpostAssemblySpace)/vinesSpace}"
)
