import numpy as np
from copy import deepcopy

class Beam:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction
    
    def next_coord(self) -> tuple:
        if self.direction == "N":
            return (self.x, self.y - 1)
        elif self.direction == "E":
            return (self.x + 1, self.y)
        elif self.direction == "S":
            return (self.x, self.y + 1)
        elif self.direction == "W":
            return (self.x - 1, self.y)
        else:
            raise ValueError(f"Invalid direction {self.direction}")
    
    def __repr__(self) -> str:
        return f"{self.direction} {self.x} {self.y}"

class Tile:
    def __init__(self, x, y, sign) -> None:
        self.x = x
        self.y = y
        self.sign = sign
        self.energy = False
        self.directions = ["N", "E", "S", "W"]
    
    def get_beams(self, direction):
        self.energy = True

        # Stop if direction was already calculated for specific tile, to avoid infinity loops
        if direction in self.directions:
            self.directions.remove(direction)
        else:
            return []
        
        new_directions = self.get_new_directions(direction)
        return [Beam(self.x, self.y, new_direction) for new_direction in new_directions]
    
    def get_new_directions(self, direction) -> list:
        if self.sign == "/":
            if direction == "N": return ["E"]
            elif direction == "E": return ["N"]
            elif direction == "S": return ["W"]
            elif direction == "W": return ["S"]
        elif self.sign == "\\":
            if direction == "N": return ["W"]
            elif direction == "E": return ["S"]
            elif direction == "S": return ["E"]
            elif direction == "W": return ["N"]
        elif self.sign == "|":
            if direction == "E" or direction == "W": return ["N", "S"]
            else: return [direction]
        elif self.sign == "-":
            if direction == "N" or direction == "S": return ["E", "W"]
            else: return [direction]
        elif self.sign == ".":
            return [direction]
        else:
            raise ValueError(f"Invalid sign {self.sign}")
    
    def __repr__(self) -> str:
        return "#" if self.energy else "."

with open("Day 16/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    org_grid = np.array([[Tile(x,y,tile) for x, tile in enumerate(line)] for y, line in enumerate(lines)])

def part_one(start_beam):
    grid = deepcopy(org_grid)
    beams = [start_beam]
    while len(beams):
        new_beams = []
        for beam in beams:
            x,y = beam.next_coord()
            if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
                tile = grid[y, x]
                new_beams += tile.get_beams(beam.direction)
        beams = new_beams

    return sum([1 for x in grid.flatten() if x.energy])

def part_two():
    score = 0
    for x in range(org_grid.shape[0]):
        print(x, org_grid.shape[0])
        if part_one(Beam(x,-1,"S")) > score:
            score = part_one(Beam(x,-1,"S"))

        if part_one(Beam(x,org_grid.shape[1],"N")) > score:
            score = part_one(Beam(x,org_grid.shape[1],"N"))
    
    for y in range(org_grid.shape[1]):
        print(y, org_grid.shape[1])
        if part_one(Beam(-1,y,"E")) > score:
            score = part_one(Beam(-1,y,"E"))
            
        if part_one(Beam(org_grid.shape[0],y,"W")) > score:
            score = part_one(Beam(org_grid.shape[0],y,"W"))
    
    return score

import time
startTime = time.time()

print(f"Part one: {part_one(Beam(-1,0,'E'))}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))