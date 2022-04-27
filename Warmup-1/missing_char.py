def missing_char(str, n):
    new_lst = list(str)
    lst = new_lst.pop(n)
    return ''.join(new_lst)

print(missing_char('hihihi',1))