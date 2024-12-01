lists = open('../old_input/input_day1.txt', 'r').read().split('\n')

left_list = sorted([int(x.split('   ')[0]) for x in lists])
right_list = sorted([int(x.split('   ')[1]) for x in lists])

score = 0

for index, item in enumerate(left_list):
    occurrences = right_list.count(item)
    score += item * occurrences


print(score)
