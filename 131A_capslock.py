#word = input()

word = "S"


def analyze(item):
    temp = 0
    for i in item:
        if i.isupper():
            temp += 1
    return temp


def normalize(item):
    if len(word) == 1 and item.islower():
        return item.upper()
    elif len(item) == 1 and item.isupper():
        return item.lower()
    elif item[0].islower() and len(item) == (analyze(item) + 1):
        return item[0].upper() + item[1:].lower()
    elif len(item) == analyze(item):
        return item.lower()
    return item


print (normalize(word))