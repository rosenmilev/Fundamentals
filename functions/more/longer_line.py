import math


def center_point(x_1, y_1, x_2, y_2):
    if abs(x_1) + abs(y_1) > abs(x_2) + abs(y_2):
        points = [x_2, y_2, x_1, y_1]
    else:
        points = [x_1, y_1, x_2, y_2]

    return points


def calculating_line_length(x_1, y_1, x_2, y_2):

    d = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

    return d


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

if calculating_line_length(x_1, y_1, x_2, y_2) >= calculating_line_length(x_3, y_3, x_4, y_4):
    points_order = list(map(int, center_point(x_1, y_1, x_2, y_2)))
else:
    points_order = list(map(int, center_point(x_3, y_3, x_4, y_4)))


print(f"({points_order[0]}, {points_order[1]})({points_order[2]}, {points_order[3]})")
