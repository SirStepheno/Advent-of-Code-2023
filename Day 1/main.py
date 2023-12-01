with open("Day 1/input.txt") as f:
    lines = f.readlines()

def getFirstAbsoluteInt(input):
    for char in input:
        if char.isdigit():
            return input.find(char), int(char)
    return None, 0
        
def getFirstWrittenInt(input, inverted = False):
    lowest_char = None
    lowest_index = None
    for key, value in language_to_int.items():

        if inverted:
            key = key[::-1]
        
        index = input.find(key)
        if index >= 0 and (lowest_index == None or index < lowest_index):
            lowest_char, lowest_index = value, index
    
    if lowest_char:
        return lowest_index, int(lowest_char)
    return None, 0



def getFirstInt(input, inverted = False):
    if inverted:
        input = input[::-1]

    abs_index, abs = getFirstAbsoluteInt(input)
    written_index, written = getFirstWrittenInt(input, inverted=inverted)

    if written_index == None:
        return abs
    elif abs_index == None:
        return written
    elif written_index < abs_index:
        return written
    elif abs_index < written_index:
        return abs
    else:
        raise ValueError(f"Can't happen with abs index {abs_index} and written index {written_index}")

language_to_int = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    
}

result = 0

for line in lines:
    result += getFirstInt(line) * 10 + getFirstInt(line, inverted=True)

print(result)