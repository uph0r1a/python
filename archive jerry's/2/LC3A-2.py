myReaction: list = []
lol = int(input())
for _ in range(lol):
    original = input()
    answer = input()
    myReaction.append((original, answer))

for real in myReaction:
    original: str = real[0]
    answer: str = real[1]

    originalNum: int = 0
    answerNum: int = 0
    lastCharacter: str = ""
    error: int = 0
    while True:
        if answerNum > len(answer) - 1:
            break

        if answer[answerNum] == original[originalNum]:
            lastCharacter = answer[answerNum]
            originalNum += 1
            answerNum += 1

        elif answer[answerNum] == lastCharacter:
            originalNum += 1
            error += 1

        else:
            error: str = "IMPOSSIBLE"

print(error)
