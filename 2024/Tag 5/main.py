from readFile import readFile

from collections import defaultdict
import re

# Part 1
# Berechnet die Gesamtpunktzahl basierend auf Regeln und Seitenaktualisierungen.
def part1(puzzle_input):
    rules, updates = puzzle_input.split('\n\n')
    preceding = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        preceding[int(p2)].add(int(p1))

    def get_score(pages):
        disallowed = set()
        for page in pages:
            if page in disallowed:
                return 0
            
            disallowed |= preceding[page]

        return pages[len(pages)//2]

    total = 0
    for line in updates.split('\n'):
        pages = list(map(int, line.split(',')))
        total += get_score(pages)

    return total

# Part 2
# Bewertet Seiten mit einer Neuordnung, falls erforderlich, und berechnet die Gesamtpunktzahl.
def part2(puzzle_input):
    rules, updates = puzzle_input.split('\n\n')
    preceding = defaultdict(set)
    for p1, p2 in re.findall(r'(\d+)\|(\d+)', rules):
        preceding[int(p2)].add(int(p1))

    def get_score(pages, is_reordered=False):
        disallowed_after = dict()
        for i, page in enumerate(pages):
            if page in disallowed_after:
                j = disallowed_after[page]
                reordered = pages[:j] + [page] + pages[j:i] + pages[i+1:]
                return get_score(reordered, True)
            
            for p in preceding[page]:
                if p not in disallowed_after:
                    disallowed_after[p] = i
            
        return pages[len(pages)//2] if is_reordered else 0

    total = 0
    for line in updates.split('\n'):
        pages = list(map(int, line.split(',')))
        total += get_score(pages)

    return total

if __name__ == "__main__":
    puzzle_input = readFile()

    # Part 1
    print(part1(puzzle_input))

    # Part 2
    print(part2(puzzle_input))