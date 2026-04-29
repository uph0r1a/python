text = input("Enter a string: ")

most_frequent = text[0]
max_count = 0

for char in text:
    count = text.count(char)
    if count > max_count:
        max_count = count
        most_frequent = char

print("Most frequent character:", most_frequent)
