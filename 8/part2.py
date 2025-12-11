from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

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

def checkComplete():
    size = 0
    seen = set()
    q = deque()
    q.append(0)

    while q:
        curr = q.popleft()
        if curr in seen:
            continue
        seen.add(curr)
        size += 1

        for n in graph[curr]:
            q.append(n)

    return size == len(data)

i = 0

while True:
    next_connection = distances[i]
    point1 = next_connection[1]
    point2 = next_connection[2]

    graph[point1].append(point2)
    graph[point2].append(point1)

    if checkComplete():
        print(data[point1][0] * data[point2][0])
        break

    i += 1
