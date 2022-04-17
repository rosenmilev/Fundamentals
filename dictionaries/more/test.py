import string


def determine_letter_position(letter):
    letter = letter.lower()
    alphabet = string.ascii_lowercase

    letter_position = alphabet.index(letter)

    return letter_position


letter = input()
print(determine_letter_position(letter))
