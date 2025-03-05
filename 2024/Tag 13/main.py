from readFile import readFile
import re

#Part 1
def part1(puzzle_input):
    total = 0
    tolerance = 0.0001
    for machine in puzzle_input.split('\n\n'):
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        A = (bx*y - by*x) / (bx*ay - by*ax)
        B = (x-ax*A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B

    return int(total)

#Part 2
def part2(puzzle_input):
    total = 0
    tolerance = 0.0001
    offset = 10_000_000_000_000
    for machine in puzzle_input.split('\n\n'):
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        x += offset
        y += offset
        A = (bx*y - by*x) / (bx*ay - by*ax)
        B = (x-ax*A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total += 3*A + B

    return int(total)


if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))

    # Part 2
    print(part2(puzzle_input))