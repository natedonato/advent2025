input = open("input.txt").read()
input = input.split(",")

count = 0

for id_range in input:
    (start, end) = list(map(int, id_range.split("-")))

    for id in range(start, end + 1):
        s = str(id)
        length = len(s)

        for i in range(1, length):
            if length % i == 0:
                first = s[:i]
                invalid = True

                for j in range(1, length // i):
                    current = s[j * i : j * i + i]
                    if current != first:
                        invalid = False
                        break

                if invalid:
                    count += id
                    break

print(count)
