moves = input().split("@")
command = input()
houses = []
already_day = []
removed = 0
previous_building = 0
building = 0
failed = 0
for house in moves:
    houses.append(int(house))
while not command == "Love!":
    # if command == "Love!":
    #     break

    com, value = command.split()
    building = int(value) + previous_building
    if building > len(houses) - 1:
        building = 0
        previous_building = 0
    houses[building] -= 2
    if houses[building] < 0:
        houses[building] = 0
    previous_building = building

    if houses[building] == 0:
        if building in already_day:
            print(f"Place {building} already had Valentine's day.")
        else:
            print(f"Place {building} has Valentine's day.")
            removed += 1
            already_day.append(building)

            # if len(already_day) == len(houses):
            #     print(f"Cupid's last position was {building}.")
            #     print("Mission was successful.")
            #     break

    command = input()
print(f"Cupid's last position was {building}.")
for check in houses:
    if int(check) > 0:
        failed += 1

if failed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")