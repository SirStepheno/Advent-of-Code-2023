with open("Day 3/input.txt") as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]

class Number:
    def __init__(self, val, x_min, y) -> None:
        self.val = int(val)
        self.x_min = x_min
        self.y = y
    
    def set_x_max(self, x_max):
        self.x_max = x_max
    
    def add_digit(self, digit):
        self.val = self.val * 10 + int(digit)
    
    def __repr__(self) -> str:
        return str(self.__dict__) + "\n"
    
class Symbol:
    def __init__(self, val, x, y) -> None:
        self.val = val
        self.x = x
        self.y = y
    
    def near_coord(self, number):
        if number.x_min - 1 <= self.x <= number.x_max + 1 and number.y - 1 <= self.y <= number.y + 1:
            return True
        return False
    
    def __repr__(self) -> str:
        return str(self.__dict__) + "\n"


all_numbers = []
all_symbols = []
for y, line in enumerate(lines):
    # First get all the numbers
    current_number = None
    for x, char in enumerate(line + "."): # Add an point at end, so numbers at the end are saved
        if char.isdigit():
            if current_number != None:
                current_number.add_digit(char)
            else:
                current_number = Number(char, x, y)
        else: # No digit
            if current_number != None:
                current_number.set_x_max(x - 1)
                all_numbers.append(current_number)
                current_number = None
            if char != ".":
                all_symbols.append(Symbol(char, x, y))


def part_one():
    numbers = set()
    for symbol in all_symbols:
        for number in all_numbers:
            if symbol.near_coord(number):
                numbers.add(number)
    
    return sum([number.val for number in numbers])

def part_two():
    total = 0
    for symbol in all_symbols:
        gear_numbers = []
        for number in all_numbers:
            if symbol.near_coord(number):
                gear_numbers.append(number.val)
        if len(gear_numbers) == 2:
            total += gear_numbers[0] * gear_numbers[1]
    
    return total


print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")