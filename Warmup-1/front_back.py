def front_back(str):
    lst = list(str)
    lst[0],lst[-1] = lst[-1],lst[0]
    return ''.join(lst)

print(front_back('code'))