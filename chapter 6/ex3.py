print("Enter a file name: ", end="")
name = input()

with open("files/" + name + ".txt") as f:
    line = f.readline()
    i = 1
    while line != "":
        print(f"{i}: {line}", end="")
        i += 1
        line = f.readline()
