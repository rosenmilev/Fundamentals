type_of_fire = input()
water_available = int(input())

type_of_fire = type_of_fire.split("#")
effort = 0
extinguished_cells = []

for cell in type_of_fire:
    current_cell = cell.split()
    cell_number = int(current_cell[2])

    if cell_number > water_available:
        continue
    if current_cell[0] == "High" and 81 <= cell_number <= 125:
        water_available -= cell_number
    elif current_cell[0] == "Medium" and 51 <= cell_number <= 80:
        water_available -= cell_number
    elif current_cell[0] == "Low" and 1 <= cell_number <= 50:
        water_available -= cell_number
    else:
        continue
    effort += int(current_cell[2]) * 0.25
    extinguished_cells.append(cell_number)

print("Cells:")
for cel in extinguished_cells:
    print(f"- {cel}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(extinguished_cells)}")
