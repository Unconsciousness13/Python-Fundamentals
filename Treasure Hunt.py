initial_treasure_chest = input().split("|")
command = input()
counter = 0

while not command == "Yohoho!":
    splited = command.split()
    com = splited[0]

    splited = splited[1::]
    if com == "Loot":
        for el in splited:
            if el not in initial_treasure_chest:
                initial_treasure_chest.insert(0, el)
    elif com == "Drop":
        index = int(splited[-1])
        if 0 <= index <= len(initial_treasure_chest) -1 :
            to_add = initial_treasure_chest[index]
            initial_treasure_chest.pop(index)
            initial_treasure_chest.append(to_add)
    elif com == "Steal":
        index = int(splited[-1])
        stealed = initial_treasure_chest[-index::]
        del initial_treasure_chest[-index::]
        print(", ".join(stealed))
    command = input()
    if command == "Yohoho!":
        if len(initial_treasure_chest) < 1:
            print("Failed treasure hunt.")
        else:
            for el in initial_treasure_chest:
                counter += len(el)
            suma = counter / len(initial_treasure_chest)
            print(f"Average treasure gain: {suma:.2f} pirate credits.")