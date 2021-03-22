import math


def calculate_distance(x1, y1, x2=0, y2=0):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

line_one_len = calculate_distance(x1, y1, 0, 0)
line_two_len = calculate_distance(x3, y3, 0, 0)

if line_one_len >= line_two_len:
    if calculate_distance(x1, y1) <= calculate_distance(x2, y2):
        print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
    else:
        print(f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")

else:

    if calculate_distance(x3, y3) <= calculate_distance(x4, y4):
        print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")

    else:
        print(f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})")
