#creature = input()

creature = ["a","f", "b", "c", "d", "a", "c", "e", "d", "f", "e"]

def distinct(word):
    unique = []
    for item in word:
        if item not in unique:
            unique.append(item)
    return unique

def chat(name):
    if len(distinct(name)) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


print(chat(creature))