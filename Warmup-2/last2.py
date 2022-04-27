def last2(str):
    new = str[len(str)-2:]
    count = 0
    if len(str) < 2:
        return 0
    for i in range(len(str)-2):
        sub = str[i:i+2]
        if sub == new:
            count = count + 1
    return count