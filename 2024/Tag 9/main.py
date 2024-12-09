from readFile import readFile
from collections import deque

#Part 1
# Berechnet die Gesamtsumme basierend auf der Größenverteilung einer Disk, wobei Slots abwechselnd behandelt werden.
def part1(puzzle_input):
    disk = deque([int(size) for size in puzzle_input])
    left_id = 0
    right_id = len(puzzle_input) // 2
    idx = 0
    total = 0
    is_empty_slot = False
    while disk:
        size = disk.popleft()
        if is_empty_slot:
            for _ in range(size):
                total += idx * right_id
                idx += 1
                disk[-1] -= 1
                if disk[-1] == 0:
                    for _ in range(2):
                        disk.pop()
                    right_id -= 1
        else:
            for _ in range(size):
                total += idx * left_id
                idx += 1
            left_id += 1
        is_empty_slot = not is_empty_slot

    return total

#Part 2
# Ordnet Diskgrößen um, basierend auf spezifischen Regeln, und berechnet die Gesamtsumme.
def part2(puzzle_input):
    disk = []
    for i, num in enumerate(puzzle_input):
        idx = None if i % 2 else i // 2
        size = int(num)
        if size > 0:
            disk.append([idx, size])

    i = 0
    while i < len(disk):
        i += 1
        idx, size = disk[-i]
        if idx is None:
            continue
        
        for j in range(len(disk) - i):
            if disk[j][0] is None and disk[j][1] >= size:
                if disk[j][1] == size:
                    disk[j][0] = idx
                else:
                    disk[j][1] -= size
                    disk.insert(j, disk[-i].copy())
                disk[-i][0] = None
                break

    total = idx = 0
    for id, size in disk:
        if id is not None:
            total += id * size * (idx + ((size - 1) / 2))
        idx += size

    return int(total)

if __name__ == '__main__':
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))
    
    # Part 2
    print(part2(puzzle_input))