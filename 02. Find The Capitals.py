word = input()

lst = []

for index, w in enumerate(word):
    if w.isupper():
        lst.append(index)

print(lst)