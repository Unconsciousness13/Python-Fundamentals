text = input()
while True:
    line = input().split(':')
    command = line[0]
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {text}")
        break
    elif command == "Add Stop":
        index = int(line[1])
        string = line[2]
        if index in range(len(text)):
            text = text[:index] + string + text[index:]
        print(text)
    elif command == 'Remove Stop':
        start = int(line[1])
        end = int(line[2])
        if start in range(len(text)) and end in range(len(text)):
            text = text[:start] + text[end + 1:]
        print(text)
    elif command == "Switch":
        old = line[1]
        new = line[2]
        if old in text:
            text = text.replace(old, new)
        print(text)