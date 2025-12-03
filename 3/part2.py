input = open("input.txt", "r").read().split("\n")[:-1]
total = 0

for line in input:
    line = list(map(int, [c for c in line]))

    line_len = len(line)
    num_skips = line_len - 12

    current_idx = 0
    digits = []

    while len(digits) < 12:
        next_digit = max(line[current_idx : current_idx + num_skips + 1])
        
        while line[current_idx] != next_digit:
            current_idx += 1
            num_skips -= 1
        
        digits.append(next_digit)
        current_idx += 1

    joltage = int(("").join([str(i) for i in digits]))
    total += joltage

print(total)
