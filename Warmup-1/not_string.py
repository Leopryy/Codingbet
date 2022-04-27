def not_string(str):
    if "not" in str.lower():
        return str
    else:   
        return f'Not {str}'

print(not_string('NOT candy'))