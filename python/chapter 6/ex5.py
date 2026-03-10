with open("files/numbers.txt") as file:
    sum = 0
    line = file.readline()

    while line != "":
        sum += int(line)
        line = file.readline()

print(f"Sum: {sum}")
