num = int(input())

if num % 4  == 0 or num % 7 == 0 or num % 47 == 0:
    print("YES")
else:
    num = str(num)
    flag = "NO"
    for i in num:
        if i == "4" or i == "7":
            flag = "YES"
        else:
            flag = "NO"
            break
    print(flag)

