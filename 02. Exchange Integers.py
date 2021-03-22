# Python program to swap two variables

a = int(input())
b = int(input())


temp = a
a = b
b = temp
print("Before:")
print(f"a = {temp}")
print(f"b = {a}")
print("After:")
print(f"a = {a}")
print(f"b = {b}")
