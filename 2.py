import re
pattern = r'(\!)(?P<word>[A-Z][a-z][a-z]+)\1\:(\[)(?P<title>[A-Za-z\s]{8,})(\])'
num = int(input())
titles = []
for n in range(num):
    text = input()
    match = re.findall(pattern,text)
    if match:
        for el in match:
            word = el[1]
            title = el[3]
            for w in title:
                titles.append(str(ord(w)))
            p = " ".join(titles)
            print(f"{word}: {p}")
    if not match:
        print("The message is invalid")
