#!/usr/bin/python3

import math
import utilities

def fuel_function(x):
    return max(math.floor(x / 3.0) - 2, 0)

def fuel_requirements(x):
    fuel_req = fuel_function(x)
    if fuel_req == 0:
        return 0
    else:
        return fuel_req + fuel_requirements(fuel_req)

def main():
    input_data = utilities.data(1)

    modules = [int(x) for x in input_data.splitlines()]

    print('Part 1:')
    fuels = [fuel_function(x) for x in modules]
    print(sum(fuels))

    print('\nPart 2:')
    fuels = [fuel_requirements(x) for x in modules]
    print(sum(fuels))


if __name__ == '__main__':
    main()

