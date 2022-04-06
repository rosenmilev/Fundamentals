first_string = input()
second_string = input()

while True:

    second_string = second_string.replace(first_string, "")

    if first_string not in second_string:
        break

print(second_string)
