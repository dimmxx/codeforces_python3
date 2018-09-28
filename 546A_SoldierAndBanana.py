data = [int(x) for x in input().split()]

total = 0

for i in range(data[2]):
    total += data[0] * (i + 1)

if data[1] > total or data[1] == total:
    print(0)
else:
    print(total - data[1])


