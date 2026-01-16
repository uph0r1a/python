def Vowels(string):
    count = 0
    for c in string.lower():
        if c in ("a", "e", "i", "o", "u"):
            count += 1
    return count


def Consonants(string):
    count = 0
    for c in string.lower():
        if c not in ("a", "e", "i", "o", "u"):
            count += 1
    return count


string = input("Enter a string: ")
print(f"Vowels: {Vowels(string)}\nConsonants: {Consonants(string)}")
