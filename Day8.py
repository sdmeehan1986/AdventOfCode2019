import numpy


def getInput():
    data = open('AoC_Data/day8.txt').read()
    return data


data = getInput()
layers = []

for i in range(0, 15000, 150):
    temp = data[i:(i + 150)]
    layers.append(temp)

zeros = 151
layer = ''
for i in range(0, len(layers)):
    data = layers[i]
    count = 0
    for i in data:
        if int(i) == 0:
            count += 1
    if count < zeros:
        zeros = count
        layer = data

ones = layer.count('1')
twos = layer.count('2')

print(f'Ones times twos = {ones * twos}')

position = 0
text = []
while position < 150:
    for i in layers:
        if i[position] == '1' or i[position] == '0':
            text.append(i[position])
            position += 1
            break
num = numpy.array(text).reshape(6, 25)
for i in num:
    for j in i:
        if j == '1':
            print('# ', end='')
        if j == '0':
            print('  ', end='')
    print()
