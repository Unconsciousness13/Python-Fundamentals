people_waiting = int(input())
slots = list(map(int, input().split()))
for slot in range(len(slots)):
    while slots[slot] < 4:
        slots[slot] += 1
        people_waiting -= 1
        if people_waiting == 0 and sum(slots) / 4 == len(slots):
            print(*slots)
            break
        elif people_waiting == 0:
            print("The lift has empty spots!")
            print(*slots)
            break


if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*slots)