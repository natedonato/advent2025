with open("./input.txt") as file:
    data = file.read().split("\n")[:-1]

current_beams = set()
current_beams.add(data[0].find("S"))
split_count = 0

for line in data[1:]:
    next_beams = set()
    for beam in current_beams:
        if line[beam] == "^":
            next_beams.add(beam - 1)
            next_beams.add(beam + 1)
            split_count += 1
        else:
            next_beams.add(beam)

    current_beams = next_beams

print(split_count)
