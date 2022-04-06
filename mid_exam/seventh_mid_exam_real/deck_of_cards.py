deck = input().split(", ")
n = int(input())

for _ in range(n):

    command = input().split(", ")
    action = command[0]
    value = command[1]

    if action == "Add":
        if value in deck:
            print("Card is already in the deck")
        else:
            deck.append(value)
            print("Card successfully added")

    elif action == "Remove":
        if value in deck:
            print("Card successfully removed")
            deck.remove(value)
        else:
            print("Card not found")

    elif action == "Remove At":
        if 0 <= int(value) < len(deck):
            deck.pop(int(value))
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == "Insert":
        card_name = command[2]
        if 0 <= int(value) < len(deck):
            if card_name in deck:
                print("Card is already added")
            else:
                deck.insert(int(value), card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(deck))