with open("Day 10/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

class Grid:
    def __init__(self, rows) -> None:
        self.grid = []
        self.coord_loop = []
        self.steps = 0
        for y, row in enumerate(rows):
            res = []
            for x, item in enumerate(row):
                if item == "S":
                    self.current_char = Pipe("|", x, y)
                    res.append(self.current_char)
                    self.x = x
                    self.y = y
                else:
                    res.append(Pipe(item, x, y))
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
        self.coord_loop.append([self.x,self.y])
        self.current_char.enter(direction)
        self.steps += 1
    
    def check_end(self):
        if (self.x, self.y) == self.init_coords:
            return True
        return False
    
    def to_file(self, filename):
        with open(f'Day 10/{filename}.txt', 'w') as file:
            for i, row in enumerate(self.grid):
                file.write("".join([str(item.letter) if item.in_loop else "!" for item in row]) + "\n")

    def __repr__(self) -> str:
        result = " " + "".join([str(x) for x in range(len(self.grid[0]))]) + "\n"
        for i, row in enumerate(self.grid):
            result += str(i) + "".join([str(item.letter) if item != "." else item for item in row]) + "\n"
        result += f"({self.x}, {self.y})"
        return result

class Pipe:
    def __init__(self, letter, x, y) -> None:
        lookup = {
            "F": ["S", "E"],
            "7": ["S", "W"],
            "L": ["N", "E"],
            "J": ["N", "W"],
            "|": ["N", "S"],
            "-": ["W", "E"]
        }
        self.letter = letter
        if letter in lookup.keys():
            self.directions = lookup[letter]
        self.in_loop = False
        self.side = "!"
        self.x = x
        self.y = y
    
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
        return self.letter

lines = ["." * (len(lines[0]) + 2)] + ["." + line + "." for line in lines] + ["." * (len(lines[0]) + 2)]
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

    # Calculate area
    coord_loop = grid.coord_loop
    coord_loop.append(coord_loop[0])
    A = 0
    for i in range(len(coord_loop) - 1):
        A += coord_loop[i][0] * coord_loop[i + 1][1] - coord_loop[i][1] * coord_loop[i + 1][0]
    A = abs(A / 2)

    # Calculate inner points
    b = len(coord_loop) - 1
    i = A - (b/2) + 1

    return i
                


import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))