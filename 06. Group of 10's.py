numbers = [int(num) for num in input().split(", ")]
# numbers = list(map(int, input().split(", ")))
# numbers = list(map(lambda x: int(x), input().split(", ")))
group = 10
while numbers:
    new_list = []
    for number in numbers:
        if number in range(group - 10, group + 1):
            new_list.append(number)
    for num in new_list:
        numbers.remove(num)
    print(f"Group of {group}'s: {new_list}")
    group += 10



