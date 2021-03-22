# def tribonacci(signature, n):
#     res = signature[:n]
#     for i in range(n - 3):
#         res.append(sum(res[-3:]))
#         print(res)
#
#
# num = input()
# tribonacci(signature ,n)
def first_func(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return first_func(n - 1) + first_func(n - 2) + first_func(n - 3)


num = int(input())
if num > 0:
    for i in range(1, num + 1):
        print(first_func(i), end=" ")

first_func(num)