def func_bar(num):
    num = num //10
    bar = ".........."
    if num == 10:
        print(f"{num * 10}% Complete!")
        print("[%%%%%%%%%%]")
        exit()
    if num == 1:
        bar = "[%.........]"
    elif num == 2:
        bar = "[%%........]"
    elif num == 3:
        bar = "[%%%.......]"
    elif num == 4:
        bar = "[%%%%......]"
    elif num == 5:
        bar = "[%%%%%.....]"
    elif num == 6:
        bar = "[%%%%%%....]"
    elif num == 7:
        bar = "[%%%%%%%%...]"
    elif num == 8:
        bar = "[%%%%%%%%..]"
    elif num == 9:
        bar = "[%%%%%%%%%.]"
    print(f"{num * 10}% {bar}")
    print("Still loading...")
    return num


number = int(input())
func_bar(number)
