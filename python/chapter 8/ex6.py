sum = count = 0

try:
    with open("files/text.txt") as f:
        for line in f:
            count += 1
            for word in line.split():
                sum += 1

except Exception as e:
    print(f"Error: {e}")

print(f"Average number of words: {sum / count}")
