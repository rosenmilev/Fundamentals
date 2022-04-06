import re
number_of_valid_pairs = 0
mirror_words = []
text = input()

pattern = r"(@|\#)[A-Za-z]{3,}(\1)(\1)[A-Za-z]{3,}(\1)"

result = re.finditer(pattern, text)


for res in result:

    current_word = res.group()[1:len(res.group()) - 1]
    number_of_valid_pairs += 1

    if "#" in current_word:
        current_word = current_word.split("##")
    elif "@" in current_word:
        current_word = current_word.split("@@")

    first_word = current_word[0]
    second_word = current_word[1]

    if first_word[::-1] == second_word:
        mirror_words.append(f"{first_word} <=> {second_word}")

if number_of_valid_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{number_of_valid_pairs} word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(f"{', '.join(mirror_words)}")
else:
    print("No mirror words!")
