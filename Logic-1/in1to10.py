def in1to10(n, outside_mode):
    if outside_mode == True:
        return n <= 1 or n >= 10
    else:
        return 1<=n<=10