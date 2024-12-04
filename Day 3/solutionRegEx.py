import re

def read(filename):
    with open(filename, 'r') as f:
        text = f.read()
    
    # Match `mul(x, y)` and capture x and y; also match `do()` and `don't()` without any capturing groups
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    matches = re.finditer(pattern, text)
    
    instructions = []
    for match in matches:
        # group(0) is the whole match, group(1) is first capture, group(2) is second capture
        if match.group(1) and match.group(2):
            x, y = int(match.group(1)), int(match.group(2))
            instructions.append(('mul', x, y))
        elif match.group(0) == 'do()':
            instructions.append(('do',))
        elif match.group(0) == "don't()":
            instructions.append(("don't",))
    return instructions

def part1Solution(instructions):
    result = 0

    for instruction in instructions:
        if instruction[0] == 'mul':
            result += instruction[1] * instruction[2]
    
    return result

def part2Solution(instructions):
    result = 0
    enabled = True

    for instruction in instructions:
        if instruction[0] == 'do':
            enabled = True
        elif instruction[0] == "don't":
            enabled = False
        elif instruction[0] == 'mul' and enabled:
            result += instruction[1] * instruction[2]

    return result

instructions = read('input.txt')
print(part1Solution(instructions))
print(part2Solution(instructions))
