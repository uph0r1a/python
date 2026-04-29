import os


class Question:
    def __init__(
        self,
        trivia_question="",
        answer1="",
        answer2="",
        answer3="",
        answer4="",
        correct_answer=0,
    ):
        self.__trivia_question = trivia_question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct_answer = correct_answer

    def set_trivia_question(self, trivia_question=""):
        self.__trivia_question = trivia_question

    def set_answer1(self, answer1=""):
        self.__answer1 = answer1

    def set_answer2(self, answer2=""):
        self.__answer2 = answer2

    def set_answer3(self, answer3=""):
        self.__answer3 = answer3

    def set_answer4(self, answer4=""):
        self.__answer4 = answer4

    def set_correct_answer(self, correct_answer=0):
        self.__correct_answer = correct_answer

    def get_trivia_question(self):
        return self.__trivia_question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct_answer(self):
        return self.__correct_answer


questions = {
    1: Question(
        "Which color is the sky on a clear day?", "Green", "Blue", "Red", "Yellow", 2
    ),
    2: Question("How many days are there in a week?", "5", "6", "7", "8", 3),
    3: Question("What is 2 + 2?", "3", "4", "5", "6", 2),
    4: Question("Which animal barks?", "Cat", "Dog", "Cow", "Sheep", 2),
    5: Question(
        "What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3
    ),
    6: Question(
        "Which fruit is typically red?", "Banana", "Apple", "Grape", "Orange", 2
    ),
    7: Question("What do bees produce?", "Milk", "Honey", "Water", "Oil", 2),
    8: Question("How many legs does a spider have?", "6", "8", "10", "12", 2),
    9: Question(
        "Which season is the coldest?", "Summer", "Spring", "Winter", "Autumn", 3
    ),
    10: Question(
        "What is the opposite of 'hot'?", "Warm", "Cold", "Cool", "Boiling", 2
    ),
}
score1 = score2 = 0
for question in questions:
    os.system("clear")
    print(
        questions[question].get_trivia_question()
        + "\n1)"
        + questions[question].get_answer1()
        + "\n2)"
        + questions[question].get_answer2()
        + "\n3)"
        + questions[question].get_answer3()
        + "\n4)"
        + questions[question].get_answer4()
    )
    if int(input("Enter your choice: ")) == questions[question].get_correct_answer():
        print("Correct\n")
        if int(question) % 2 != 0:
            score1 += 1
        else:
            score2 += 1
    else:
        print("Incorrect\n")

    input(f"Player 1: {score1}\nPlayer 2: {score2}\nPress Enter to continue...")

os.system("clear")
if score1 > score2:
    print("Player 1 win")
elif score1 < score2:
    print("Player 2 win")
else:
    print("Draw")
