d = int(input())
b = int(input())

for num in range(b,d,-1):
    if num <= b:
        if num % d == 0:
            if num > 0:
                print (num)
                break