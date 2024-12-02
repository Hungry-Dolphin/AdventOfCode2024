from itertools import pairwise

reports = open('../old_input/input_day2.txt', 'r').read().split('\n')

safe_reports = 0

for report in reports:
    pairs = pairwise([int(x) for x in report.split()])
    # For some reason the pairwise would only let me iterate over it once
    list_pairs = [[x, y] for x, y in pairs]

    # max step of 3
    steps = all([abs(x-y) <= 3 for x, y in list_pairs])

    # increasing or decreasing
    if all(x > y for x, y in list_pairs) or all(x < y for x, y in list_pairs):
        safe_reports += 1 if steps else 0


print(safe_reports)