word = input()


def run(item):
     for i in item:
        if i == "H" or i == "Q" or i == "9":
             return "YES"
     return "NO"


print (run(word))