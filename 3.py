data = input()
peoples = {}
while not data == "Results":
    splited = data.split(":")
    com = splited[0]
    if com == "Add":
        person_name = splited[1]
        health = int(splited[2])
        energy = int(splited[3])
        if person_name in peoples:
            peoples[person_name]['health'] += health
            peoples[person_name]['energy'] += energy
        else:
            peoples[person_name] = {"health": health, 'energy': energy}
    elif com == "Attack":
        attacker = splited[1]
        defender = splited[2]
        damage = int(splited[3])
        if attacker in peoples:
            if defender in peoples:
                peoples[defender]['health'] -= damage
                peoples[attacker]['energy'] -= 1
                if peoples[defender]['health'] <= 0:
                    print(f"{defender} was disqualified!")
                    del peoples[defender]
                if peoples[attacker]['energy'] <= 0:
                    print(f"{attacker} was disqualified!")
                    del peoples[attacker]
    elif com == "Delete":
        user = splited[1]
        if user == "All":
            if peoples:
                peoples.clear()
        else:
            if user in peoples:
                del peoples[user]
    elif data == "Delete All":
        if peoples:
            peoples.clear()

    data = input()
# print(f"People count: {len(peoples)}")
# if peoples:
#     sorted_peop = sorted(peoples.items(), key=lambda x: (-x[1]['health'], x[0]))
#     for name, stats in sorted_peop:
#         print(f"{name} - {stats['health']} - {stats['energy']}")
# # for name, stats in sorted(peoples.items(), key=lambda x: (-x[1]['health'], x[0])):
# #     print(f"{name} - {stats['health']} - {stats['energy']}")
# # for p in peoples:
# #     print(f"{p} - {peoples[p]['health']} - {(peoples[p]['energy'])}")
print(f'People count: {len(peoples)}')
person_records = dict(sorted(peoples.items(), key=lambda x: (-x[1]['health'], x[0])))
for key, value in person_records.items():
    print(f'{key} - {value["health"]} - {value["energy"]}')