import numpy as np

with open("Day 13/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    matrixes = [[]]
    i = 0
    for line in lines:
        if len(line):
            matrixes[-1].append([x for x in line])
        else:
            matrixes.append([])
    matrixes = [np.array(matrix) for matrix in matrixes]

def get_reflection_rows(matrix, marge):
    x = []
    for i in range(1, matrix.shape[0]):
        upper, lower = np.flipud(matrix[:i]), matrix[i:]
        if len(np.where(upper[:min(upper.shape[0], lower.shape[0])] != lower[:min(upper.shape[0], lower.shape[0])])[0]) == marge:
            x.append(i)
    if len(x) > 1:
        raise ValueError(f"Multiple found rows {x}")
    elif len(x):
        return x[0]
    else:
        return 0       

def part_one():
    total = 0
    for matrix in matrixes:
        total += 100 * get_reflection_rows(matrix, 0)
        total += get_reflection_rows(np.swapaxes(matrix, 0, 1), 0)
    return total      

def part_two():
    total = 0
    for matrix in matrixes:
        total += 100 * get_reflection_rows(matrix, 1)
        total += get_reflection_rows(np.swapaxes(matrix, 0, 1), 1)
    return total

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))