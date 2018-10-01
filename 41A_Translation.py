word = input()
code = input()
code_m = []

for i in range(len(word) - 1, -1, -1):
    code_m.append(word[i])

code_m = ''.join(code_m)

if code_m == code:
    print('YES')
else:
    print('NO')