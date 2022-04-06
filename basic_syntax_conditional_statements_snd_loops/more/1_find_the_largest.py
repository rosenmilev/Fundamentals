# import sys
#
# number = input()
#
# number_as_string = number
# largest_digit = str(-sys.maxsize)
# largest_number = ""
#
# while True:
#     for digit in number:
#         if int(digit) > int(largest_digit):
#             largest_digit = digit
#     number = number.replace(largest_digit, "", 1)
#     largest_number += largest_digit
#     largest_digit = str(-sys.maxsize)
#     if len(number) == 0:
#         break
# print(largest_number)

#SECOND WAY

number = input()

number_as_string = number
max_number_possible = ''

while True:
    if max(number_as_string) == " ":
        break

    multiplier = number_as_string.count(max(number_as_string))
    max_number_possible += max(number_as_string) * multiplier
    number_as_string = number_as_string.replace(max(number_as_string), " ")


print(max_number_possible)