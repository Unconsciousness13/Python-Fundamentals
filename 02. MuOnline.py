init_health = 100
bitcoins = 0
room_count = 0
dungeon_rooms = list(input().split("|"))
for room in dungeon_rooms:
    room_count += 1
    room = room.split(" ")
    command, value = room[0], int(room[-1])
    if command == "potion":
        if init_health < 100:
            init_health += value
            if init_health > 100:
                diff = abs(init_health - value - 100)
                print(f"You healed for {diff} hp.")
                init_health = 100
            else:
                print(f"You healed for {value} hp.")
        else:
            print(f"You healed for 0 hp.")
        print(f"Current health: {init_health} hp.")
    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        init_health -= value
        if init_health > 0:
            print(f"You slayed {command}.")

        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            break

    if room_count == len(dungeon_rooms):
        print(f"You've made it!")
        print(f"Bitcoins: {bitcoins}")
        print(f"Health: {init_health}")
        break
