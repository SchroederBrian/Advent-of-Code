from readFile import readFile
import re
from itertools import count
import math

#Part 1
def part1(puzzle_input, is_example_input=False):
    m = 7 if is_example_input else 103
    n = 11 if is_example_input else 101

    m_half, n_half = m//2, n//2
    quadrants = [0] * 4
    for line in puzzle_input.split('\n'):
        x, y, i, j = map(int, re.findall(r'(-?\d+)', line))
        x = (x + 100*i) % n
        y = (y + 100*j) % m
        if x == n_half or y == m_half:
            continue
        
        idx = (x < n_half) * 2  + (y < m_half)
        quadrants[idx] += 1

    return math.prod(quadrants)

#Part 2
def part2(puzzle_input):
    m = 103
    n = 101
    robots = [
        [int(x) for x in re.findall(r'(-?\d+)', line)]
        for line in puzzle_input.split('\n')
    ]
    N = len(robots)
    for second in count(1):
        coordinates = set()
        overlap = False
        for r in range(N):
            x, y, i, j = robots[r]
            x = (x + i) % n
            y = (y + j) % m
            robots[r][:2] = [x, y]
            if (x, y) in coordinates:
                overlap = True
            coordinates.add((x, y))

        if not overlap:
            return second
        

if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))

    # Part 2
    print(part2(puzzle_input))