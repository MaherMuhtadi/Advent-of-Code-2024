def read(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def trends(report):
    validChange = []
    increasing = []
    decreasing = []

    for i in range(len(report)-1):
        diff = abs(int(report[i]) - int(report[i+1]))
        validChange.append(diff >= 1 and diff <= 3)
        increasing.append(report[i] >= report[i+1])
        decreasing.append(report[i] <= report[i+1])
    
    return validChange, increasing, decreasing

def part1Solution(reports):
    safeCount = 0

    for report in reports:
        levels = list(map(int, report.split()))
        validChange, increasing, decreasing = trends(levels)
        if all(validChange) and (all(increasing) or all(decreasing)):
            safeCount += 1
    
    return safeCount

def part2Solution(reports):
    safeCount = 0

    for report in reports:
        levels = list(map(int, report.split()))
        validChange, increasing, decreasing = trends(levels)
        
        if all(validChange) and (all(increasing) or all(decreasing)):
            safeCount += 1
            continue

        for i in range(len(levels)):
            modified_report = levels[:i] + levels[i+1:]  # Remove the i-th level
            validChange, increasing, decreasing = trends(modified_report)
            if all(validChange) and (all(increasing) or all(decreasing)):
                safeCount += 1
                break

    return safeCount

reports = read('input.txt')
print("Part 1 Answer:", part1Solution(reports))
print("Part 2 Answer:", part2Solution(reports))