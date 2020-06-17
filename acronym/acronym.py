def abbreviate(words):
    tokens = words.replace("'", '').replace('-', ' ').replace('_', '').split()
    # tokens = words.split()
    result = ''
    for item in tokens:
        result += item[0].upper()
    return result