def password_checker(text):
    Is_It = True
    text_count = 0
    digit_count = 0
    for f in text:
        text_count += 1
        if chr(48) <= f <= chr(57):
            digit_count += 1
    for f in text:
        if not chr(65) <= f <= chr(90) and not chr(97) <= f <= chr(122) and not chr(48) <= f <= chr(57):
            print("Password must consist only of letters and digits")
            Is_It = False
            break
    if text_count < 6 or text_count > 10:
        print("Password must be between 6 and 10 characters")
        Is_It = False

    if digit_count < 2:
        print("Password must have at least 2 digits")
        Is_It = False
    if Is_It == True:
        print("Password is valid")


password = input()
password_checker(password)
