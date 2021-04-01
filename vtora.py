particle = input().split("|")
while True:
    command = (input().split())
    if command[0] == "Done":
        print(f"You crafted {''.join(particle)}!")
        break
    if command[0] == "Move":
        index = int(command[2])
        if command[1] == "Left":
            if 1 <= index < len(particle):
                current = particle[index]
                particle.pop(index)
                particle.insert(index - 1, current)

        elif command[1] == "Right":
            if 0 <= index < len(particle) - 1:
                current = particle[index]
                particle.pop(index)
                particle.insert(index + 1, current)

    elif command[0] == "Check":
        if command[1] == "Even":
            even = []
            for el in range(len(particle)):
                if el % 2 == 0:
                    founded = particle[el]
                    even.append(founded)
            print(*even)

        elif command[1] == "Odd":
            odd = []
            for el in range(len(particle)):
                if el % 2 == 1:
                    founded = particle[el]
                    odd.append(founded)
            print(*odd)