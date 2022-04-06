string = input()
string = string.lower()

counter = 0

for i in range(len(string)):
    if string[i:i + 3] == "sun" or string[i:i + 4] == "sand" or string[i:i + 4] == "fish" or string[i:i + 5] == "water":
        counter += 1

print(counter)
