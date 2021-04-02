n = int(input())
negative = []
positive = []
for i in range (n):
    next = int(input())
    if next >= 0:
        positive.append(next)
    else:
        negative.append(next)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")