input = open("input.txt", 'r').read().split("\n")[:-1]

total = 0

for line in input:
    line = list(map(int, [c for c in line]))
    
    d1 = max(line[:-1])
    remaining = line[line.index(d1) + 1 :]
    d2 = max(remaining)

    jolts = d1 * 10 + d2
    total += jolts

print(total)