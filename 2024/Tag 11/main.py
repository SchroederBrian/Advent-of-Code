from readFile import readFile
from collections import Counter, defaultdict

#Part 1
def part1(puzzle_input):
    stones = Counter(int(num) for num in puzzle_input.split())

    def mutate(stone):
        if stone == 0:
            return [1]
        digits = str(stone)
        half, remainder = divmod(len(digits), 2)
        if remainder == 0:
            return map(int, (digits[:half], digits[half:]))
        return [stone * 2024]

    for _ in range(25):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for child in mutate(stone):
                new_stones[child] += count
        stones = new_stones

    return sum(stones.values())

#Part 2
def part2(puzzle_input):
    stones = Counter(int(num) for num in puzzle_input.split())

    def mutate(stone):
        if stone == 0:
            return [1]
        digits = str(stone)
        half, remainder = divmod(len(digits), 2)
        if remainder == 0:
            return map(int, (digits[:half], digits[half:]))
        return [stone * 2024]

    for _ in range(75):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            for child in mutate(stone):
                new_stones[child] += count
        stones = new_stones

    return sum(stones.values())


if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))
    
    # Part 2
    print(part2(puzzle_input))