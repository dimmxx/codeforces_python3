
word = input()
#word = "pnnepelqomhhheollvlo"
template = ["h", "e", "l", "l", "o"]

def chat():
   for i in word:
       if len(template) != 0:
           if i == template[0] and len(template) != 1:
               del template[0]
           elif i == template[0] and len(template) == 1:
               return "YES"
       else:
           return "YES"
   return "NO"


print(chat())