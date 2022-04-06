targets = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()

    if command == "End":
        targets = " ".join(list(map(str, targets)))
        print(f"Shot targets: {shot_targets} -> {targets}")
        break
    index = int(command)

    if 0 <= index <= len(targets) - 1 and targets[index] != -1:

        for i in range(len(targets)):

            if not i == index and not targets[i] == -1:

                if targets[i] > targets[index]:
                    targets[i] -= targets[index]
                else:
                    targets[i] += targets[index]

        targets[index] = -1
        shot_targets += 1


