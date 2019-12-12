from itertools import permutations


class IntcodeMachine:

    def __init__(self, data_string, input, inputPower, inputPhase):
        self.data = data_string
        self.input = input
        self.inputPower = inputPower
        self.phase = inputPhase
        self.output = None
        self.count = 0
        self.pos = 0

    def resetPos(self):
        self.pos = 0

    def updateInput(self, newInput):
        self.input = newInput

    def padder(self, code):
        while len(code) < 5:
            code = '0' + code
        return code

    def parameters(self, code):
        opcode = int(code[3:5])
        param1 = int(code[2])
        param2 = int(code[1])
        param3 = int(code[0])

        return [opcode, param1, param2, param3]

    def updatePowerPhase(self, power, phase):
        self.inputPower = power
        self.phase = phase

    def opcode1(self, params, position):
        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])

        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])

        num3 = int(self.data[position + 3])

        # print(f'{num1} : {num2} : {num3}')
        self.data[num3] = str(num1 + num2)

    def opcode2(self, params, position):
        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])

        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])

        num3 = int(self.data[position + 3])

        # print(f'{num1} : {num2} : {num3}')
        self.data[num3] = str(num1 * num2)

    def opcode3(self, params, position):
        if params[1] == 0:

            if self.count == 0:
                self.data[int(self.data[position + 1])] = str(self.phase)
                self.count += 1
            elif self.count == 1:
                self.data[int(self.data[position + 1])] = str(self.inputPower)
                self.count += 1
            else:
                self.data[int(self.data[position + 1])] = str(self.input)
        else:

            if self.count == 0:
                self.data[position + 1] = str(self.phase)
                self.count += 1
            elif self.count == 1:
                self.data[position + 1] = str(self.inputPower)
                self.count += 1
            else:
                self.data[position + 1] = str(self.input)

    def opcode4(self, params, position):
        if params[1] == 0:
            print(self.data[int(self.data[position + 1])])
            self.output = int(self.data[int(self.data[position + 1])])
        else:
            print(self.data[position + 1])
            self.output = int(self.data[position + 1])

    def opcode5(self, params, position):
        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])
        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])
        if num1 != 0:
            return num2
        else:
            return 'A'

    def opcode6(self, params, position):

        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])

        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])

        if num1 == 0:
            return num2
        else:
            return 'A'

    def opcode7(self, params, position):

        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])

        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])

        num3 = int(self.data[position + 3])

        if num1 < num2:
            self.data[num3] = '1'
        else:
            self.data[num3] = '0'

    def opcode8(self, params, position):
        if params[1] == 0:
            num1 = int(self.data[int(self.data[position + 1])])
        else:
            num1 = int(self.data[position + 1])

        if params[2] == 0:
            num2 = int(self.data[int(self.data[position + 2])])
        else:
            num2 = int(self.data[position + 2])

        num3 = int(self.data[position + 3])

        if num1 == num2:
            self.data[num3] = '1'
        else:
            self.data[num3] = '0'

    def opcode99(self):
        pass
        # print(f'The value at position 0 is {self.data[0]}')

    def ampPower(self,):
        nextPower = self.call()
        return nextPower

    def call(self):
        position = self.pos
        while True:
            code = self.padder(self.data[position])
            params = self.parameters(code)
            if params[0] == 1:
                self.opcode1(params, position)
                position += 4
            elif params[0] == 2:
                self.opcode2(params, position)
                position += 4
            elif params[0] == 3:
                self.opcode3(params, position)
                position += 2
            elif params[0] == 4:
                self.opcode4(params, position)
                position += 2
            elif params[0] == 5:
                check = self.opcode5(params, position)
                if check != 'A':
                    position = check
                else:
                    position += 3
            elif params[0] == 6:
                check = self.opcode6(params, position)
                if check != 'A':
                    position = check
                else:
                    position += 3
            elif params[0] == 7:
                self.opcode7(params, position)
                position += 4
            elif params[0] == 8:
                self.opcode8(params, position)
                position += 4
            elif params[0] == 99:
                self.opcode99()
                position += 1
                break

        self.pos = position
        self.count = 0
        return self.output


def getInput():
    data = open('AoC_Data/day7.txt').read().split(',')
    return data

def partA():
    print('Starting part A')
    perm = permutations([0, 1, 2, 3, 4])
    ampList = ['A', 'B', 'C', 'D', 'E']
    amps = dict()
    for amp in ampList:
        amps[amp] = IntcodeMachine(getInput(), 1, 0, 0)
    # power = 0
    maxPower = 0
    for i in perm:
        power = 0
        pos = 0

        for j in amps:
            amps[j].updatePowerPhase(power, i[pos])
            power = amps[j].ampPower()
            amps[j].resetPos()
            pos += 1
        if power > maxPower:
            maxPower = power
    print(maxPower)

partA()
