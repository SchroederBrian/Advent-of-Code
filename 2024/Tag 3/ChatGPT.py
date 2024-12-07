import re
from readFile import readFile

#Part 1
data = readFile()
if data:
    print(sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", data)))