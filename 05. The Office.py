employers = input().split(" ")
factor = int(input())
employers = list(map(lambda x: int(x) * factor, employers))
happy_employer = list(filter(lambda x: x >= sum(employers) / len(employers), employers))
if len(happy_employer) >= len(employers) / 2:
    print(f"Score: {len(happy_employer)}/{len(employers)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employer)}/{len(employers)}. Employees are not happy!")
