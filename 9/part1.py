with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

data = [[int(e) for e in line.split(",")] for line in data]
max_area = 0

for p in range(len(data) - 1):
    for q in range(p + 1, len(data)):
        point1 = data[p]
        point2 = data[q]

        width = abs(point1[0] - point2[0]) + 1
        height = abs(point1[1] - point2[1]) + 1
        max_area = max(max_area, width * height)

print(max_area)
