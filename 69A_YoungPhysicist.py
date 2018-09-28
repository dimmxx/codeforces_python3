vectors = int(input())

forces = []

for i in range(vectors):
    data = list(map(int, input().split()))
    forces.append(data)

x = 0
y = 0
z = 0

for i in range(vectors):
    x += forces[i][0]
    y += forces[i][1]
    z += forces[i][2]

if x != 0 or y != 0 or z != 0:
    print("NO")
else:
    print("YES")
