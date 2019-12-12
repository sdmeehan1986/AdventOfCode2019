def file_data(file):

    with open(file, '+r') as file:
        data = file.read().splitlines()

    return data


def day1(num):

    part = int(num) / 3
    return int(part) - 2


def day1_call():
    data = file_data('AoC_Data/day1.txt')

    total1 = 0
    total2 = 0
    for i in data:
        temp = day1(i)
        total1 += temp

        temp2 = day1(temp)
        while temp2 > 0:
            total2 += temp2
            temp2 = day1(temp2)

    print(f'part 1 is {total1}')
    print(f'part 2 is {total1 + total2}')


day1_call()
