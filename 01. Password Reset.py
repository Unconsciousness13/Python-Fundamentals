old_password = input()
data = input()

new_password = ''
while not data == "Done":

    splited = data.split(" ")
    if data == "TakeOdd":
        for el in range(len(old_password)):
            if el % 2 == 1:
                new_password += old_password[el]
        old_password = new_password
        print(new_password)
    elif splited[0] == "Cut":
        index, length = int(splited[1]), int(splited[2])
        if 0 <= index+length < len(new_password):
            left = new_password[:index]
            right = new_password[index + length:]
            new_password = left + right
            print(new_password)
    elif splited[0] == "Substitute":
        look = splited[1]
        if look in new_password:
            while look in new_password:
                new_password = new_password.replace(splited[1], splited[2])
            print(new_password)
        else:
            print("Nothing to replace!")
    old_password = new_password
    data = input()
print(f"Your password is: {new_password}")


# def take_odd(s: str) -> str:
#     """Takes only the characters at odd indices and concatenates them together to obtain the new raw password.
#     Args:
#         s (str): Raw password
#     Returns:
#         str: Changed password
#     """
#     odds = ''
#     for i, c in enumerate(s):
#         if i % 2 != 0:
#             odds += c
#     return odds
#
#
# def cut(s: str, i: int, l: int) -> str:
#     """Gets the substring with the given length starting from the given index from the password and removes its first occurrence of it. The given index and length will always be valid.
#     Args:
#         s (str): Raw password
#         i (int): index
#         l (int): length
#     Returns:
#         str: Changed password
#     """
#     substring = s[i:i+l]
#     s = s.replace(substring, '', 1)
#     return s
#
#
# def substitute(s: str, o: str, n: str) -> tuple:
#     """If the raw password contains the given substring, replaces all of its occurrences with the substitute text given.
#     Args:
#         s (str): Raw password
#         o (str): Old phrase
#         n (str): New phrase
#     Returns:
#         tuple: (Changed password, True if changed | False if not)
#     """
#     if o in s:
#         while o in s:
#             s = s.replace(o, n)
#             return s, True
#     return s, False
#
#
# s = input()
#
# while True:
#     data = input()
#     if data == 'Done':
#         break
#     command = data.split()[0]
#     if command == 'TakeOdd':
#         s = take_odd(s)
#         print(s)
#     if command == 'Cut':
#         index = int(data.split()[1])
#         length = int(data.split()[2])
#         s = cut(s, index, length)
#         print(s)
#     if command == 'Substitute':
#         old = data.split()[1]
#         new = data.split()[2]
#         s, changed = substitute(s, old, new)
#         if changed:
#             print(s)
#         else:
#             print('Nothing to replace!')
#
# print(f'Your password is: {s}')