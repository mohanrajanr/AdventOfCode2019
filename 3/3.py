points = list()
with open('data/input.txt') as f:
    for line in f.readlines():
        stripped = line.strip()
        points.append(stripped.split(','))


# def get_coords(instructions):
#     directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
#     points = set()
#     x = y = 0
#     for inst in instructions:
#         dx, dy = directions[inst[0]]
#         for i in range(int(inst[1:])):
#             x += dx
#             y += dy
#             points.add((x, y))
#
#     return points
#
# coordinates = []
# for point in points:
#     coordinates.append(get_coords(point))
#
# intersection = coordinates[0].intersection(coordinates[1])
# print(intersection)
# min_intersection = min([sum([abs(x), abs(y)]) for (x, y) in intersection])
# print(min_intersection)


def get_coords(instructions):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    points = dict()
    x = y = step = 0
    for inst in instructions:
        dx, dy = directions[inst[0]]
        for i in range(int(inst[1:])):
            x += dx
            y += dy
            step += 1
            points[(x, y)] = step

    return points

coordinates = []
for point in points:
    coordinates.append(get_coords(point))

intersection = [point for point in coordinates[0] if point in coordinates[1]]
print(intersection)
min_intersection = min([sum([coordinates[0][(x, y)], coordinates[1][(x, y)]]) for (x, y) in intersection])
print(min_intersection)
