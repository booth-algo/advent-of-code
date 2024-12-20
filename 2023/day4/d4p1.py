import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


results = 0

for line in lines:
    _, numbers = line.split(':')
    set_before, set_after = numbers.split('|')

    front_set = set(set_before.split())
    back_set = set(set_after.split())

    matches = front_set & back_set

    if matches:
        results += 2**(len(matches)-1)

print(results)    
