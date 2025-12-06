with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

number_data = data[:-1]
ops = data[-1]

line_start = 0
total = 0

while line_start < len(ops):
    current_op = ops[line_start]

    line_end = line_start + 1
    while line_end < len(ops) and ops[line_end] == " ":
        line_end += 1

    if line_end != len(ops):
        line_end -= 2
    else:
        line_end -= 1

    val = 0 if current_op == "+" else 1

    for i in range(line_start, line_end + 1):
        current_num = 0
        for line in number_data:
            if line[i] != " ":
                current_num *= 10
                current_num += int(line[i])

        val = val + current_num if current_op == "+" else val * current_num

    total += val
    line_start = line_end + 2

print(total)
