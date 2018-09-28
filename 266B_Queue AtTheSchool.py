ql = int(input())
sec = int(input())
que = list(input())


change = 0
for i in range (len(que) - 1):
    if que[i] == 'B' and que[i + 1] == 'G':
        i += 2
