import time

class IntcodeMachine:

    def __init__(self, data_string, input_code):
        self.data = data_string[0].split(',')
        self.input = input_code

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
            self.data[int(self.data[position + 1])] = str(self.input)
        else:
            self.data[position + 1] = str(self.input)

    def opcode4(self, params, position):
        if params[1] == 0:
            print(self.data[int(self.data[position + 1])])
        else:
            print(self.data[position + 1])

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
        print(f'The value at position 0 is {self.data[0]}')

    def call(self):

        position = 0

        # print(params)
        while True:
            code = self.padder(self.data[position])
            params = self.parameters(code)
            if params[0] == 1:
                self.opcode1(params, position)
                position += 4
            if params[0] == 2:
                self.opcode2(params, position)
                position += 4
            if params[0] == 3:
                self.opcode3(params, position)
                position += 2
            if params[0] == 4:
                self.opcode4(params, position)
                position += 2
            if params[0] == 5:
                check = self.opcode5(params, position)
                if check != 'A':
                    position = check
                else:
                    position += 3
            if params[0] == 6:
                check = self.opcode6(params, position)
                if check != 'A':
                    position = check
                else:
                    position += 3
            if params[0] == 7:
                self.opcode7(params, position)
                position += 4
            if params[0] == 8:
                self.opcode8(params, position)
                position += 4
            if params[0] == 99:
                self.opcode99()
                break

        # print(self.data)


data = open('AoC_Data/day5.txt').read().splitlines()
# Part 1
start1 = time.perf_counter()
test = IntcodeMachine(data, '1')
test.call()
print(time.perf_counter() - start1)

# Part 2
start2 = time.perf_counter()
test = IntcodeMachine(data, '5')
test.call()
end = time.perf_counter()
print(f'Time for part 2 is {end - start2} and a total of {end - start1} for both parts')