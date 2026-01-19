import random


def main():
    deck = create_deck()

    player1_total = 0
    player2_total = 0
    player = 1

    while deck:
        card, value = deal_card(deck, player1_total if player == 1 else player2_total)

        if player == 1:
            player1_total += value
            print(f"Player 1 draws {card} (total: {player1_total})")
        else:
            player2_total += value
            print(f"Player 2 draws {card} (total: {player2_total})")

        if player1_total > 21 and player2_total > 21:
            print("Both players busted. No winner.")
            return
        elif player1_total > 21:
            print("Player 1 busts! Player 2 wins!")
            return
        elif player2_total > 21:
            print("Player 2 busts! Player 1 wins!")
            return

        player = 2 if player == 1 else 1

    print("All cards have been dealt. Game over.")


def create_deck():
    deck = {}

    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    faces = {"Ace": 1, "Jack": 10, "Queen": 10, "King": 10}

    for suit in suits:
        for num in range(2, 11):
            deck[f"{num} of {suit}"] = num
        for face, value in faces.items():
            deck[f"{face} of {suit}"] = value

    return deck


def deal_card(deck, current_total):
    card = random.choice(list(deck))
    value = deck.pop(card)

    if "Ace" in card:
        if current_total + 11 <= 21:
            value = 11
        else:
            value = 1

    return card, value


main()
