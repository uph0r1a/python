import random

responses = []

try:
    with open("files/8_ball_responses.txt") as f:
        for line in f:
            responses.append(line.strip())
except Exception as e:
    print(f"Error: {e}")
    exit()

quit = False
while not quit:
    question = input("Enter a question: ")

    if question:
        print(random.choice(responses))
    else:
        print("No question")

    quitQuestion = input("Do you want to quit? (Y/YES): ")

    if quitQuestion.upper() in ("Y", "YES"):
        quit = True
