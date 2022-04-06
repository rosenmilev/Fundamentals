data = input()
text_to_print = data[0].upper()
multiplier = ""
final_print = ""

for i in range(1, len(data)):

    if not data[i].isnumeric():
        text_to_print += data[i].upper()

    else:
        multiplier += data[i]

        if i == len(data) - 1:
            final_print += text_to_print * int(multiplier)
            break

        if not data[i + 1].isnumeric():
            final_print += text_to_print * int(multiplier)
            multiplier = ""
            text_to_print = ""

print(f"Unique symbols used: {len(set(final_print))}")
print(final_print)
