cards_deck = input().split(":")
new_list = []
command = input().split()
while not command == "Ready":

    if command[0] == "Add":
        card = command[1]
        if card in cards_deck:
            new_list.append(card)
        else:
            print("Card not found.")
    elif command[0] == "Insert":
        card, index = command[1], int(command[2])
        if card in cards_deck and 0 <= index < len(new_list):
            new_list.insert(index, card)
        else:
            print("Error!")
    elif command[0] == "Remove":
        card = command[1]
        if card in new_list:
            new_list.remove(card)
        else:
            print("Card not found.")
    elif command[0] == "Swap":
        card1, card2 = command[1], command[2]
        a, b = new_list.index(card1), new_list.index(card2)
        new_list[b], new_list[a] = new_list[a], new_list[b]

    elif command[0] == "Shuffle" and command[1] == "deck":
        new_list = [ca for ca in reversed(new_list)]
    command = input().split()
    if command[0] == "Ready":
        print(" ".join(new_list))
        break
