with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

parsed_data = []

for line in data:
    parsed_line = ""
    for i, c in enumerate(line):
        if c != " " or (i > 0 and line[i - 1] != " "):
            parsed_line += c

    parsed_data.append(parsed_line.strip())

parsed_data = [line.split(" ") for line in parsed_data]
nums = parsed_data[:-1]
nums = [list(map(int, row)) for row in nums]
ops = parsed_data[-1]

total = 0

for i, op in enumerate(ops):
    if op == "+":
        val = 0
        for line in nums:
            val += line[i]
        total += val
    elif op == "*":
        val = 1
        for line in nums:
            val *= line[i]
        total += val

print(total)
