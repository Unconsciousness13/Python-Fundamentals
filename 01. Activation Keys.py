activation_key = input()
while True:
    command = input().split(">>>")
    action = command[0]
    if action == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    elif action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        transform = command[1]
        start = int(command[2])
        end = int(command[3])
        if transform == "Upper":
            left = activation_key[:start]
            right = activation_key[end:]
            cuted = activation_key[start:end]
            activation_key = left + cuted.upper() + right
            print(activation_key)

        if transform == "Lower":
            left = activation_key[:start]
            right = activation_key[end:]
            cuted = activation_key[start:end]
            activation_key = left + cuted.lower() + right
            print(activation_key)
    elif action == "Slice":
        starta = int(command[1])
        enda = int(command[2])
        lefta = activation_key[:starta]
        righta = activation_key[enda:]
        activation_key = lefta + righta
        print(activation_key)
