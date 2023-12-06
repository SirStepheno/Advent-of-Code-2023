def part_one():
    total = 1
    for time, record in [(59,430),(70,1218),(78,1213),(78,1276)]:
        distances = []
        for press in range(time): # Whole time pressing button never the good answer
            distances.append(press * (time-press))
        total *= sum([1 for x in distances if x > record])
    return total

def part_two():
    time, record = 59707878, 430121812131276
    distances = []
    for press in range(time): # Whole time pressing button never the good answer
        distances.append(press * (time-press))
    return sum([1 for x in distances if x > record])

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")