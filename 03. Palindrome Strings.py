string = input().split()
searched_word = input()
palindromes = []
count = 0
for word in string:
    if word == searched_word:
        count += 1
    if word == "".join(reversed(word)):
        palindromes.append(word)
print(palindromes)
print(f"Found palindrome {count} times")