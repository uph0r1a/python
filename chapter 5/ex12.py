def max(numb1, numb2):
    if numb1 >= numb2:
        return numb1
    else:
        return numb2


print("Enter number 1: ", end="")
numb1 = int(input())

print("Enter number 2: ", end="")
numb2 = int(input())

print(f"Greater of the 2: {max(numb1,numb2)}")
