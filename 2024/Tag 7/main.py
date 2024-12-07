from readFile import readFile

#Part 1
# Berechnet die Summe aller Zielwerte, die durch Addition oder Multiplikation erreicht werden können.
def part1(puzzle_input):
    def is_valid(target, nums):
        n = len(nums)
        queue = [(1, nums[0])]
        while queue:
            i, val = queue.pop()
            if i == n:
                if val == target:
                    return True
                continue
            
            possibilities = [
                val + nums[i],
                val * nums[i],
            ]
            for p in possibilities:
                if p <= target:
                    queue.append((i+1, p))

        return False

    total = 0
    for line in puzzle_input.split('\n'):
        left, right = line.split(': ')
        target = int(left)
        nums = [int(num) for num in right.split()]
        if is_valid(target, nums):
            total += target

    return total

#Part 2
# Berechnet die Summe aller Zielwerte, die durch Addition, Multiplikation oder Verkettung erreicht werden können.
def part2(puzzle_input):
    def is_valid(target, nums):
        n = len(nums)
        queue = [(1, nums[0])]
        while queue:
            i, val = queue.pop()
            if i == n:
                if val == target:
                    return True
                continue
            
            possibilities = [
                val + nums[i],
                val * nums[i],
                int(f'{val}{nums[i]}'),
            ]
            for p in possibilities:
                if p <= target:
                    queue.append((i+1, p))

        return False

    total = 0
    for line in puzzle_input.split('\n'):
        left, right = line.split(': ')
        target = int(left)
        nums = [int(num) for num in right.split()]
        if is_valid(target, nums):
            total += target

    return total

if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))

    # Part 2
    print(part2(puzzle_input))