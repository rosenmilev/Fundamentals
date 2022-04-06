import re


def determine_letter_position(letter):
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    letter_position = alphabet.index(letter) + 1

    return letter_position


def operations(current_string: str):
    current_sum = 0

    first_letter = current_string[0]
    number = int(current_string[1:len(current_string) - 1])
    last_letter = current_string[-1]

    first_letter_position = determine_letter_position(first_letter)
    last_letter_position = determine_letter_position(last_letter)

    if first_letter.isupper():
        current_sum = number / first_letter_position
    elif first_letter.islower():
        current_sum = number * first_letter_position

    if last_letter.isupper():
        current_sum -= last_letter_position
    elif last_letter.islower():
        current_sum += last_letter_position

    return current_sum


total_sum = 0

pattern = r"\b[A-Za-z]\d+[A-Za-z]\b"
data = input()

strings = re.findall(pattern, data)

for string in strings:
    total_sum += operations(string)

print(f"{total_sum:.2f}")
