def check_force_user(force_book, force_user):
    is_present = False

    for value in force_book.values():
        if force_user in value:
            is_present = True

    return is_present


def search_force(force_book, force_user):
    result = ""
    for key in force_book:
        if force_user in force_book[key]:
            result = key

    return result


force_book = {}

command = input()

while not command == "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]

        if force_side not in force_book and not check_force_user(force_book, force_user):
            force_book[force_side] = []

        if not check_force_user(force_book, force_user):
            force_book[force_side].append(force_user)

    elif "->" in command:
        command = command.split(" -> ")
        force_side = command[1]
        force_user = command[0]

        if not check_force_user(force_book, force_user) and force_side not in force_book:
            force_book[force_side] = []
            force_book[force_side].append(force_user)

        elif not check_force_user(force_book, force_user):
            force_book[force_side].append(force_user)

        elif check_force_user(force_book, force_user):
            if force_side not in force_book:
                force_book[force_side] = []
            key = search_force(force_book, force_user)

            force_book[force_side].append(force_user)
            force_book[key].remove(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for key, value in force_book.items():
    if len(force_book[key]) > 0:
        print(f"Side: {key}, Members: {len(force_book[key])}")

        for user in force_book[key]:
            print(f"! {user}")
