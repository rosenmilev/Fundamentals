first_row = input().split()
second_row = input().split()
third_row = input().split()

field = list()
field.append(first_row)
field.append(second_row)
field.append(third_row)
winner = ""
current_checked_sequence = []

for row in field:
    if len(set(row)) == 1:
        winner = row[0]

for column in range(3):
    for col in range(3):
        current_checked_sequence.append(field[col][column])
    if len(set(current_checked_sequence)) == 1:
        winner = current_checked_sequence[0]
    current_checked_sequence.clear()

for diag_1 in range(3):
    current_checked_sequence.append(field[diag_1][diag_1])
if len(set(current_checked_sequence)) == 1:
    winner = current_checked_sequence[0]
current_checked_sequence.clear()

for diag_2 in range(3):
    current_checked_sequence.append(field[diag_2][2 - diag_2])
if len(set(current_checked_sequence)) == 1:
    winner = current_checked_sequence[0]

if winner == "2":
    print("Second player won")
elif winner == "1":
    print("First player won")
else:
    print("Draw!")
