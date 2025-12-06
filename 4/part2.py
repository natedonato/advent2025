input = open("input.txt", "r").read().split("\n")[:-1]
input = [list(i) for i in input]
m = len(input)
n = len(input[0])

def getNeighborCount(r, c):
    count = 0
    
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if dr == 0 and dc == 0:
                continue

            r1 = r + dr
            c1 = c + dc

            if r1 >= 0 and r1 < m and c1 >= 0 and c1 < n:
                val = input[r1][c1]
                if val == "@":
                    count += 1

    return count

available = 0
changed = True

while changed:
    changed = False
    for r in range(m):
        for c in range(n):
            if input[r][c] == "@":
                if getNeighborCount(r, c) < 4:
                    available += 1
                    changed = True
                    input[r][c] = "."

print(available)
