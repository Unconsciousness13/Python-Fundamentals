usernames = input().split(", ")
tire = "-"
dolna = "_"
for word in usernames:
    if 2 < len(word) <= 16:
        if tire in word or word.isalpha() or word.isalnum() or dolna in word:
            print(word)