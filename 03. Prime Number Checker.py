n = int(input())
if n == 1:
    print(False)
elif n == 2:
    print(True)
for x in range(2, n):
    if n % x == 0:
        print(False)
        break
else:
    print(True)
