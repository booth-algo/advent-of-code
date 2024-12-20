import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

reports = [line.split() for line in lines]

def check_report(diff):
    same_sign = all(level >= 0 for level in diff) or all(level < 0 for level in diff)
    within_limit = all(abs(level) <= 3 for level in diff)
    # levels_differ = all(level != 0 for level in diff)
    levels_differ = diff.count(0) == 0

    return same_sign and within_limit and levels_differ

num = 0

for report in reports:
    diff = []
    diff = [int(report[i]) - int(report[i + 1]) for i in range(len(report) - 1)]
    if check_report(diff):
        num += 1
    else:
        for i in range(len(report)):
            clone = list(report)
            clone.pop(i)
            diff = [int(clone[i]) - int(clone[i + 1]) for i in range(len(clone) - 1)]
            if check_report(diff):
                num += 1
                break

print(num)
