number_of_snowballs = int(input())
best_ball_characteristics = []
best_ball_result = 0

for ball in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    result = (weight / time) ** quality

    if result > best_ball_result:
        best_ball_result = result
        best_ball_characteristics = [weight, time, quality]

print(f"{best_ball_characteristics[0]} : {best_ball_characteristics[1]} = {int(best_ball_result)} "
      f"({best_ball_characteristics[2]})")
