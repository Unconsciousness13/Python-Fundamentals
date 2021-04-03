email = input()
data = input()
username = ''
encrypted = []
while not data == "Complete":
    splited = data.split(" ")
    com = data[0]
    if data == "Make Upper":
        email = email.upper()
        print(email)
    elif data == "Make Lower":
        email = email.lower()
        print(email)
    elif splited[0] == "GetDomain":
        index = int(splited[1])
        cut = email[-index:]
        print(cut)
    elif data == "GetUsername":
        if "@" in email:
            for el in email:
                if el == "@":
                    break
                username += el
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif splited[0] == "Replace":
        a = splited[1]
        b = "-"
        email = email.replace(a, b)
        print(email)
    elif data == "Encrypt":
        for _ in email:
            encrypted.append(ord(_))
        print(*encrypted)
    data = input()
