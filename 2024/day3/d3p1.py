import re

with open('input.txt') as f:
    text = f.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", text)

total = 0

for x,y in matches:
    total += int(x) * int(y)

print(total)

