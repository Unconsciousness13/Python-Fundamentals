n = int(input())
el_list = []
for electrons in range(1, n + 1):
    max_electrons = 2 * (electrons ** 2)
    el_list.append(max_electrons)
    if sum(el_list) == n:
        print(el_list)
        break
    if sum(el_list) > n:
        el_list.pop()
        last_num = abs(n - sum(el_list))
        el_list.append(last_num)
        print(el_list)
        break


