sequence = input().split()
moves = 0

while True:
    command = input().split()
    moves += 1
    if command[0] == "end":
        sequence = " ".join(sequence)
        print(f"Sorry you lose :(\n{sequence}")
        break
    else:
        index1 = int(command[0])
        index2 = int(command[1])

    if index1 == index2 or len(sequence) <= index2 or 0 > index2 or len(sequence) <= index1 or 0 > index1:
        sequence.insert(int(len(sequence) / 2), f"-{moves}a")
        sequence.insert(int(len(sequence) / 2), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        a = sequence[index1]
        sequence.remove(a)
        sequence.remove(a)
    elif not sequence[index1] == sequence[index2]:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break
