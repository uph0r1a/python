with open("files/names.txt") as file:
    count = 0

    line = file.readline()

    while line != "":
        count += 1
        line = file.readline()

print(f"Number of names: {count}")
