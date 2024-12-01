lists = open('../old_input/input_day1.txt', 'r').read().split('\n')

left_list = sorted([int(x.split('   ')[0]) for x in lists])
right_list = sorted([int(x.split('   ')[1]) for x in lists])

distance = 0

for index, item in enumerate(left_list):
    distance += abs(item-right_list[index])

print(distance)
