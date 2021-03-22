sequence_of_elements = input().split()
counter = 0
command = input()
while not command == "end":
    sep = command.split()
    first, second = int(sep[0]), int(sep[1])
    counter += 1
    if 0 <= first < len(sequence_of_elements) and 0 <= second < len(sequence_of_elements):
        if sequence_of_elements[first] == sequence_of_elements[second]:
            first_value = sequence_of_elements[first]
            second_value = sequence_of_elements[second]
            print(f"Congrats! You have found matching elements - {first_value}!")

            sequence_of_elements.remove(first_value)
            sequence_of_elements.remove(second_value)

        else:
            print("Try again!")
    else:
        print("Invalid input! Adding additional elements to the board")
        half = int(len(sequence_of_elements) / 2)
        a = str(-counter) + "a"
        sequence_of_elements.insert(half, a)
        sequence_of_elements.insert(half, a)

    if len(sequence_of_elements) == 0 or len(sequence_of_elements) == 1:
        break

    command = input()

if len(sequence_of_elements) > 1:
    print(f"Sorry you lose :(")
    print(*sequence_of_elements)
else:
    print(f"You have won in {counter} turns!")
