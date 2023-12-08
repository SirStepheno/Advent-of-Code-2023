from math import lcm


with open("Day 8/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]


instructions = lines[0]
data = {}
for line in lines[2:]:
    key, value = line.split(" = ")
    values = value.replace("(", "").replace(")", "").split(", ")
    data[key] = tuple(values)


def find(pointer):
    for x in range(1000):
        for i, instruction in enumerate(instructions, start=1):
            if instruction == "L":
                pointer = data[pointer][0]
            else:
                pointer = data[pointer][1]
            
            if pointer[-1] == "Z":
                return x * len(instructions) + i


def part_one():
    return find("AAA")
    

def part_two():
    # Checked that from first Z value each instructions became a loop, so use the first value as base and calculate the Least Common Multiple
    pointers = [key for key in data.keys() if key[-1] == "A"]
    loops = []
    for pointer in pointers:
        loops.append(find(pointer))
    
    return lcm(*loops)

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))