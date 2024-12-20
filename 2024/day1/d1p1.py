import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

pattern = re.compile(r"(\d+)\s*(\d+)")

list1 = []
list2 = []

for line in lines:
    match = pattern.match(line)
    if match:
        first = int(match.group(1))
        second = int(match.group(2))
        list1.append(first)
        list2.append(second)

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += abs(list2[i]-list1[i])

print(total)