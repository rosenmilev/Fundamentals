string = input()
indexes = []

for i in range(0, len(string)):
    if string[i] == string[i].upper() and not string[i] == " " and string[i].isalpha():
        indexes.append(i)

print(indexes)
