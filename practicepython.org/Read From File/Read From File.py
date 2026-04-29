counter_dict = {}

try:
    with open("/storage/Coding/python/practicepython.org/Read From File/text.txt") as f:
        for line in f:
            line = line.strip()
            counter_dict[line] = counter_dict.get(line, 0) + 1
except Exception as e:
    print(f"Error: {e}")

print(counter_dict)