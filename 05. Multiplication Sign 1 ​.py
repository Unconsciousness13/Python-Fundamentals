from functools import reduce
one = int(input())
two = int(input())
three = int(input())
lista = []
lista.append(one)
lista.append(two)
lista.append(three)
result = reduce((lambda x, y: x * y), lista)
if result == 0:
    print("zero")
elif result > 0:
    print("positive")
else:
    print("negative")
