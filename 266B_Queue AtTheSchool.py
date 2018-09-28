ql, sec = map(int, input().split())
que = list(input())

db = []

while sec > 0:
    for i in range(len(que) - 1):
         if que[i] == 'B' and que[i + 1] == 'G':
             db.append(i)

    for i in range(len(db)):
         temp = que[db[i]]
         que[db[i]] = que[db[i] + 1]
         que[db[i] + 1] = temp
    db =[]
    sec -= 1

print(''.join(que))


