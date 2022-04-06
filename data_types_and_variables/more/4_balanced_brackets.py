number_of_lines = int(input())

list_of_brackets = []

for line in range(number_of_lines):
    inputs = input()
    if inputs == "(" or inputs == ")":
        list_of_brackets.append(inputs)

evens = True
odds = True

if list_of_brackets[0] == ")":
    print("UNBALANCED")
else:
    for i in range(len(list_of_brackets)):
        if i % 2 == 0 and not list_of_brackets[i] == "(":
            evens = False
        if i % 2 == 1 and not list_of_brackets[i] == ")":
            odds = False

    if len(list_of_brackets) % 2 == 0 and evens and odds:
        print("BALANCED")
    else:
        print("UNBALANCED")
