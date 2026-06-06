import random


def draw_card():
    """Drar ett kort mellan 1 och 11."""
    return random.randint(1, 11)


def calculate_score(cards):
    """Räknar ihop summan av korten i listan."""
    total = 0

    for card in cards:
        total += card

    return total


def print_hand(name, cards):
    """Skriver ut spelarens eller datorns kort och poäng."""
    score = calculate_score(cards)
    print(f"{name} har korten {cards}. Poäng: {score}")


def player_turn(player_cards):
    """Låter spelaren dra kort tills spelaren stannar eller får över 21."""
    while True:
        print_hand("Du", player_cards)

        if calculate_score(player_cards) > 21:
            print("Du fick över 21 och förlorade.")
            break

        choice = input("Vill du dra ett kort till? (j/n): ")

        if choice.lower() == "j":
            player_cards.append(draw_card())
        else:
            break


def dealer_turn(dealer_cards):
    """Datorn drar kort tills den har minst 17 poäng."""
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(draw_card())

    print_hand("Datorn", dealer_cards)


def decide_winner(player_cards, dealer_cards):
    """Avgör vem som vinner."""
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)

    print()
    print("Resultat:")
    print_hand("Du", player_cards)
    print_hand("Datorn", dealer_cards)

    if player_score > 21:
        print("Datorn vinner.")
    elif dealer_score > 21:
        print("Du vinner! Datorn fick över 21.")
    elif player_score > dealer_score:
        print("Du vinner!")
    elif dealer_score > player_score:
        print("Datorn vinner.")
    else:
        print("Det blev oavgjort.")


def start_twentyone():
    """Startar spelet TwentyOne."""
    print("Välkommen till TwentyOne!")
    print("Försök komma så nära 21 som möjligt utan att gå över.")
    print()

    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]

    player_turn(player_cards)

    if calculate_score(player_cards) <= 21:
        dealer_turn(dealer_cards)

    decide_winner(player_cards, dealer_cards)