from itertools import pairwise

reports = open('../old_input/input_day2.txt', 'r').read().split('\n')

safe_reports = 0

def valid(items):
    inc = True
    dec = True
    for index, pair in enumerate(items):
        if not abs(pair[0] - pair[1]) <= 3:
            return pair
        if pair[0] > pair[1] and dec:
            inc = False
        elif pair[0] < pair[1] and inc:
            dec = False
        else:
            return pair

    return []

for report in reports:
    rep = [int(x) for x in report.split()]
    dangerous_items = valid(pairwise(rep))
    if len(dangerous_items) == 0:
        safe_reports += 1
    else:
        valid_list = []
        for ind in range(len(rep)):
            # remove a single value in each position of the list
            popped = [value for inde, value in enumerate(rep) if inde != ind]
            if len(valid(pairwise(popped))) == 0:
                valid_list.append(True)
            else:
                valid_list.append(False)

        # if any of those lists with a removed item give a valid combination it is fine
        if any(valid_list):
            safe_reports += 1

print(safe_reports)
