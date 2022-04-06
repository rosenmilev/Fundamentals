def max_electrons_in_shell(position):
    max_electrons = 2 * (position ** 2)
    return max_electrons


number_of_electrons = int(input())
current_position = 0
electron_shells = []

while number_of_electrons > 0:
    current_position += 1
    current_maximum = max_electrons_in_shell(current_position)

    if current_maximum <= number_of_electrons:
        electron_shells.append(current_maximum)
        number_of_electrons -= current_maximum
    else:
        electron_shells.append(number_of_electrons)
        number_of_electrons = 0

print(electron_shells)
