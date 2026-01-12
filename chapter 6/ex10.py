def inputScore():
    try:
        with open("files/golf.txt", "a") as f:

            print("Enter player's name: ", end="")
            name = input()

            print(f"Enter player {name} golf score: ", end="")
            score = int(input())

            f.write(f"{name}: {score}\n")
    except Exception as e:
        print(f"Error: {e}")


def outputScore():
    try:
        with open("files/golf.txt") as f:

            line = f.readline()
            if line == "":
                print("No record yet")
            else:
                while line != "":
                    print(line, end="")
                    line = f.readline()
    except Exception as e:
        print(f"Error: {e}")


print("Golf score: \n1)Enter record\n2)Display record\nEnter your choice: ", end="")
choice = input()

if choice == "1":
    inputScore()
elif choice == "2":
    outputScore()
else:
    print("Invalid choice")
