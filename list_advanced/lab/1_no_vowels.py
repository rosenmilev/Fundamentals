text = input()
vowels = "aouei"

new_text = "".join([i for i in text if i not in vowels])

print(new_text)
