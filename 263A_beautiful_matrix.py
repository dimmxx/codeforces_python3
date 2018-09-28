matrix = []
for _ in range(5):
    temp = list(map(int, input().split()))
    matrix.append(temp)

#matrix  = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

row = 0
column = 0
move_row = 0
move_column = 0

for i in range(5):
    for j in range(5):

        if matrix[i][j] == 1:
            row = i
            column = j

if row == 0 or row == 4:
    move_row = 2
elif row == 1 or row == 3:
    move_row = 1
elif row == 0:
    move_row = 0

if column == 0 or column == 4:
    move_column = 2
elif column == 1 or column == 3:
    move_column = 1
elif column == 0:
    move_column = 0

print (move_column + move_row)

