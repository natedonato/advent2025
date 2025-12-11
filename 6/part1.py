with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

parsed_data = [line.strip().split() for line in data]
nums = parsed_data[:-1]
nums = [[int(el) for el in row] for row in nums]
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
