import re

with open('input.txt') as f:
    text = f.read()

pattern = r'((?:do|don\'t)\(\))'
parts = re.split(pattern, text)

result = []
current_group = []

for part in parts:
    if part in ["do()", "don't()"]:
        if current_group: # if we have accumulated parts
            result.append(current_group)
        current_group = [part] # start new group with delimiter
    elif part: # if part is not empty
        current_group.append(part)

if current_group: # add last group if exists
    result.append(current_group)

total = 0

def product(entry):
    matches = re.findall(r"mul\((\d+),(\d+)\)", entry)
    products = 0
    for x,y in matches:
        products += int(x) * int(y)

    return products

# For first part
total += product(result[0][0])

# For remaining
for entry in result:
    if entry[0] == "do()":
        total += product(entry[1])

print(total)        

