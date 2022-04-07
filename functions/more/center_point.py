import math


def center_point(x_1, y_1, x_2, y_2):
    if abs(x_1) + abs(y_1) > abs(x_2) + abs(y_2):
        points = [x_2, y_2, x_1, y_1]
    else:
        points = [x_1, y_1, x_2, y_2]

    return points


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

points_order = center_point(x_1, y_1, x_2, y_2)

print(f"({math.floor(points_order[0])}, {math.floor(points_order[1])})")
