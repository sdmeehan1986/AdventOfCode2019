def file_data(file):

    with open(file, '+r') as file:
        data = file.read().splitlines()

    return data


def day2(data):

    for i in range(0, len(data), 4):
        num0 = int(data[i])
        num1 = int(data[i + 1])
        num2 = int(data[i + 2])
        num3 = int(data[i + 3])

        if num0 == 99:
            break
        elif num0 == 1:
            temp = int(data[num1]) + int(data[num2])
            data[num3] = temp
        elif num0 == 2:
            temp = int(data[num1]) * int(data[num2])
            data[num3] = temp

    return data


def day2_b(data, num1, num2):

    data[1] = num1
    data[2] = num2

    check = day2(data)
    if int(check[0]) == 19690720:
        print(check[0])
        return True


def day2_call():
    temp_data = file_data('AoC_Data/day2.txt')
    data = temp_data[0].split(',')
    print(day2(data)[0])

    end_value = 0
    check = False
    for i in range(0, 100):
        for j in range(0, 100):
            data = temp_data[0].split(',')
            if day2_b(data, i, j):
                print(f'i is {i} and j is {j}')
                end_value = 100 * i + j
                check = True
                break
        if check:
            break

    print(end_value)


day2_call()
