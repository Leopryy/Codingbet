def lucky_sum(a, b, c):
    lst = [a,b,c]
    hi = 0
    for i in range(len(lst)):
        if lst[i] != 13:
            hi += lst[i]
        elif lst[i] == 13:
            break
    return hi