def without_end(str):
    str1 = str.replace(str[0], "")
    if len(str1) <= 2:
        str2 = str1.replace(str1[0], "")
    else:
        str2 = str1.replace(str1[-1],'')
    return str2