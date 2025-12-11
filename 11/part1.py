from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

graph = {}

for line in data:
    current = line[:3]
    connected_nodes = line[4:].split()
    graph[current] = connected_nodes

queue = deque()
queue.append("you")

count = 0
while queue:
    curr = queue.popleft()

    if curr == "out":
        count += 1
        continue

    if not graph[curr]:
        continue

    for child in graph[curr]:
        queue.append(child)

print(count)
