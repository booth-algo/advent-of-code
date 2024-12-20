import re
from collections import defaultdict

loaded = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as f:
    lines = f.readlines()

# lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]

data = defaultdict(list)

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
        # print(game_num)
        # print(color_data)

        for color_match in color_pattern.finditer(color_data):
            count = int(color_match.group(1))
            color = color_match.group(2)

            if color in loaded:
                data[game_num].append((count, color, loaded[color]))
                if count > loaded[color]:
                    impossible = True
    if not impossible:
        sum += game_num
    
print(sum)