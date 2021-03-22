numbers = [int(num) for num in input().split()]
average = (sum(numbers) / len(numbers))
total = []
for num in numbers:
    if num > average:
        total.append(num)

total = sorted(total, reverse=True)
if len(total) == 0:
    print("No")
else:
    print(*total[:5])

