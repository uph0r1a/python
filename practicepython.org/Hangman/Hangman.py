import random, os

words = []
try:
    with open(
        "/storage/Coding/python/practicepython.org/Hangman/sowpods.txt", "r"
    ) as f:
        words = [line.strip() for line in f if line.strip()]
except Exception as e:
    print(f"Error: {e}")

os.system("clear")

HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

print("Welcome to Hangman!")
while 1:
    os.system("clear")
    word = list(random.choice(words))
    guess = list("_" * (len(word)))
    guessed = []
    number_of_wrong_guesses = 0

    while guess != word and number_of_wrong_guesses < 6:
        os.system("clear")
        print(HANGMANPICS[number_of_wrong_guesses])
        print(" ".join(guess), end="\n\n")
        print("Guessed Letters:", ", ".join(guessed))

        letter_guess = input("Guess your letter: ").upper().strip()
        if len(letter_guess) != 1 or not letter_guess.isalpha():
            print("Please enter a single letter.")
            continue

        if letter_guess in guessed:
            print("Letter already guessed")
            input("Press Enter...")
            continue

        guessed.append(letter_guess)

        if letter_guess not in word:
            print("Incorrect!")
            number_of_wrong_guesses += 1
            input("Press Enter...")
        else:
            for i, c in enumerate(word):
                if c == letter_guess:
                    guess[i] = letter_guess

    os.system("clear")
    print(HANGMANPICS[number_of_wrong_guesses])
    print(
        " ".join(guess)
        + ("\nCongratulations" if number_of_wrong_guesses < 6 else "\nYou lose")
    )

    while 1:
        choice = input("Do you want to continue(Y/N)?").upper().strip()
        if choice == "N" or choice == "Y":
            break
        print("Invalid choice")
    if choice == "N":
        break
