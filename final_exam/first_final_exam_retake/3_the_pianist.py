number_of_pieces = int(input())
pieces_dict = {}

for _ in range(number_of_pieces):
    piece = input().split("|")

    if piece[0] not in pieces_dict:
        pieces_dict[piece[0]] = []

    pieces_dict[piece[0]].append(piece[1])
    pieces_dict[piece[0]].append(piece[2])

while True:
    command = input().split("|")

    if command[0] == "Stop":
        break

    if command[0] == "Add":
        if command[1] not in pieces_dict:
            pieces_dict[command[1]] = []
            pieces_dict[command[1]].append(command[2])
            pieces_dict[command[1]].append(command[3])
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
        else:
            print(f"{command[1]} is already in the collection!")

    elif command[0] == "Remove":
        if command[1] in pieces_dict:
            pieces_dict.pop(command[1])
            print(f"Successfully removed {command[1]}!")

        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        if command[1] in pieces_dict:
            pieces_dict[command[1]][1] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")

for key, value in pieces_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
