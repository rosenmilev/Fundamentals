commands = []

while True:
    command = input()
    if command == "End":
        break
    commands.append(command)

commands.sort(key=lambda a: int(a.split("-")[0]))
result = [i.split("-")[1] for i in commands]

print(result)
