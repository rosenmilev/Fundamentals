import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
needed_budget = 0
apron_needed = 0

eggs = 10 * egg_price


for student in range(1, students + 1):
    needed_budget += eggs + apron_price
    apron_needed += 1
    if student % 5 == 0:
        continue
    else:
        needed_budget += flour_price

additional_aprons = math.ceil(apron_needed * 0.2) * apron_price
needed_budget += additional_aprons

if needed_budget <= budget:
    print(f"Items purchased for {needed_budget:.2f}$.")
else:
    print(f"{(needed_budget - budget):.2f}$ more needed.")
