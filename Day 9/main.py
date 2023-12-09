with open("Day 9/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def part_one():
    total = 0
    for line in lines:
        history = [[int(val) for val in line.split(" ")]]
        while any(history[-1]):
            history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1])-1)])
        
        total += sum([item[-1] for item in history])
    return total

def part_two():
    total = 0
    for line in lines:
        history = [[int(val) for val in line.split(" ")]]
        while any(history[-1]):
            history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1])-1)])
        
        result = [0]
        for arr in history[::-1][1:]:
            result.append(arr[0] - result[-1])
        total += result[-1]
    return total

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))