targets_sequence = [int(x) for x in input().split(' ')]

while True:
    tokens = input().split(' ')
    command = tokens[0]
    index = 0
    value = 0

    if command == "Shoot":
        index = int(tokens[1])
        value = int(tokens[2])

        if 0 <= index < len(targets_sequence):
            targets_sequence[index] -= value

            if targets_sequence[index] <= 0:
                targets_sequence.pop(index)

    elif command == "Add":
        index = int(tokens[1])
        value = int(tokens[2])

        if 0 <= index < len(targets_sequence):
            targets_sequence.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        index = int(tokens[1])
        radius = int(tokens[2])

        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets_sequence):
            del targets_sequence[start: end + 1]
        else:
            print("Strike missed!")

    elif command == "End":
        targets_sequence = [str(x) for x in targets_sequence]
        print("|".join(targets_sequence))
        break
