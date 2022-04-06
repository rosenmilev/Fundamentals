n = int(input())

positive_numbers = []
negative_numbers = []
sum_of_negatives = 0

for num in range(n):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
        sum_of_negatives += number

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}\n"
      f"Sum of negatives: {sum_of_negatives}")


# Second way(better):
#
# n = int(input())
#
# positives_list = []
# negatives_list = []
#
# for row in range(n):
#     current_number = int(input())
#     if current_number >= 0:
#         positives_list.append(current_number)
#     else:
#         negatives_list.append(current_number)
#
# print(positives_list)
# print(negatives_list)
# print(f"Count of positives: {len(positives_list)}\n"
#       f"Sum of negatives: {sum(negatives_list)}")
