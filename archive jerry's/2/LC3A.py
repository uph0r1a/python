myReaction = []
lol = int(input())
for _ in range(lol):
    original = input()
    BarbabaAnswer = input()
    myReaction.append((original, BarbabaAnswer))

for reallll in myReaction:
    original = reallll[0]
    answer = reallll[1]

    originalNumber: int = 0
    answerNumber: int = 0
    imBoutaPrintThis: int = 0
    flag: bool = False
    while True:
        if answerNumber > len(answer) - 1:
            break

        if answer[answerNumber] == original[originalNumber]:
            answerNumber += 1
            if flag:
                imBoutaPrintThis += 1
            else:
                flag = True

        elif answer[answerNumber] == original[originalNumber + 1]:
            originalNumber += 1
            flag = False

        else:
            imBoutaPrintThis: str = "IMPOSSIBLE"
            break


print(f"Case #1: {imBoutaPrintThis}")
