with open("Day 15/input.txt") as f:
    line = f.readlines()[0]

def get_ascii(input):
    subtotal = 0 
    for char in input:
        subtotal += ord(char)
        subtotal *= 17
        subtotal %= 256
    return subtotal

def part_one():
    total = 0
    for instruction in line.split(","):
        total += get_ascii(instruction)
    return total

def part_two():
    boxes = {x: {} for x in range(256)}
    for instruction in line.split(","):
        if "=" in instruction:
            box, lens = instruction.split("=")
            boxes[get_ascii(box)][box] = int(lens)
        elif "-" in instruction:
            box = instruction[:-1]
            if box in boxes[get_ascii(box)].keys():
                del boxes[get_ascii(box)][box]
        else:
            raise ValueError(instruction)
    
    total = 0
    for key, value in boxes.items():
        for i, value1 in enumerate(value.values(), start = 1):
            total += (key + 1) * i * value1
    return total
        

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))