import os
from collections import Counter

# Lädt Eingabedatei und prüft, ob die Datei existiert. Liest den Inhalt bei Erfolg.
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

# Bob
# Überprüft die Sicherheit der Zeilen basierend auf aufeinanderfolgenden Differenzen.
def safeOrUnsafe(lines):
    result = 0
    for line in lines:
        check = 0
        if line[0] > line[1]:
            for i in range(0, len(line)-1):
                if line[i] - line[i+1] >= 1 and line[i] - line[i+1] <= 3:
                    check = True
                else:
                    check = False
                    break
        elif line[0] < line[1]:
            for i in range(0, len(line)-1):
                if line[i+1] - line[i] >= 1 and line[i+1] - line[i] <= 3:
                    check = True
                else:
                    check = False
                    break
        if check:
            result += 1
    return result

# Level 2 function with Problem Dampener
# Versucht, unsichere Zeilen durch Entfernen eines Elements sicher zu machen.
def safeOrUnsafeLvl2(lines):
    result = 0
    for line in lines:
        if isSafe(line):
            result += 1
        else:
            for i in range(len(line)):
                modified_line = line[:i] + line[i+1:]
                if isSafe(modified_line):
                    result += 1
                    break
    return result

# Prüft, ob eine Liste sicher ist, basierend auf Differenzen und steigendem oder fallendem Muster.
def isSafe(line):
    if len(line) < 2:
        return False
    diffs = [line[i+1] - line[i] for i in range(len(line) - 1)]
    all_increasing = all(1 <= diff <= 3 for diff in diffs)
    all_decreasing = all(-3 <= diff <= -1 for diff in diffs)
    return all_increasing or all_decreasing

# Torf
# Bewertet Zeilen auf Sicherheit mithilfe eines Vergleichsoperators.
def safeOrUnsafe2(lines):
    result = 0
    for line in lines:
        if line[0] > line[1]:
            result += 1 if checkSafe(line, lambda x, y: x > y) else 0
        elif line[0] < line[1]:
            result += 1 if checkSafe(line, lambda x, y: x < y) else 0
    return result

# Überprüft Sicherheit basierend auf einem benutzerdefinierten Vergleich zwischen Elementen.
def checkSafe(line, compare):
    check = False
    for i in range(0, len(line)-1):
        if abs(line[i] - line[i+1]) >= 1 and abs(line[i] - line[i+1]) <= 3 and compare(line[i], line[i+1]):
            check = True
        else:
            check = False
            break
    return check


if __name__ == "__main__":
    file = readFile()
    if file:
        linesString = file.strip().splitlines()
        lines = [[int(i) for i in inner] for inner in [line.split() for line in linesString]]

        print(f"Result Bob: {safeOrUnsafe(lines)}")
        print(f"Result Torf: {safeOrUnsafe2(lines)}")
        print(f"Result Bob Lvl2: {safeOrUnsafeLvl2(lines)}")
