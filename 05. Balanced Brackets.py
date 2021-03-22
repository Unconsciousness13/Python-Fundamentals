n = int(input())
lastBracket = ""
balance = "BALANCED"
for i in range(1,n +1):
    currentInput = input()
    if currentInput == "(" and lastBracket == "(":
        balance = "UNBALANCED"
        break
    if currentInput == ")" and lastBracket != "(":
        balance = "UNBALANCED"
        break
    # if lastBracket == "(":
    #     balance = "UNBALANCED"
    if currentInput == "(" or currentInput == ")":
        lastBracket += currentInput
    if lastBracket == "()":
        lastBracket = ""
print(balance)


