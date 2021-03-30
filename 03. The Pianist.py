n = int(input())
composers = {}
for inputs in range(n):
    data = input()
    piece, composer, key = data.split("|")
    composers[piece] = {'composer': composer, 'key': key}
command = input()
while not command == "Stop":
    splited = command.split("|")
    order = splited[0]
    piece = splited[1]
    if order == "Add":
        composer = splited[2]
        key = splited[3]
        if piece  in composers:
            print(f"{piece} is already in the collection!")
        else:
            composers[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif order == "Remove":
        if piece in composers:
            del composers[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif order == 'ChangeKey':
        new_piece = splited[2]
        if piece in composers:
            composers[piece]['key'] = new_piece
            print(f"Changed the key of {piece} to {new_piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()
sorted_comp = sorted(composers.items(), key=lambda x: (x[0]))
for composer,items in sorted_comp:
    print(f"{composer} -> Composer: {items['composer']}, Key: {items['key']}")