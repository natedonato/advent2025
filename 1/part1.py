with open("./input.txt", "r") as file:
    input = file.read().split("\n")[:-1]

start = 50
count = 0

for line in input:
    dir = line[0]
    num = int(line[1:])

    if dir == "L":
        num *= -1

    start += num
    start %= 100

    if start == 0:
        count += 1

print(count)
