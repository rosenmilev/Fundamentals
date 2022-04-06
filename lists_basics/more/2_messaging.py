sequence = input().split(" ")
cipher = input()
cipher_list = []
message = ""

for let in cipher:
    cipher_list.append(let)

for num in sequence:
    char = sum(map(int, num))
    if char > len(cipher) - 1:
        char = char % (len(cipher_list))
    print(cipher_list[char], end="")
    cipher_list.remove(cipher_list[char])
