from intcode import IntCode

data = list()
with open('data/input.txt') as f:
    for line in f.readlines():
        stripped = line.strip()
        data.extend(map(int, stripped.split(',')))

# Part 1
new_data = data.copy()
code = IntCode(new_data)
code.run()
print(new_data[0])

# Part 2
for i in range(100):
    for j in range(100):
        new_data = data.copy()
        new_data[1] = i
        new_data[2] = j
        print(new_data)
        code = IntCode(new_data)
        code.run()
        print(new_data[0])
        if new_data[0] == 19690720:
            print("{} {} {}".format(i, j, 100 * i + j))
            exit()
        else:
            print("Nope")
