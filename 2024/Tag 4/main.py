from readFile import readFile

# Part 1
# Zählt Vorkommen des Wortes 'XMAS' in verschiedenen Richtungen innerhalb eines Gitters.
def part1(puzzle_input):
    rows = puzzle_input.split('\n')
    m = len(rows)
    n = len(rows[0])

    def count(r, c):
        if rows[r][c] != 'X':
            return 0
        return sum([
            c > 2 and rows[r][c:c-4:-1] == 'XMAS',                                              # left
            c < n - 3 and rows[r][c:c+4] == 'XMAS',                                             # right
            r > 2 and ''.join(rows[r-i][c] for i in range(4)) == 'XMAS',                        # up
            r < m - 3 and ''.join(rows[r+i][c] for i in range(4)) == 'XMAS',                    # down
            r > 2 and c > 2 and ''.join(rows[r-i][c-i] for i in range(4)) == 'XMAS',            # left-up
            r > 2 and c < n - 3 and ''.join(rows[r-i][c+i] for i in range(4)) == 'XMAS',        # right-up
            r < m - 3 and c > 2 and ''.join(rows[r+i][c-i] for i in range(4)) == 'XMAS',        # left-down
            r < m - 3 and c < n - 3 and ''.join(rows[r+i][c+i] for i in range(4)) == 'XMAS',    # right-down
        ])

    return sum(count(r, c) for r in range(m) for c in range(n))

# Part 2
# Prüft auf ein spezifisches Muster um das Zeichen 'A' und zählt passende Vorkommen.
def part2(puzzle_input):
    rows = puzzle_input.split('\n')
    m = len(rows)
    n = len(rows[0])

    def check(r, c):
        if rows[r][c] != 'A':
            return False
        ul = rows[r-1][c-1]
        ur = rows[r-1][c+1]
        dl = rows[r+1][c-1]
        dr = rows[r+1][c+1]
        return sorted([ul, ur, dl, dr]) == ['M', 'M', 'S', 'S'] and ul != dr

    return sum(check(r, c) for r in range(1, m-1) for c in range(1, n-1))

if __name__ == "__main__":
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))

    # Part 2
    print(part2(puzzle_input))