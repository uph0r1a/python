upperCase = lowerCase = digits = whiteSpace = 0
text = ""

try:
    with open("files/text.txt") as f:
        for line in f:
            for c in line:
                if c.isupper():
                    upperCase += 1
                elif c.islower():
                    lowerCase += 1
                elif c.isdigit():
                    digits += 1
                elif c.isspace():
                    whiteSpace += 1

except Exception as e:
    print(f"Error: {e}")


print(
    f"The number of uppercase letters in the file: {upperCase}\n"
    f"The number of lowercase letters in the file: {lowerCase}\n"
    f"The number of digits in the file: {digits}\n"
    f"The number of whitespace characters in the file: {whiteSpace}"
)
