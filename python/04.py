#!/usr/bin/python3
import utilities

def meets_criteria(n):
    digit = 10
    found_pair = False

    while n > 0:
        new_digit = n % 10

        if new_digit > digit:
            return False
        elif new_digit == digit:
            found_pair = True

        digit = new_digit
        n = n // 10

    return found_pair

def has_exactly_pair(n):
    digit = 10

    current_digit = 10
    current_count = 1

    while n > 0:
        new_digit = n % 10

        if new_digit == digit:
            current_count += 1
        elif current_count == 2:
            return True
        else:
            current_count = 1

        digit = new_digit
        n = n // 10

    return current_count == 2

def main():
    (min, max) = [int(x) for x in utilities.data(4).strip().split('-')]

    print("Part 1:")
    solutions = [n for n in range(min, max+1) if meets_criteria(n)]
    print(len(solutions))

    print("\nPart 2:")
    solutions = [n for n in solutions if has_exactly_pair(n)]
    print(len(solutions))



if __name__ == '__main__':
    main()

