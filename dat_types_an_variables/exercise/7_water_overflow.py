# number_of_lines = int(input())
# liters_poured = 0
# capacity_left = 250
#
# for i in range(number_of_lines):
#     liters = int(input())
#     if liters <= 255 - liters_poured:
#         liters_poured += liters
#         capacity_left = capacity_left - liters
#     else:
#         print("Insufficient capacity!")
#
# print(liters_poured)

number_of_lines = int(input())
capacity = 0

for _ in range(number_of_lines):
    liters_of_water = int(input())
    if liters_of_water + capacity <= 255:
        capacity += liters_of_water
        continue

    print("Insufficient capacity!")