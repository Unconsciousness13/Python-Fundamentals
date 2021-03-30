encrypt_message = input()
data = input()
while not data == "Decode":
    command = data.split("|")
    order = command[0]
    if order == "Move":
        moves = int(command[1])
        if moves in range(len(encrypt_message)):
            for_move = encrypt_message[:moves]
            rest = encrypt_message[moves:]
            encrypt_message = rest + for_move
    elif order == "Insert":
        index = int(command[1])
        value = command[2]
        if index in range(len(encrypt_message)+1):
            start = encrypt_message[:index]
            end = encrypt_message[index:]
            encrypt_message = start + value + end
    elif order == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in encrypt_message:
            encrypt_message = encrypt_message.replace(substring, replacement)
    data = input()
print(f"The decrypted message is: {encrypt_message}")