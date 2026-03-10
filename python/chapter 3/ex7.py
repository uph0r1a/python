def validColor(color):
    if color.lower() == "red" or color.lower() == "blue" or color.lower() == "yellow":
        return True
    return False


def colorInput():
    while 1:
        color = input()
        if validColor(color):
            return color.lower()
        print("Invalid primary color\nRe-enter color: ", end="")


print("Enter primary color 1: ", end="")
primary1 = colorInput()

print("Enter primary color 2: ", end="")
primary2 = colorInput()

if {primary1, primary2} == {"red", "blue"}:
    print("Purple")
elif {primary1, primary2} == {"red", "yellow"}:
    print("Orange")
elif {primary1, primary2} == {"blue", "yellow"}:
    print("Green")
