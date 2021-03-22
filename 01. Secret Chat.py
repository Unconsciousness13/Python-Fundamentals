message = input()
while True:
    command = input().split(":|:")
    order = command[0]
    if order == "Reveal":
        print(f"You have a new text message: {message}")
        break

    if order == "InsertSpace":
        message = message[:int(command[1])] + " " + message[int(command[1]):]
        print(message)
    elif order == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")

    elif order == "ChangeAll":
        first, second = command[1], command[2]
        if first in message:
            message = message.replace(first, second)
            print(message)
