def read(filename):
    l1 = []
    l2 = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        l1.append(line.split()[0])
        l2.append(line.split()[1])
    return l1, l2

def part1Solution(L1, L2):
    L1.sort()
    L2.sort()
    distance = 0
    for i in range(len(L1)):
        distance += abs(int(L1[i]) - int(L2[i]))
    return distance

def part2Solution(L1, L2):
    similarity = 0
    for id in L1:
        similarity += int(id) * L2.count(id)
    return similarity

L1, L2 = read('input.txt')
print("Part 1 Answer:", part1Solution(L1, L2))
print("Part 2 Answer:", part2Solution(L1, L2))