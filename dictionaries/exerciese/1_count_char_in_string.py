word = input()
char_dict = {}

for letter in word:
    if letter not in char_dict:
        char_dict[letter] = 0
    char_dict[letter] += 1

for let, occurrences in char_dict.items():
    if not let == " ":
        print(f"{let} -> {occurrences}")
