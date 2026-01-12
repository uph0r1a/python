print("Enter a file name: ", end="")
name = input()

with open("files/" + name + ".txt") as f:
    i = 0
    line = f.readline()
    while line != "" and i < 5:
        print(line, end="")
        i += 1
        line = f.readline()
