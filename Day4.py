def ValidPassword(password):

    double = False
    decrease = False
    setNum = int(password[0])

    for i in range(1, 6):
        check = int(password[i])
        if check == setNum:
            double = True
        if check < setNum:
            decrease = True
        setNum = check

    if decrease == False and double == True:
        return True
    else:
        return False


def DoubleCheck(password):

    double = 0
    num1 = int(password[0])
    num2 = int(password[1])
    num3 = int(password[2])
    num4 = int(password[3])
    num5 = int(password[4])
    num6 = int(password[5])

    if num1 == num2 and num1 != num3:
        double += 1
    if num2 == num3 and num2 != num1 and num2 != num4:
        double += 1
    if num3 == num4 and num3 != num2 and num3 != num5:
        double += 1
    if num4 == num5 and num4 != num3 and num4 != num6:
        double += 1
    if num5 == num6 and num5 != num4:
        double += 1

    if double >0:
        return True
    else:
        return False


rangeStart = 240920
rangeEnd = 789857 + 1

count = 0

for i in range(rangeStart, rangeEnd):
    check = ValidPassword(str(i))
    check2 = DoubleCheck(str(i))
    if check and check2:
        count += 1
print(count)
