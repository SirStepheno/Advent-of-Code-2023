import numpy as np

with open("Day 14/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    grid = np.array([list(line) for line in lines])

def move(row):
    while True:
        changed = False
        for i in range(1, len(row)):
            if row[i] == "O" and row[i - 1] == ".":
                row[i], row[i - 1] = ".", "O"
                changed = True
        
        if not changed:
            return row

def score(grid):
    total = 0
    for i, row in enumerate(np.flipud(grid), start=1):
        total += i * np.count_nonzero(row == "O")
    return total

def part_one(grid):
    for i in range(grid.shape[1]):
        grid[:,i] = move(grid[:,i])
    return score(grid)
    
def part_two(grid):
    scores = []
    for rot in range(1, 501):
        for _ in range(4):
            for i in range(grid.shape[1]):
                grid[:,i] = move(grid[:,i])
            grid = np.rot90(grid, -1)
        scores.append((rot, score(grid)))
    
    with open(f'Day 14/output.txt', 'w') as file:
        for i, weight in scores:
            file.write(f"{i} - {weight}\n")
    start, length = int(input("Give a first repeat location: ")), int(input("How many elements in loop: "))
    return scores[start + ((1000000000 - start) % length) - 1][1]

import time
startTime = time.time()

print(f"Part one: {part_one(grid.copy())}")
print(f"Part two: {part_two(grid.copy())}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))