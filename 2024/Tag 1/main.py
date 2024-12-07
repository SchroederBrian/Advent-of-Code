import os
from collections import Counter

# Lädt die Datei 'input.txt', wenn vorhanden, und gibt den Inhalt zurück.
def read_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'input.txt')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as input_file:
            content = input_file.read()
            return content
    else:
        print(f"Datei {file_path} nicht gefunden.")
        return None

# Teilt jede Zeile der Datei in zwei Zahlen auf und gibt sie als zwei separate Listen zurück.
def splitFile(file):
    left_side = []
    right_side = []
    for line in file.strip().splitlines():
        if line.strip():
            left, right = line.split(maxsplit=1)
            left_side.append(int(left.strip()))
            right_side.append(int(right.strip()))
    return left_side, right_side


# Berechnet die Summe der absoluten Differenzen zwischen den entsprechenden Elementen zweier Listen.
def calculate_difference(sortedLeft, sortedRight):
    result = 0
    for i in range(len(sortedLeft)):
        result += abs(sortedLeft[i] - sortedRight[i])
    return result


# Berechnet einen Ähnlichkeitsscore basierend auf den Häufigkeiten von Elementen in der zweiten Liste.
def calculate_similarity_score(left_side, right_side):
    right_counts = Counter(right_side)
    
    similarity_score = 0
    for num in left_side:
        similarity_score += num * right_counts.get(num, 0)
    
    return similarity_score


if __name__ == "__main__":
    file = read_file()
    if file:
        left_side, right_side = splitFile(file)

        sorted_left = sorted(left_side)
        sorted_right = sorted(right_side)

        print(f"Part 1: {calculate_difference(sortedLeft, sortedRight)}")
        print(f"Part 2: {calculate_similarity_score(left_side, right_side)}")
