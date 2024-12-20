import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

reports = [line.split() for line in lines]

# hit a bad level --> check remaining with i or i-1 removed --> if not solved then return False

def check_report(diff):
    same_sign = all(level >= 0 for level in diff) or all(level < 0 for level in diff)
    within_limit = all(abs(level) <= 3 for level in diff)
    levels_differ = all(level != 0 for level in diff)

    if not same_sign or not within_limit or not levels_differ:
        # absolute value > 3 (within_limit) error: still unsafe

        #! program following cases:
        # if exactly one zero difference error and no other errors: unsafe --> safe
        # if only one not same sign error and no other errors: unsafe --> safe 

        if diff.count(0) == 1 and within_limit and same_sign:
            return True
        
        elif not same_sign and within_limit and levels_differ:
            positive_count = sum(1 for level in diff if level > 0)
            negative_count = sum(1 for level in diff if level < 0)
            if positive_count == 1 or negative_count == 1:
                return True

    else:
        return True
 

num = 0

for report in reports:
    diff = []
    diff = [int(report[i]) - int(report[i + 1]) for i in range(len(report) - 1)]
    if check_report(diff):
        num += 1

print(num)
