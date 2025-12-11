with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

current_beams = [0] * len(data[0])
current_beams[data[0].find("S")] = 1

for line in data[1:]:
    next_beams = [0] * len(data[0])
    
    for i, count in enumerate(current_beams):
        if line[i] == "^":
            next_beams[i - 1] += count
            next_beams[i + 1] += count
        else:
            next_beams[i] += count
    current_beams = next_beams

print(sum(current_beams))
