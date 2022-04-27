def string_bits(str):
    new1 = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new1 = new1 + str[i]
    return new1

print(string_bits('hello'))