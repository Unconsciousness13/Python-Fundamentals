initial_energy = int(input())
energy = initial_energy
command = input()
battle_counter = 0
while not command == "End of battle":
    converted_command = int(command)
    if energy - converted_command < 0:
        print(f"Not enough energy! Game ends with {battle_counter} won battles and {energy} energy")
        break
    battle_counter += 1
    energy -= converted_command

    if battle_counter % 3 == 0:
        energy += battle_counter

    command = input()
if command == "End of battle":
    print(f"Won battles: {battle_counter}. Energy left: {energy}")
