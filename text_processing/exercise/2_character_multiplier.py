def character_multiplier(string_1, string_2):
    total_sum = 0

    if len(string_1) > len(string_2):
        for i in range(len(string_2)):
            total_sum += ord(string_1[i]) * ord(string_2[i])
        for letter in string_1[len(string_2):]:
            total_sum += ord(letter)
    elif len(string_1) < len(string_2):
        for i in range(len(string_1)):
            total_sum += ord(string_2[i]) * ord(string_1[i])
        for letter in string_2[len(string_1):]:
            total_sum += ord(letter)
    else:
        for i in range(len(string_2)):
            total_sum += ord(string_1[i]) * ord(string_2[i])

    return total_sum


strings = input().split(" ")

print(character_multiplier(strings[0], strings[1]))
