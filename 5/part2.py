input = open("input.txt").read()

[ranges, ingredients] = input.split("\n\n")
ranges = list(map(lambda e: list(map(int, e.split("-"))), ranges.split("\n")))
ranges.sort()

count = 0
prev_max = 0

for r in ranges:
    prev_max = max(prev_max, r[0])
    
    if prev_max <= r[1]:
        count += r[1] - prev_max + 1
        prev_max = r[1] + 1

print(count)
