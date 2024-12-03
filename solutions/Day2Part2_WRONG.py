# This does not work, I have included this into the github to hopefully help somebody out.
# did not have to cheat to find a new way tho

# so what it does here is that it finds the "incorrect" numbers which do not match the criteria
# once it has found this pair it will remove each of them from the list and see if this provides a valid new list
# I have not found the 2 edge cases which this does not work and I will not take the time to find them

# in the end I just brute forced all possible deletion lists instead of only checking the ones which do not match
# the criteria. For some reason this found the 2 hits I was missing

# Note I have found the edge cases thx to reddit, I have included them in the repo. it detects a inc/dec direction
# change 1 item too late

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

def find_sub_list(sl,l):
    sll=len(sl)
    for ind in (i for i,e in enumerate(l) if e==sl[0]):
        if l[ind:ind+sll]==sl:
            return ind,ind+sll-1

for report in reports:
    pairs = pairwise([int(x) for x in report.split()])
    # For some reason the pairwise would only let me iterate over it once
    list_pairs = [[x, y] for x, y in pairs]

    dangerous_items = valid(list_pairs)
    if len(dangerous_items) == 0:
        safe_reports += 1
    else:
        remove_first = [int(x) for x in report.split()]
        # The location of the wrong items
        location = find_sub_list(dangerous_items, remove_first)
        del remove_first[location[0]]
        remove_last = [int(x) for x in report.split()]
        del remove_last[location[1]]

        list_pairs_first = [[x, y] for x, y in pairwise(remove_first)]
        list_pairs_last = [[x, y] for x, y in pairwise(remove_last)]

        first_valid = valid(list_pairs_first)
        second_valid = valid(list_pairs_last)
        if len(first_valid) == 0 or len(second_valid) == 0:
            safe_reports += 1



print(safe_reports)
# 624 too low