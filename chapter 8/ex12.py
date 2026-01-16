sentence = input("Enter a string: ")

words = sentence.split()
result = []

for word in words:
    if len(word) > 1:
        pig_word = word[1:] + word[0] + "AY"
    else:
        pig_word = word + "AY"
    result.append(pig_word)

print(" ".join(result))
