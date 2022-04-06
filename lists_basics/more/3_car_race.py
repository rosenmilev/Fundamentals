sequence = input().split()
left_car_time = 0
right_car_time = 0
winner = ""
winner_time = 0

left_car = sequence[:int(len(sequence) / 2)]
right_car = sequence[int(len(sequence) / 2) + 1:]
right_car.reverse()

for time in left_car:
    if time == "0":
        left_car_time -= left_car_time * 0.2
    left_car_time += int(time)

for time in right_car:
    if time == "0":
        right_car_time -= right_car_time * 0.2
    right_car_time += int(time)

if left_car_time > right_car_time:
    winner = "right"
    winner_time = right_car_time
elif left_car_time < right_car_time:
    winner = "left"
    winner_time = left_car_time

print(f"The winner is {winner} with total time: {winner_time:.1f}")
