from z3 import Int, Optimize, sat

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]


def solve(targets, buttons):
    opt = Optimize()
    presses = [Int(b) for b in range(len(buttons))]

    for b in presses:
        opt.add(b >= 0)

    for i in range(len(targets)):
        target = targets[i]
        relevant_buttons = []
        for press_index, b in enumerate(buttons):
            if i in b:
                relevant_buttons.append(presses[press_index])

        opt.add(sum(relevant_buttons) == target)

    opt.minimize(sum(presses))

    if opt.check() == sat:
        model = opt.model()
        return sum([model[p].as_long() for p in presses])
    else:
        raise ArithmeticError("unsolvable?")


total = 0

for line in data:
    print("\nline", line)

    buttons = [
        [int(e) for e in s.split(",")]
        for s in line[line.index("(") + 1 : line.index("{") - 2].split(") (")
    ]
    targets = [int(e) for e in line[line.index("{") + 1 : -1].split(",")]

    count = solve(targets, buttons)
    print(count)
    total += count

print("\ntotal:", total)
