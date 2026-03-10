with open("files/numbers.txt") as file:
    sum = count = 0
    line = file.readline()

    while line != "":
        sum += int(line)
        count += 1
        line = file.readline()

print(f"Average: {sum / count}")
