q = int(input())

room = []
flag = 0

for i in range(q):
    data = list(map(int, input().split()))
    room.append(data)
for i in range(q):
    if room[i][1] - room[i][0] >= 2:
        flag += 1

print(flag)
