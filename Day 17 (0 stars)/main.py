import numpy as np
from copy import deepcopy

class Node():
    def __init__(self, weigth, coord, end_coord) -> None:
        self.x, self.y = coord
        self.weigth = weigth
        self.heuristic = (end_coord[0] - coord[0]) ** 2 + (end_coord[1] - coord[1]) ** 2
        self.total = 0
        self.directions = []
        self.previous_nodes = []
    
    def get_children(self, grid):
        children = []
        
        # S
        if self.directions[-1:] != ["N"] and not self.directions[-3:] == ["S" * 3]:
            if 0 <= self.y + 1 < len(org_grid):
                children.append((org_grid[self.y + 1][self.x], "S"))
        # "N"
        if self.directions[-1:] != ["S"] and not self.directions[-3:] == ["N" * 3]:
            if 0 <= self.y - 1 < len(org_grid):
                children.append((org_grid[self.y - 1][self.x], "N"))
        # "E"
        if self.directions[-1:] != ["W"] and not self.directions[-3:] == ["E" * 3]:
            if 0 <= self.x + 1 < len(org_grid[0]):
                children.append((org_grid[self.y][self.x + 1], "E"))
        # "W"
        if self.directions[-1:] != ["E"] and not self.directions[-3:] == ["W" * 3]:
            if 0 <= self.x - 1 < len(org_grid[0]):
                children.append((org_grid[self.y][self.x - 1], "W"))
        
        return children
    
    def __repr__(self) -> str:
        return f"{self.directions}, ({self.x},{self.y})"

def a_start(start_point, end_point):
    grid = deepcopy(org_grid)
    openlist = [grid[start_point[1]][start_point[0]]]
    clostedlist = []
    while len(openlist):
        # Get the current node
        openlist = sorted(openlist, key=lambda x: x.weigth)
        current_node = openlist.pop(0)
        clostedlist.append(current_node)
    
        # Found the goal
        if current_node == grid[end_point[1]][end_point[0]]:
            return current_node

        # Get children
        children = current_node.get_children(grid)
        
        # Check children
        for child, direction in children:
            if child in clostedlist:
                continue
            
            new_total = child.weigth + child.heuristic + current_node.total

            if child in openlist:
                if child.total > new_total:
                    continue
                else:
                    child.directions.append(direction)
                    child.total = new_total

            else:
                child.directions.append(direction)
                child.total = new_total
                openlist.append(child)
        
        print(current_node,openlist)
        input()
    
    raise ValueError("No path found")
    



def part_one():
    x = a_start((0,0), (len(org_grid[0])-1, len(org_grid)-1))
    print(x, x.__dict__)

def part_two():
    pass

with open("Day 17/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    org_grid = np.array([[Node(int(num), (x,y), (len(lines[0]), len(lines))) for x, num in enumerate(line)] for y, line in enumerate(lines)])
    print(org_grid)

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))