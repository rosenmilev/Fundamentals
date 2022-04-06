current_string = input()


numbers = "".join(list(filter(lambda x: x.isdigit(), current_string)))
letters = "".join(list(filter(lambda x: x.isalpha(), current_string)))
others = "".join(list(filter(lambda x: not x.isdigit() and not x.isalpha(), current_string)))

print(numbers)
print(letters)
print(others)
