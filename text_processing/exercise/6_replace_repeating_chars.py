text = input()
new_text = ""
new_text += text[0]

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        continue
    else:
        new_text += text[i]

print(new_text)
