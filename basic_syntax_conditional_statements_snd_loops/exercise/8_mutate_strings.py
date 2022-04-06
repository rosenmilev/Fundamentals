first_string = input()
second_string = input()

for i in range(len(first_string)):
    if not first_string[i] == second_string[i]:
        print(second_string[0:i + 1] + first_string[i + 1:len(second_string)])
