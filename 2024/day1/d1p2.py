import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

pattern = re.compile(r"(\d+)\s*(\d+)")

list1 = []
list2 = []

# {num: [times on left (list1), times on right (list2)]}
mappy = {}

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

for item in list1:
    if item not in mappy:
        mappy[item] = [1, 0]
    else:
        mappy[item][0] += 1

for item in list2:
    if item in mappy:
        mappy[item][1] += 1

# print(mappy)

for key, value in mappy.items():
    temp = key*value[0]*value[1]
    total += temp

print(total)
