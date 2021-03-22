import math
n = int(input())  # number persons
p = int(input())  # capacity of persons
courses = math.ceil(n / p)
print(courses)