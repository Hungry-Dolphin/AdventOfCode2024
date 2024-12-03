import re

memory = open('../input_day3.txt', 'r').read()

mul_instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', memory)

answer = 0
enabled = True

for instruction in mul_instructions:
    if instruction.startswith('do()'):
        enabled = True
    elif instruction.startswith("don't()"):
        enabled = False
    elif enabled:
        x, y = instruction[4:-1].split(',')
        answer += (int(x) * int(y))

print(answer)