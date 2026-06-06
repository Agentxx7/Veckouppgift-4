import random


def random_card():
    suits = ["ruter", "hjärter", "spader", "klöver"]
    suit = random.choice(suits)
    value = random.randint(2, 14)

    return [suit, value]


def same_value(card1, card2):
    return card1[1] == card2[1]


def value_to_text(value):
    if value == 11:
        return "knekt"
    elif value == 12:
        return "dam"
    elif value == 13:
        return "kung"
    elif value == 14:
        return "ess"
    else:
        return str(value)


def pretty_print_card(card):
    suit = card[0]
    value = card[1]

    return suit + " " + value_to_text(value)


def count_values(cards):
    counts = {}

    for card in cards:
        value = card[1]

        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    return counts


def is_flush(cards):
    first_suit = cards[0][0]

    for card in cards:
        if card[0] != first_suit:
            return False

    return True


def is_straight(cards):
    values = []

    for card in cards:
        values.append(card[1])

    values.sort()

    for index in range(0, len(values) - 1):
        if values[index + 1] != values[index] + 1:
            return False

    return True


def poker_hand(cards):
    value_counts = count_values(cards)

    pairs = []
    three_of_a_kind = None
    four_of_a_kind = None
    five_of_a_kind = None

    for value in value_counts:
        count = value_counts[value]

        if count == 2:
            pairs.append(value)
        elif count == 3:
            three_of_a_kind = value
        elif count == 4:
            four_of_a_kind = value
        elif count == 5:
            five_of_a_kind = value

    straight = is_straight(cards)
    flush = is_flush(cards)

    # Viktigt: kontrollera bästa händerna först.
    if five_of_a_kind is not None:
        print("Du fick femtal med valören: " + value_to_text(five_of_a_kind))

    elif straight and flush:
        print("Du fick straight flush")

    elif four_of_a_kind is not None:
        print("Du fick fyrtal med valören: " + value_to_text(four_of_a_kind))

    elif three_of_a_kind is not None and len(pairs) == 1:
        print(
            "Du fick hus med tretal i "
            + value_to_text(three_of_a_kind)
            + " och par i "
            + value_to_text(pairs[0])
        )

    elif flush:
        print("Du fick flush/färg")

    elif straight:
        print("Du fick straight")

    elif three_of_a_kind is not None:
        print("Du fick tretal med valören: " + value_to_text(three_of_a_kind))

    elif len(pairs) == 2:
        print(
            "Du fick två par med valörerna: "
            + value_to_text(pairs[0])
            + " och "
            + value_to_text(pairs[1])
        )

    elif len(pairs) == 1:
        print("Du fick ett par med valören: " + value_to_text(pairs[0]))

    else:
        print("Du fick ingen pokerhand")


def print_cards(cards):
    print("Dina kort:")

    for card in cards:
        print("- " + pretty_print_card(card))


def run_poker_demo():
    cards = []

    for _ in range(5):
        cards.append(random_card())

    print_cards(cards)
    poker_hand(cards)