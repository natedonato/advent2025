with open("./input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

start = 50
count = 0

for line in input:
    dir = line[0]
    num = int(line[1:])

    sign = 1
    if dir == "L":
        sign = -1

    full_rotations = num // 100
    count += full_rotations

    remainder = num % 100

    if dir == "L" and remainder >= start:
        if start != 0:
            count += 1

    if dir == "R" and start + remainder >= 100:
        count += 1

    start = start + (sign * num)
    start %= 100

print(count)
