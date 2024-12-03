import re

memory = open('../input_day3.txt', 'r').read()

mul_instructions = re.findall(r'mul\((?:\d){1,3},(?:\d){1,3}\)', memory)

answer = 0

for instruction in mul_instructions:
    x, y = instruction[4:-1].split(',')
    answer += (int(x) * int(y))

print(answer)