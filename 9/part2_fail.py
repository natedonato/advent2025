from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]


data = [[int(e) for e in line.split(",")] for line in data]

lines = []
prev_point = data[-1]

# (x, y1, y2)
vertical_lines = []

# (y, x1, x2)
horizontal_lines = []

for p in data:
    if prev_point[0] == p[0]:
        y_vals = sorted([p[1], prev_point[1]])
        vertical_lines.append((p[0], y_vals[0], y_vals[1]))
    else:
        x_vals = sorted([p[0], prev_point[0]])
        horizontal_lines.append((p[1], x_vals[0], x_vals[1]))
    prev_point = p

horizontal_lines.sort()
vertical_lines.sort()


def checkVertical(p1, p2):
    x_range = sorted([p1[0], p2[0]])
    y_range = sorted([p1[1], p2[1]])
    prev_horizontal = []

    for x in range(x_range[0], x_range[1]):
        x += 0.5

        lines_crossed = 0

        y1 = y_range[0]

        relevant_horizontal_lines = [
            line[0]
            for line in horizontal_lines
            if line[1] <= x and line[2] >= x and line[0] <= y_range[1]
        ]

        if prev_horizontal == relevant_horizontal_lines:
            continue
        
        prev_horizontal = relevant_horizontal_lines[:]

        relevant_horizontal_lines = deque(relevant_horizontal_lines)

        for y in relevant_horizontal_lines:
            if y < y1:
                lines_crossed += 1

        for _ in range(lines_crossed):
            relevant_horizontal_lines.popleft()

        # print("lines_crossed before start ", lines_crossed)
        y = y_range[0]
        while y < y_range[1] + 1:
            if relevant_horizontal_lines and relevant_horizontal_lines[0] == y:
                lines_crossed += 1
                y += 1
                relevant_horizontal_lines.popleft()
            else:
                if lines_crossed % 2 == 0:
                    return False
                if relevant_horizontal_lines:
                    y = relevant_horizontal_lines[0]
                else:
                    y += 1

    return True


max_area = 0

for p in range(len(data)):
    print(p)
    for q in range(p + 1, len(data)):
        point1 = data[p]
        point2 = data[q]

        if checkVertical(point1, point2):
            width = abs(point1[0] - point2[0]) + 1
            height = abs(point1[1] - point2[1]) + 1
            max_area = max(max_area, width * height)

print(max_area)

