
def string_splosion(str):
    new = ''
    for i in range(len(str)):
        new = new + str[:i+1]
    return new