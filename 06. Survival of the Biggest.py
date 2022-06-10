list_of_int = [int(x) for x in input().split()]
num = int(input())
count = 0
while count != num:
    for i in list_of_int:
        if count == num:
            break
        if int(i) <= min(list_of_int):
            list_of_int.remove(i)
            count += 1
print(', '.join(map(str, list_of_int)))
