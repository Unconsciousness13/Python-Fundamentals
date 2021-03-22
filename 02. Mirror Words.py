import re
word = input().split("@" or "#")
new_word = re.sub('[^A-Za-z0-9]+', '', word)

print(word)