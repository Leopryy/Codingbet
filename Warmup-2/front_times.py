def front_times(str, n):
    hi = list(str)
    hi1 = []
    for i in range(3):
        hi1.append(hi[i])
    new_word = ''.join(hi1)
    return new_word*n

print(front_times('Chocolate',9))