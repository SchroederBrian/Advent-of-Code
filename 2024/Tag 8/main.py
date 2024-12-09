from collections import defaultdict
from itertools import combinations 
from readFile import readFile

#Part 1
# Zählt Antinodes, die durch Paare von Punkten in einer Gitterstruktur erzeugt werden.
def part1(puzzle_input):
    grid = puzzle_input.split()
    locations = defaultdict(set)
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if grid[r][c] != '.':
                locations[grid[r][c]].add((r, c))

    antinodes = set()
    for loc in locations.values():
        for (a, b), (c, d) in combinations(loc, 2):
            dr = a - c
            dc = b - d
            for r, c in [(a+dr, b+dc), (c-dr, d-dc)]:
                if r in range(m) and c in range(n):
                    antinodes.add((r, c))
         
    return len(antinodes)

#Part 2
# Erweitert Antinodes entlang der Linien zwischen Paaren von Punkten in der Gitterstruktur und zählt sie.
def part2(puzzle_input):
    grid = puzzle_input.split()
    locations = defaultdict(set)
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if grid[r][c] != '.':
                locations[grid[r][c]].add((r, c))

    antinodes = set()
    for loc in locations.values():
        for (a, b), (c, d) in combinations(loc, 2):
            dr = a - c
            dc = b - d

            row, col = a, b
            while row in range(m) and col in range(n):
                antinodes.add((row, col))
                row += dr
                col += dc
                
            row, col = c, d
            while row in range(m) and col in range(n):
                antinodes.add((row, col))
                row -= dr
                col -= dc

    return len(antinodes)

if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))
    
    # Part 2
    print(part2(puzzle_input))