#!/usr/bin/python3

import operator

with open('../input/02.txt', 'r') as f:
    data = f.read()

program = list(map(lambda x: int(x), data.split(',')))

def process_opcode(program, index):

    result = program.copy()
    opcode = program[index]
    input1 = program[index + 1]
    input2 = program[index + 2]
    output = program[index + 3]

    if opcode == 1:
        result[output] = program[input1] + program[input2]
    elif opcode == 2:
        result[output] = program[input1] * program[input2]

    return result

program[1] = 12
program[2] = 2

index = 0

while program[index] != 99:
    program = process_opcode(program, index)
    index += 4


print(program)
