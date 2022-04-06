num = int(input())
command = []
train = [0 for i in range(num)]

while True:
    command = input().split()
    if command[0] == "End":
        break
    if command[0] == "add":
        train[len(train) - 1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])

print(train)
