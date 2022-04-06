initial_energy = int(input())
battles_won = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {battles_won}. Energy left: {initial_energy}" )
        break
    distance = int(distance)
    if distance <= initial_energy:
        initial_energy -= distance
        battles_won += 1
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break
    if battles_won % 3 == 0 and battles_won > 0:
        initial_energy += battles_won
