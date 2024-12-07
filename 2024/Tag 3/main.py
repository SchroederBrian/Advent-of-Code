import re
from readFile import readFile

# Lädt Eingaben, sucht nach Mustern mit regulären Ausdrücken, und analysiert die Daten.
s = readFile()
print(f"Loaded input: {s[:500]}")

pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
data = [([int(x) for x in m.groups()], m.span(0)) for m in re.finditer(pattern, s)]
print(f"Matched data: {data[:5]}")


def get_state(p):
    # Prüft, ob der letzte Aufruf von "do()" vor Position p später als der letzte Aufruf von "don't()" ist.
    return s.rfind('do()', 0, p) >= s.rfind("don't()", 0, p)


print(f"Sum without state check: {sum(a * b for (a, b), _ in data)}")
print(f"Sum with state check: {sum(a * b for (a, b), (p, _) in data if get_state(p))}")
