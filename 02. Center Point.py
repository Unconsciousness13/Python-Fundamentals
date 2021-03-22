import math


def cartesian(x1, y1, x2, y2):
    DistanceFromPointToCenter1 = math.sqrt(x1 * x1 + y1 * y1)
    DistanceFromPointToCenter2 = math.sqrt(x2 * x2 + y2 * y2)


    if DistanceFromPointToCenter1 < DistanceFromPointToCenter2:
        print(f"({int(x1)}, {int(y1)})")
    else:
        print(f"({int(x2)}, {int(y2)})")
    return x1, y1, x2, y2

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
cartesian(x1, y1, x2, y2)
