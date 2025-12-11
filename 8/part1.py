from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

num_connections_to_make = 1000

data = [d.split(",") for d in data]
data = [list(map(int, line)) for line in data]

distances = []

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        point1 = data[i]
        point2 = data[j]
        dist = (
            (point1[0] - point2[0]) ** 2
            + (point1[1] - point2[1]) ** 2
            + (point1[2] - point2[2]) ** 2
        )
        distances.append((dist, i, j))

distances.sort()

graph = {}

for i in range(len(data)):
    graph[i] = []

for i in range(num_connections_to_make):
    next_connection = distances[i]
    point1 = next_connection[1]
    point2 = next_connection[2]
    graph[point1].append(point2)
    graph[point2].append(point1)

sizes = []
seen = set()

for node in graph:
    if node in seen:
        continue

    size = 0
    q = deque()
    q.append(node)

    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        size += 1

        for n in graph[curr]:
            q.append(n)

    sizes.append(size)

sizes.sort(reverse=True)

product = 1

for size in sizes[:3]:
    product *= size

print(product)
