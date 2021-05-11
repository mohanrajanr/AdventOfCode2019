import collections

with open('data/input.txt') as f:
    limit = tuple(f.readline().strip().split("-"))


def generate_values(index, value, maxval):
    # print(index, value, value[index], maxval)
    if index == len(value) - 1:
        for i in range(int(maxval), 10):
            yield str(i)
        return

    for i in range(int(maxval), 10):
        for j in generate_values(index + 1, value, maxval=i):
            yield str(i) + j
    return

#
# def return_count():
#     count = 0
#     for val in generate_values(0, limit[0], limit[0][0]):
#
#         doubles = 0
#         for i in range(len(val) - 1):
#             if val[i] == val[i + 1]:
#                 if doubles > 1:
#                     break
#                 doubles += 1
#
#         if doubles < 1:
#             continue
#
#         if int(val) > int(limit[1]):
#             break
#
#         if int(limit[0]) <= int(val) <= int(limit[1]):
#             # print(val)
#             count += 1
#             continue
#
#     return count
#
# print(return_count())


def return_count2():
    count = 0
    for val in generate_values(0, limit[0], limit[0][0]):

        doubles = 0
        counter = collections.Counter(val)

        if 2 not in counter.values():
            continue

        if int(val) > int(limit[1]):
            break

        if int(limit[0]) <= int(val) <= int(limit[1]):
            print(val)
            count += 1
            continue

    return count

print(return_count2())
