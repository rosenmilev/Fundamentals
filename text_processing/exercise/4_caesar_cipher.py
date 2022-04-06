string = input()
new_string = ""

for ch in string:
    new_string += chr(ord(ch) + 3)

print(new_string)
