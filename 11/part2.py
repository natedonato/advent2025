from collections import deque

with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

graph = {}
graph["out"] = {"children": [], "num_visits": [0, 0, 0, 0], "parent_count": 0}

for line in data:
    current = line[:3]
    graph[current] = {"children": [], "num_visits": [0, 0, 0, 0], "parent_count": 0}

for line in data:
    current = line[:3]
    connected_nodes = line[4:].split()
    graph[current]["children"] = connected_nodes
    for node in connected_nodes:
        graph[node]["parent_count"] += 1

graph["svr"]["num_visits"][0] += 1

queue = deque()
queue.append("svr")

while queue:
    current = queue.popleft()
    current_visits = graph[current]["num_visits"]

    if current == "fft":
        current_visits[3] = current_visits[2]
        current_visits[1] = current_visits[0]
        current_visits[0] = 0
        
    if current == "dac":
        current_visits[3] = current_visits[1]
        current_visits[2] = current_visits[0]
        current_visits[0] = 0

    for child in graph[current]["children"]:
        for i in range(4):
            graph[child]["num_visits"][i] += current_visits[i]
        
        graph[child]["parent_count"] -= 1
        if graph[child]["parent_count"] == 0:
            queue.append(child)

print(graph["out"]["num_visits"][3])
