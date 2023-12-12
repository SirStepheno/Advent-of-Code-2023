with open("Day 10/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

class Grid:
    def __init__(self, rows) -> None:
        self.grid = []
        self.steps = 0
        for y, row in enumerate(rows):
            res = []
            for x, item in enumerate(row):
                if item == "S":
                    self.current_char = Pipe("|")
                    res.append(self.current_char)
                    self.x = x
                    self.y = y
                    
                elif item == ".":
                    res.append(".")
                else:
                    res.append(Pipe(item))
            self.grid.append(res)
        self.init_coords = (self.x, self.y)
    
    def get_char(self, x, y):
        return self.grid[y][x]

    def get_current_char(self):
        return self.current_char
    
    def move(self, direction):
        if direction == "N":
            self.y -= 1
        elif direction == "S":
            self.y += 1
        elif direction == "E":
            self.x += 1
        elif direction == "W":
            self.x -= 1
        else:
            raise ValueError(f"Direction {direction} not valid")
        self.current_char = self.get_char(self.x, self.y)
        self.current_char.enter(direction)
        self.steps += 1
    
    def check_end(self):
        if (self.x, self.y) == self.init_coords:
            return True
        return False
    
    def to_binary_grid(self):
        new_grid = []
        for row in self.grid:
            new_grid.append([1 if item != "." and item.in_loop else 0 for item in row])
        self.grid = new_grid
    
    def to_file(self, filename):
        with open(f'Day 10/{filename}.txt', 'w') as file:
            for i, row in enumerate(self.grid):
                file.write("".join([str(item.letter) if item != "." and item.in_loop else "!" for item in row]) + "\n")
    
    def to_binary_file(self, filename):
        with open(f'Day 10/{filename}.txt', 'w') as file:
            for i, row in enumerate(self.grid):
                file.write("".join([str(item) for item in row]) + "\n")


    def __repr__(self) -> str:
        result = " " + "".join([str(x) for x in range(len(self.grid[0]))]) + "\n"
        for i, row in enumerate(self.grid):
            result += str(i) + "".join([str(item.letter) if item != "." else item for item in row]) + "\n"
        result += f"({self.x}, {self.y})"
        return result

class Pipe:
    def __init__(self, letter) -> None:
        lookup = {
            "F": ["S", "E"],
            "7": ["S", "W"],
            "L": ["N", "E"],
            "J": ["N", "W"],
            "|": ["N", "S"],
            "-": ["W", "E"]
        }
        self.letter = letter
        self.directions = lookup[letter]
        self.in_loop = False
    
    def enter(self, direction):
        self.in_loop = True
        if direction == "N":
            self.directions.remove("S")
        elif direction == "S":
            self.directions.remove("N")
        elif direction == "E":
            self.directions.remove("W")
        elif direction == "W":
            self.directions.remove("E")
        else:
            raise ValueError(f"Direction {direction} not valid")

    def next(self):
        return self.directions.pop(0)
    
    def __repr__(self) -> str:
        return f"{self.letter} -> {self.directions}"

grid = Grid(lines)

def part_one():
    while True:
        next_direction = grid.get_current_char().next()
        grid.move(next_direction)
        if grid.check_end():
            break
    return grid.steps / 2


def part_two():
    grid.to_file("output")
    grid.to_binary_grid()
    grid.to_binary_file("output1")
    from skimage.morphology import flood_fill
    import numpy as np
    new_array = np.array(grid.grid)
    new_array = np.pad(new_array, pad_width=1, mode='constant', constant_values=0)
    grid.grid = flood_fill(new_array, (0, 0), 2)
    grid.to_binary_file("output2")
    print(sum([np.count_nonzero(row == 0) for row in grid.grid]))


import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))