#!/usr/bin/python3

import intcode

def run_with_noun_verb(noun, verb):
    with open('../input/02.txt', 'r') as f:
        data = f.read()

    program = list(map(lambda x: int(x), data.split(',')))
    program[1] = noun
    program[2] = verb


    computer = intcode.computer(program)
    computer.run()

    return computer.memory[0]


def main():
    print("Part 1:")
    print(run_with_noun_verb(12, 2))

    print("\nPart 2:")
    for noun in range(99):
        for verb in range(99):
            if run_with_noun_verb(noun, verb) == 19690720:
                print(100 * noun + verb)
                return

if __name__ == '__main__':
    main()
