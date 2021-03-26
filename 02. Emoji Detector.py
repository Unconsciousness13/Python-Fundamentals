import re

string = input()
pattern = r'(?P<word>(\*\*|::)[A-Z][a-z]{2,}(\2))'
threshold = r'[0-9]+'
word_list = []
cool = []
not_cool = []
limit = 1
word_sum = 0
cool_threshold = ''
for word in re.finditer(pattern, string):
    words = word.group('word')
    word_list.append(words)
for num in re.findall(threshold, string):
    cool_threshold += num
cool_threshold = list(cool_threshold)
for idx in range(len(cool_threshold)):
    limit *= int(cool_threshold[idx])
for index in range(len(word_list)):

    for el in word_list[index]:
        if el.isalpha():
            word_sum += ord(el)
            if word_sum > limit:
                cool.append(word_list[index])
            else:
                not_cool.append(word_list[index])
    word_sum = 0
cool = list(dict.fromkeys(cool))
print(f"Cool threshold: {limit}")
print(f"{len(word_list)} emojis found in the text. The cool ones are:")
for cooli in cool:
    print(cooli)