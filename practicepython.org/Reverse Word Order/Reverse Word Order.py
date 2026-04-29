def reverseStr(s):
    words = []
    word = ""
    reversedStr = ""

    for c in s:
        if c == " ":
            words.append(word)
            word = ""
        else:
            word += c

    words.append(word)

    for c in reversed(words):
        reversedStr += c + " "

    return reversedStr.strip()


s = input("Enter a string: ")
print("Reverse: " + reverseStr(s))
