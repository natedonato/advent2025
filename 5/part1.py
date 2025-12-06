input = open("input.txt").read()

[ranges, ingredients] = input.split("\n\n")
ranges = [list(map(int, e.split("-"))) for e in ranges.split("\n")]
ranges.sort()
ingredients = list(map(int, ingredients.split("\n")[:-1]))

print(ranges)
print(ingredients)

fresh = 0

for i in ingredients:
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            fresh += 1
            break

print(fresh)
