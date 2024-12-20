import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


results = {}
count = 0

for line in lines:
    count += 1
    _, numbers = line.split(':')
    set_before, set_after = numbers.split('|')

    front_set = set(set_before.split())
    back_set = set(set_after.split())

    matches = front_set & back_set

    results[count] = len(matches)

# print(results)

copies = {}

for entry in results:
    copies[entry] = 1

for key, val in results.items():
    for i in range(1,val+1):
        copies[key+i] += copies[key]

print(sum(copies.values()))
