from collections import deque


with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]


data = [[int(e) for e in line.split(",")] for line in data]

xs, ys = zip(*data)
xs = list(set(xs))
ys = list(set(ys))

xs.sort()
ys.sort()

x_decompress = {}
x_compress = {}
y_compress = {}
y_decompress = {}

i = 2
for x in xs:
    x_compress[x] = i
    x_decompress[i] = x
    i += 1

grid_width = i + 2

i = 2
for y in ys:
    y_compress[y] = i
    y_decompress[i] = y
    i += 1

grid_height = i + 2
grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]


def prettyPrint():
    for line in grid:
        print("".join(line))


# takes in input coordinate, returns compressed grid coordinate
def compress(p):
    return [x_compress[p[0]], y_compress[p[1]]]


# takes in "compressed" grid coord, returns true input coordinate
def decompress(p):
    return [x_decompress[p[0]], y_decompress[p[1]]]


def drawBetween(p1, p2):
    if p1[0] == p2[0]:
        ys = [p1[1], p2[1]]
        ys.sort()

        for y in range(ys[0] + 1, ys[1]):
            grid[y][p1[0]] = "X"
    else:
        xs = [p1[0], p2[0]]
        xs.sort()
        for x in range(xs[0] + 1, xs[1]):
            grid[p1[1]][x] = "X"


compressed_data = [compress(e) for e in data]
prev = compressed_data[-1]

for p in compressed_data:
    [x, y] = p
    grid[y][x] = "#"
    drawBetween(prev, p)
    prev = p


def floodfill():
    start = (0, 0)
    q = deque([start])
    seen = set(start)

    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        grid[curr[0]][curr[1]] = " "

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                r = curr[0] + dr
                c = curr[1] + dc

                if (
                    r >= 0
                    and r < len(grid)
                    and c >= 0
                    and c < len(grid[0])
                    and grid[r][c] == "."
                ):
                    q.append((r, c))


floodfill()


def checkValid(p1, p2):
    xs = [p1[0], p2[0]]
    ys = [p1[1], p2[1]]
    xs.sort()
    ys.sort()

    for x in range(xs[0], xs[1] + 1):
        for y in range(ys[0], ys[1] + 1):
            if grid[y][x] == " ":
                return False

    return True


max_area = 0

for i, p in enumerate(compressed_data):
    for j, p2 in enumerate(compressed_data):
        if i < j and checkValid(p, p2):
            true_p1 = decompress(p)
            true_p2 = decompress(p2)
            width = abs(true_p1[0] - true_p2[0]) + 1
            height = abs(true_p1[1] - true_p2[1]) + 1

            max_area = max(max_area, width * height)

print(max_area)
