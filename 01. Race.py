import re

name_pattern = r'[A-Za-z]+'
km_pattern = r'[0-9]+'
participants = input()
splited_part = participants.split(", ")
top_list = {}
for el in splited_part:
    if el not in top_list:
        top_list[el] = 0
command = input()
name = ''
numbers = []
while not command == "end of race":
    searched_name = re.findall(name_pattern, command)
    for el in searched_name:
        name += el
    searched_distance = re.findall(km_pattern, command)
    for el in searched_distance:
        num = int(el)
        numbers += el
    numbers = [int(el) for el in numbers]
    if name in top_list.keys():
        top_list[name] += sum(numbers)
    name = ''
    numbers = []

    command = input()
sorted_top_list = sorted(top_list.items(), key=lambda x: (-x[1]))
number = 1
for na in sorted_top_list:
    if number == 1:
        print(f"1st place: {na[0]}")
    if number == 2:
        print(f"2nd place: {na[0]}")
    if number == 3:
        print(f"3rd place: {na[0]}")
        break
    number += 1