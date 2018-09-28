group = int(input())
inp = list(map(int, input().split(" ")))

#imp = [int(x) for x in input().split(" ")]
#print(imp)
#inp = [1, 2, 4, 3, 3]

one = []
two = []
three = []
four = []

for num in inp:
    if num == 4:
        four.append(num)
    if num == 3:
        three.append(num)
    if num == 2:
        two.append(num)
    if num == 1:
        one.append(num)

def taxi_4():
    return len(four)

def taxi_3():
    taxi3 = 0
    for num in three:
        if len(one) != 0:
            one.pop()
        taxi3 += 1
    return taxi3

def taxi_2():
    if len(two) % 2 == 0:
        return len(two)/2
    else:
        if len(one) != 0:
            one.pop()
            if len(one) != 0:
               one.pop()
        return (len(two) - 1)/2 + 1

def taxi_1():
    if len(one) > 0 and len(one) < 4:
        return 1
    if len(one) % 4 == 0:
        return len(one)/4
    else:
        return len(one)/4  + 1

#print(taxi_4())
#print(taxi_3())
#print(taxi_2())
#print(taxi_1())

result = taxi_4() + taxi_3() + taxi_2() + taxi_1()



print(int(result))