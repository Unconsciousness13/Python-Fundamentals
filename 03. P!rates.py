capitals = {}
command = input()
while not command == "Sail":
    name, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if name not in capitals:
        capitals[name] = {'population': population, 'gold': gold}
    else:
        capitals[name]['population'] += population
        capitals[name]['gold'] += gold
    command = input()
data = input()
while not data == "End":
    splited = data.split('=>')
    action = splited[0]
    if action == 'Plunder':
        name = splited[1]
        people = int(splited[2])
        gold = int(splited[3])
        if name in capitals:
            capitals[name]['population'] -= people
            capitals[name]['gold'] -= gold
            print(f"{name} plundered! {gold} gold stolen, {people} citizens killed.")
            if 0 >= capitals[name]['population'] or 0 >= capitals[name]['gold']:
                print(f"{name} has been wiped off the map!")
                del capitals[name]

    elif action == "Prosper":
        name = splited[1]
        gold = int(splited[2])
        if name in capitals:
            if gold >= 0:
                capitals[name]['gold'] += gold
                print(f"{gold} gold added to the city treasury. {name} now has {capitals[name]['gold']} gold.")

            else:
                print("Gold added cannot be a negative number!")

    data = input()
if not capitals:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f'Ahoy, Captain! There are {len(capitals)} wealthy settlements to go to:')
    for name, stats in sorted(capitals.items(), key=lambda x: (-x[1]['gold'], x[0])):
        print(f'{name} -> Population: {stats["population"]} citizens, Gold: {stats["gold"]} kg')
