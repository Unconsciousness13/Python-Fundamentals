rooms = int(input())
total_free_chairs = 0
room = 0
every_room = 0
for com in range(rooms):
    command = input().split(" ")
    chairs = len(command[0])
    taken = int(command[1])
    room += 1
    if chairs > taken:
        free_chairs = chairs - taken
        total_free_chairs += free_chairs
        every_room += 1
    elif chairs < taken:
        print(f"{int(taken - chairs)} more chairs needed in room {room}")
    else:
        every_room += 1
if every_room == room:
    print(f"Game On, {total_free_chairs} free chairs left")
