def diff21(n):
    if n > 21:
        result = abs(n - 21) * 2
    else:
        result = abs(n - 21)
    return result

# print(diff21(19))
# print(diff21(10))
# print(diff21(21))