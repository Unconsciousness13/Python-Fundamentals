n = int(input())
for a in range (n):
    for b in range(n):
        for c in range(n):
            print(f"{chr(97+a)}{chr(97+b)}{chr(97+c)}")