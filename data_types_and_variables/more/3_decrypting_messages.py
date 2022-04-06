key = int(input())
lines = int(input())

decrypted_char = ""
message = ""

for i in range(lines):
    character = input()
    decrypted_char = chr(ord(character) + key)
    message += decrypted_char

print(message)
