n = int(input())
counter = 0
suma = 0
cha = input()
while counter != n:
    counter += 1

    suma += ord(cha)
    if counter == n:
        print(f"The sum equals: {suma}")
        break
    cha = input()


