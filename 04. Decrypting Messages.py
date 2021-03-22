key = int(input())
n = int(input())
char = input()
counter = 0
bukva = 0
keyword = ""
while not counter  == n:
    bukva = (ord(char) + key)
    bukva = chr(bukva)
    keyword += bukva
    counter +=1
    if counter == n:
        print(keyword)
        break
    char = input()