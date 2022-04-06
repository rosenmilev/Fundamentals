cards = input()
shuffles = int(input())

cards = cards.split()

while shuffles > 0:
    first_half = []
    second_half = []
    shuffled_cards = []
    for i in range(int(len(cards) / 2)):
        first_half.append(cards[i])

    for i in range(int(len(cards) / 2), len(cards)):
        second_half.append(cards[i])

    for i in range(len(first_half)):
        shuffled_cards.append(first_half[i])
        shuffled_cards.append(second_half[i])

    cards = shuffled_cards
    shuffles -= 1

print(cards)
