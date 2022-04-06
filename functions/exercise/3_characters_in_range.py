def chars_in_range(chr1, chr2):
    for char in range(ord(chr1) + 1, ord(chr2)):
        if char == ord(chr2) - 1:
            print(chr(char))
        else:
            print(chr(char), end=" ")


char1, char2 = input(), input()
chars_in_range(char1, char2)
