def lucky_sum(a, b, c):
    new = [a,b,c]
    count = 0
    if 13 in new:
        new = new.remove(13)
    for i in new:
        count += i
    return count
print(lucky_sum(13,2,13))