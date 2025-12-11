from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]


def opToBin(op):
    op = op.split(",")
    op = [int(e) for e in op]
    b = 0
    for n in op:
        b += 1 << n
    return b


def solve(line):
    lights = []
    i = 1
    while line[i] != "]":
        if line[i] == ".":
            lights.append("0")
        else:
            lights.append("1")
        i += 1

    ops = line[i + 3 : line.index("{") - 2].split(") (")
    ops = [opToBin(o) for o in ops]
    mask = 0
    target = int("".join(reversed(lights)), 2)
    num_pushes = 0
    queue = deque()
    queue.append(mask)

    while queue:
        l = len(queue)
        for i in range(l):
            m = queue.popleft()
            if m == target:
                return num_pushes
            for op in ops:
                queue.append(m ^ op)

        num_pushes += 1


total = 0
for line in data:
    count = solve(line)
    total += count

print(total)
