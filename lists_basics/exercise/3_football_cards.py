cards = input()

cards = cards.split()
team_a = []
team_b = []
flag = False

for card in cards:
    if "A" in card:
        team_a.append(card)
    elif "B" in card:
        team_b.append(card)
    if len(set(team_a)) > 4 or len(set(team_b)) > 4:
        flag = True
        break

print(f"Team A - {11 - len(set(team_a))}; Team B - {11 - len(set(team_b))}")
if flag:
    print("Game was terminated")
