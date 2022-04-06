import math

first_employee, second_employee, third_employee = int(input()), int(input()), int(input())
number_of_students = int(input())
resting_hours = 0

total_students_per_hour = first_employee + second_employee + third_employee

total_hours = math.ceil(number_of_students / total_students_per_hour)

if total_hours > 3:
    if total_hours % 3 == 0:
        resting_hours -= 1
    resting_hours += total_hours // 3

print(f"Time needed: {total_hours + resting_hours}h.")
