import random


def main():
    deck = create_deck()

    player1_total = 0
    player2_total = 0
    player_turn = 1

    while len(deck) > 0:
        card, value = deal_card(
            deck, player1_total if player_turn == 1 else player2_total
        )

        if player_turn == 1:
            player1_total += value
            print(f"Player 1 draws {card} (total: {player1_total})")
            if player1_total > 21:
                print("Player 1 busts! Player 2 wins!")
                break
        else:
            player2_total += value
            print(f"Player 2 draws {card} (total: {player2_total})")
            if player2_total > 21:
                print("Player 2 busts! Player 1 wins!")
                break

        player_turn = 2 if player_turn == 1 else 1

    else:
        if player1_total > 21 and player2_total > 21:
            print("Both players busted. No winner.")
        else:
            print("No more cards in the deck.")


def create_deck():
    deck = {
        "Ace of Spades": 1,
        "2 of Spades": 2,
        "3 of Spades": 3,
        "4 of Spades": 4,
        "5 of Spades": 5,
        "6 of Spades": 6,
        "7 of Spades": 7,
        "8 of Spades": 8,
        "9 of Spades": 9,
        "10 of Spades": 10,
        "Jack of Spades": 10,
        "Queen of Spades": 10,
        "King of Spades": 10,
        "Ace of Hearts": 1,
        "2 of Hearts": 2,
        "3 of Hearts": 3,
        "4 of Hearts": 4,
        "5 of Hearts": 5,
        "6 of Hearts": 6,
        "7 of Hearts": 7,
        "8 of Hearts": 8,
        "9 of Hearts": 9,
        "10 of Hearts": 10,
        "Jack of Hearts": 10,
        "Queen of Hearts": 10,
        "King of Hearts": 10,
        "Ace of Clubs": 1,
        "2 of Clubs": 2,
        "3 of Clubs": 3,
        "4 of Clubs": 4,
        "5 of Clubs": 5,
        "6 of Clubs": 6,
        "7 of Clubs": 7,
        "8 of Clubs": 8,
        "9 of Clubs": 9,
        "10 of Clubs": 10,
        "Jack of Clubs": 10,
        "Queen of Clubs": 10,
        "King of Clubs": 10,
        "Ace of Diamonds": 1,
        "2 of Diamonds": 2,
        "3 of Diamonds": 3,
        "4 of Diamonds": 4,
        "5 of Diamonds": 5,
        "6 of Diamonds": 6,
        "7 of Diamonds": 7,
        "8 of Diamonds": 8,
        "9 of Diamonds": 9,
        "10 of Diamonds": 10,
        "Jack of Diamonds": 10,
        "Queen of Diamonds": 10,
        "King of Diamonds": 10,
    }
    return deck


def deal_card(deck, current_total):
    card = random.choice(list(deck))
    value = deck.pop(card)

    if "Ace" in card and current_total + 11 <= 21:
        value = 11
    elif "Ace" in card:
        value = 1

    return card, value


if __name__ == "__main__":
    main()
