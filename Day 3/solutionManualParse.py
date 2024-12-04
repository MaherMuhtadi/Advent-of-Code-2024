def read(filename):
    with open(filename, 'r') as f:
        text = f.read()
    
    instructions = []
    for i in range(len(text)):
        if text[i:i+4] == 'do()':
            i += 4
            instructions.append(('do',))
        elif text[i:i+7] == "don't()":
            i += 7
            instructions.append(("don't",))
        elif text[i:i+4] == 'mul(':
            i += 4
            x = '' # First number
            y = '' # Second number
            j = i
            while text[j] != ',':
                x += text[j]
                j += 1
            j += 1 # Skip the comma
            while text[j] != ')':
                y += text[j]
                j += 1
            if x.isdigit() and y.isdigit():
                instructions.append(('mul', int(x), int(y)))
                i = j + 1 # Skip the closing parenthesis

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
