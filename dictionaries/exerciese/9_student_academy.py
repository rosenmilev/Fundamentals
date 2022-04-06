
number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    student = input()

    if student not in students:
        students[student] = []

    grade = float(input())
    students[student].append(grade)

students = {key: value for key, value in students.items() if sum(value) / len(value) >= 4.50}

for key, value in students.items():
    average_grade = sum(value) / len(value)

    print(f"{key} -> {average_grade:.2f}")
