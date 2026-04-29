text = set()

try:
    with open("files/text.txt") as f:
        for line in f:
            for word in line.split():
                text.add(word)

except Exception as e:
    print(f"Error: {e}")

print(text)
