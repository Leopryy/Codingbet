def pos_neg(a, b, negative):
    if negative == True:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


print(pos_neg(-4,5,True))