food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())
enough = True

for day in range(1, 31):
    food -= 0.3
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= 1 / 3 * pig_weight
    if float(f"{food:.2f}") <= 0 or float(f"{hay:.2f}") <= 0 or float(f"{cover:.2f}") <= 0:
        enough = False
        print("Merry must go to the pet store!")
        break

if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
