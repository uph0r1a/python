with open("files/random.txt") as f:
    count = sum = 0
    line = f.readline()

    while line != "":
        count += 1
        sum += int(line)
        line = f.readline()

print(
    f"The total of the numbers: {sum}\nThe number of random numbers read from the file: {count}"
)
