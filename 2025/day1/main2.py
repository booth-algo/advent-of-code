def part2(rotations):
    position = 50
    count = 0
    for rot in rotations:
        direction = 1 if rot[0] == 'R' else -1
        distance = int(rot[1:])
        for _ in range(distance):
            position = (position + direction) % 100
            if position == 0:
                count += 1
    return count

rotations = [line.strip() for line in open('data.txt')]
print(part2(rotations))
