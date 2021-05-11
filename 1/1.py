

data = list()
with open('input.txt') as f:
    for line in f.readlines():
        stripped = line.strip()
        data.append(stripped)

# print(data)


print("Part 1")
sumval = 0
for d in data:
    sumval += (int(d)//3) - 2

print(sumval)

print("Part 2")
sumval = 0
for d in data:
    curr = fuel = (int(d)//3) - 2
    while (fuel//3) - 2 > 0:
        # print(fuel)
        fuel = (fuel//3) - 2
        curr += fuel
    # print("Here:{}".format(curr))
    sumval += curr

print(sumval)
