number = input().split(", ")
numbers = [int(num) for num in number]
minimum_wealth = int(input())
for num in range(len(numbers)):
    if numbers[num] < minimum_wealth:
        diff = minimum_wealth - numbers[num]
        max_num = max(numbers)
        if max_num - diff >= minimum_wealth:
            numbers[numbers.index(max_num)] -= diff
            numbers[num] += diff
if sum(numbers) >= len(numbers) * minimum_wealth:
    print(numbers)
else:
    print("No equal distribution possible")