text = input()
current_explosion = 0
new_text = ""

for i in range(len(text)):
    if text[i] == ">":
        current_explosion += int(text[i + 1])
        new_text += ">"
    elif current_explosion == 0:
        new_text += text[i]
    else:
        current_explosion -= 1

print(new_text)
