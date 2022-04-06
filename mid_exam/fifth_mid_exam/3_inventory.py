journal = input().split(", ")

while True:
    command = input().split(" - ")
    action = command[0]

    if action == "Craft!":
        print(", ".join(journal))
        break

    item_1 = command[1]

    if action == "Collect":
        if item_1 not in journal:
            journal.append(item_1)
    elif action == "Drop":
        if item_1 in journal:
            journal.remove(item_1)
    elif action == "Combine Items":
        item_1 = item_1.split(":")
        first_item = item_1[0]
        second_item = item_1[1]
        if first_item in journal:
            journal.insert(journal.index(first_item) + 1, second_item)
    elif action == "Renew":
        if item_1 in journal:
            journal.append(item_1)
            journal.remove(item_1)
