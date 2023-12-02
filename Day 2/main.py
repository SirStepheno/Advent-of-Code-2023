from numpy import prod

with open("Day 2/input.txt") as f:
    lines = f.readlines()

def part_one():
    max_bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def checkGame(turns):
        for turn in turns:
            cubes = turn.split(", ")
            for cube in cubes:
                amount, color = cube.split(" ")
                if int(amount) > max_bag[color]:
                    return False
        return True
    
    total = 0
    for line in lines:
        game_id, turns = int(line[:-1].split(": ")[0].replace("Game", "")), line[:-1].split(": ")[1].split("; ")
        if checkGame(turns):
            total += game_id
    
    return total

def part_two():

    def getMinimalBag(turns):
        bag = {"red": None, "green": None, "blue": None}
        for turn in turns:
            cubes = turn.split(", ")
            for cube in cubes:
                amount, color = cube.split(" ")
                if bag[color] == None or int(amount) > bag[color]:
                    bag[color] = int(amount)
        return bag
    
    total = 0
    for line in lines:
        game_id, turns = int(line[:-1].split(": ")[0].replace("Game", "")), line[:-1].split(": ")[1].split("; ")
        min_bag = getMinimalBag(turns)
        total += prod(list(min_bag.values()))
    
    return total



print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")
