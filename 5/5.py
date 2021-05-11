from intcode import IntCode

data = list()
with open('data/input.txt') as f:
    for line in f.readlines():
        stripped = line.strip()
        data.extend(map(int, stripped.split(',')))


new_data = data.copy()
code = IntCode(new_data)
code.run()
print(new_data[0])