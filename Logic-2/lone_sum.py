def lone_sum(a, b, c):
    if a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b ==c and a != b :
        return a
    elif a ==b and a== c:
        return 0
    else:
        return a+b+c