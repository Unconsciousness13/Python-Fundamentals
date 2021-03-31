import re

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
text = input()
while text:
    valid_emails = [el.group() for el in re.finditer(pattern, text)]
    if valid_emails:
        print(*valid_emails)
    text = input()
