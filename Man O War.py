pirate_ship = [int(num) for num in input().split(">")]
# pirate_ship = list(map(int, input().split(">")))
warship = [int(num) for num in input().split(">")]
max_health = int(input())

is_sunken = False
while True:
    command = input().split()
    if command[0] == "Retire":
        break
    if command[0] == "Fire":
        index, damage = int(command[1]), int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunken = True
                break

    elif command[0] == "Defend":
        start_index, end_index, damage = int(command[1]), int(command[2]), int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship) and damage > 0:
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunken = True
                    break

    elif command[0] == "Repair":
        index, health = int(command[1]), int(command[2])
        if 0 <= index < len(pirate_ship) and health > 0:
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif command[0] == "Status":
        weaked = 0
        lower = max_health * 0.20
        for hp in pirate_ship:
            if hp < lower:
                weaked += 1
        print(f"{weaked} sections need repair.")
if not is_sunken:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")