import numpy as np
from itertools import combinations

with open("Day 11/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def part_both(times):
    galaxy = np.array([list(line) for line in lines])
    x = 0
    for i, row in enumerate(galaxy):
        if not np.count_nonzero(row == "#"):
            galaxy[i] = "!"
    galaxy = galaxy.swapaxes(0,1)
    x = 0
    for i, row in enumerate(galaxy):
        if not np.count_nonzero(row == "#"):
            galaxy[i] = "!"
    galaxy = galaxy.swapaxes(0,1)
    
    x,y = np.where(galaxy == "#")
    total = 0
    for i, combination in enumerate(combinations(zip(x,y), 2)):
        a,b = combination
        warps_vert = galaxy[min(a[0], b[0]):max([a[0], b[0]]) + 1, a[1]]
        warps_horz = galaxy[a[0], min(a[1], b[1]):max([a[1], b[1]]) + 1]
        extra_vert = len(np.nonzero(warps_vert == "!")[0]) * (times)
        extra_horz = len(np.nonzero(warps_horz == "!")[0]) * (times)
        total += abs(b[0] - a[0]) + abs(b[1] - a[1]) + extra_vert + extra_horz

    return total

import time
startTime = time.time()

print(f"Part one: {part_both(1)}")
print(f"Part two: {part_both(1000000 - 1)}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))