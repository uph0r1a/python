print("Reboot the computerand try to connect\nDid that fix the problem: ", end="")
fixed = input()

if fixed.lower() == "yes":
    pass
else:
    print("Reboot the router and try to connect\nDid that fix the problem: ", end="")
    fixed = input()
    if fixed.lower() == "yes":
        pass
    else:
        print(
            "Make sure the cables between the router & modem are plugged in firmly.\nDid that fix the problem: ",
            end="",
        )
        fixed = input()
        if fixed.lower() == "yes":
            pass
        else:
            print(
                "Move the router to a new location and try to connect.\nDid that fix the problem: ",
                end="",
            )
            fixed = input()
            if fixed.lower() == "yes":
                pass
            else:
                print("Get a new router.")
