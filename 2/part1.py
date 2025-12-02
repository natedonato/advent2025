input = open("input.txt").read()
input = input.split(",")

count = 0

for id_range in input:
    (start, end) = list(map(int, id_range.split("-")))

    for id in range(start, end + 1):
        s = str(id)
        length = len(s)

        if s[:length // 2] == s[length // 2 :]:
            count += id

print(count)
