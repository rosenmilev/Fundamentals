cafes = 0
commands = ["coding", "dog", "cat", "movie"]

while True:
    command = input()
    if command == "END":
        if cafes > 5:
            print("You need extra sleep")
        else:
            print(cafes)
        break
    if command.lower() in commands:
        if command == command.lower():
            cafes += 1
        else:
            cafes += 2
