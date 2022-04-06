import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0

for student in range(number_of_students):
    current_attendance = int(input())
    current_bonus = current_attendance / number_of_lectures * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        max_attendance = current_attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
