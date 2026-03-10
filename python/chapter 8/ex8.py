def Capitalize(text):
    result = ""
    capitalize_next = True

    for char in text:
        if capitalize_next and char.isalpha():
            result += char.upper()
            capitalize_next = False
        else:
            result += char

        if char in ".!?":
            capitalize_next = True

    return result


user_input = input("Enter a string: ")

print(Capitalize(user_input))
