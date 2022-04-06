def decipher_message(word):
    first = int("".join(filter(str.isdigit, word)))
    second = list(filter(str.isalpha, word))
    second[0], second[len(second) - 1] = second[len(second) - 1], second[0]
    second = "".join(second)
    word = chr(first) + second

    return word


current_message = input().split()

deciphered_message = [decipher_message(cur_word) for cur_word in current_message]
print(" ".join(deciphered_message))
