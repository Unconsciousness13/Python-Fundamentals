def asci(one, two):
    text = ""
    for i in range(ord(one) + 1, ord(two)):
        text += chr(i) + " "
    return text


first = input()
second = input()
print(asci(first, second))
