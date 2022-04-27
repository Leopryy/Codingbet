def string_match(a, b):
    count = 0
    minlen = min(len(a),len(b))
    for i in range(minlen-1):
        if a[i]+a[i+1] == b[i] +b[i+1]:
            count +=1
    return count