coin = int(input())
value = [int(x) for x in input().split()]

#value = [2, 5, 3, 2, 2]
value.sort(reverse=True)
#print(value)

out = 0
sum0 = 0
for i in range(len(value)):
    sum0 += value[i]
    sum1 = 0
    for j in range(i + 1, len(value)):
        sum1 += value[j]
    if sum1 < sum0:
        out = i + 1
        break
print(out)






