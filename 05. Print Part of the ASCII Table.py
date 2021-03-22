first = int(input())
second = int(input())
sum = ""
for char in range(first, second + 1):
    stri = chr(char)
    sum += (stri + " ")
print(sum)
