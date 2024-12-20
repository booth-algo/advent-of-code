import re
from collections import defaultdict

loaded = {
    'red': 0,
    'green': 0,
    'blue': 0
}

with open('input.txt') as f:
    lines = f.readlines()

# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]

impossible = False
sum = 0

game_pattern = re.compile(r"Game (\d+):\s*(.*)")
color_pattern = re.compile(r"(\d+)\s*(\w+)")

for line in lines:
    impossible = False
    match = game_pattern.match(line)
    if match:
        game_num = int(match.group(1))
        color_data = match.group(2)

        for color_match in color_pattern.finditer(color_data):
            count = int(color_match.group(1))
            color = color_match.group(2)

            if color in loaded and count > loaded[color]:
                loaded[color] = count

    print(loaded)

    temp = 1

    for val in loaded.values():
        temp *= val

    sum += temp
    loaded = dict.fromkeys(loaded, 0) # Sets all values in dict to 0

    
print(sum)