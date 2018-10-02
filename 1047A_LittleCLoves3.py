import random

number = int(input())

number1 = random.randint(0, number)
if number1 % 3 == 0:
    number1 += 1

number2 = random.randint(0, number - number1)
if number2 % 3 == 0:
    number2 += 1

number3 = number - number1 - number2
if number3 % 3 == 0 or number3 < 0:
    number1 = 1
    number2 = 1
    number3 = number - 2
    if number3 % 3 == 0:
       number3 -= 1
       number1 += 1


print(number1, number2, number3)

