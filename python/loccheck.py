import sys
lines_of_code = []
numberloc = int(0)
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
if len(sys.argv) > 2:
    sys.exit("Too many arguments")
else:
    if sys.argv[1].endswith(".py"):
        filename = sys.argv[1]
    else:
        sys.exit("Not a Python file")
try:
    with open(sys.argv[1], "r") as File:
        for line in File:
            lines_of_code.append(line)
except FileNotFoundError:
    sys.exit("File does not exit")
print(lines_of_code)
for line in lines_of_code:
    if line[0] == "#":
        pass
    elif line.isspace():
        pass
    else:
        numberloc += 1
print(numberloc)
