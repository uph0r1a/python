import string

word_count = {}

try:
    with open("files/text.txt") as file:
        for line in file:
            for word in line.split():
                word = word.strip(string.punctuation).lower()

                if word:
                    word_count[word] = word_count.get(word, 0) + 1

except Exception as e:
    print(f"Error: {e}")

for word, count in word_count.items():
    print(f"{word}: {count}")
