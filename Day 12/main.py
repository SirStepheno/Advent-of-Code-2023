from itertools import product
with open("Day 12/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def build(input, numbers):
    result = []
    for i in input:
        if i == -1:
            result.append(numbers.pop(0))
        else:
            result.append(i)
    return result

def count(input):
    count = []
    current_count = 0
    for i in input:
        if i:
            current_count += 1
        elif not i and current_count:
            count.append(current_count)
            current_count = 0
    
    if current_count:
        count.append(current_count)

    return count

def part_one():
    total = 0
    for line in lines:
        data, amount = line.split(" ")
        amount = [int(char) for char in amount.split(",")]
        data = [1 if char == "#" else -1 if char == "?" else 0 for char in data]
        products = [pro for pro in product(range(2), repeat=data.count(-1)) if pro.count(1) + data.count(1) == sum(amount)]
        for pro in products:
            new_data = build(data.copy(), list(pro))
            if count(new_data) == amount:
                total += 1
    return total


def part_two():
    total = 0
    for line in lines:
        t = 0
        data, amount = line.split(" ")
        amount = [int(char) for char in amount.split(",")]
        data = [1 if char == "#" else -1 if char == "?" else 0 for char in data]
        data.append(-1)
        products = [pro for pro in product(range(2), repeat=data.count(-1)) if pro.count(1) + data.count(1) == sum(amount)]
        for pro in products:
            new_data = build(data.copy(), list(pro))
            if count(new_data) == amount:
                total += 1
                t += 1
        print(t)
    return total

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))