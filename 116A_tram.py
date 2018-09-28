
stop = int(input())
p = []

for _ in range (stop):
    temp = list(map(int, input().split()))
    p.append(temp)

#stop = 4
#p = [[0, 3], [2, 5], [4, 2], [4, 0]]

p_sum = [0]

for i in range (stop):

    sum = p_sum[i] - p[i][0] + p[i][1]
    p_sum.append(sum)


print(max(p_sum))


