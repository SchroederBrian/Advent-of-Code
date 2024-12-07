import os
from collections import Counter

def readFile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'input.txt')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as input_file:
            content = input_file.read()
            return content
    else:
        print(f"Datei {file_path} nicht gefunden.")
        return None


def splitFile(file):
    leftSide = []
    rightSide = []
    for line in file.strip().splitlines():
        if line.strip():
            left, right = line.split()
            leftSide.append(int(left.strip()))
            rightSide.append(int(right.strip()))
    return leftSide, rightSide


def solve(sortedLeft, sortedRight):
    result = 0
    for i in range(len(sortedLeft)):
        result += abs(int(sortedLeft[i]) - int(sortedRight[i]))
    return result


def solve_part2(leftSide, rightSide):
    right_counts = Counter(rightSide)
    
    similarity_score = 0
    for num in leftSide:
        similarity_score += num * right_counts[num]
    
    return similarity_score


if __name__ == "__main__":
    file = readFile()
    if file:
        leftSide, rightSide = splitFile(file)

        sortedLeft = sorted(leftSide)
        sortedRight = sorted(rightSide)

        print(f"Part 1: {solve(sortedLeft, sortedRight)}")
        print(f"Part 2: {solve_part2(leftSide, rightSide)}")
