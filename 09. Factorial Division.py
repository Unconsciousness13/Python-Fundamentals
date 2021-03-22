import math


def fact(num, num2):
    num = math.factorial(num)
    num2 = math.factorial(num2)
    result = num / num2
    print(f"{result:.2f}")
    return num, num2, result


first = int(input())
second = int(input())
fact(first, second)
