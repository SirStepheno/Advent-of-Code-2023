class Instruction:
    def __init__(self, letter, compare, value, workflow):
        self.letter = letter
        self.compare = compare
        self.value = int(value)
        self.workflow = workflow
    
    def __repr__(self):
        return f"{self.letter} {self.compare} {self.value} {self.workflow}"

class Workflow:
    def __init__(self, name):
        self.name = name
        self.instructions = [] 
        self.default_workflow = None
    
    def parse_instruction(self, instruction):
        instructions = instruction.split("{")[1][:-1].split(",")
        self.default_workflow = instructions[-1]
        for instruction in instructions[:-1]:
            if ">" in instruction:
                letter, value = instruction.split(">")
                value, workflow = value.split(":")
                self.instructions.append(Instruction(letter, ">", value, workflow))
            elif "<" in instruction:
                letter, value = instruction.split("<")
                value, workflow = value.split(":")
                self.instructions.append(Instruction(letter, "<", value, workflow))
            else:
                raise ValueError("Invalid instruction: " + instruction)
    
    def get_next_workflow(self, parts):
        for instruction in self.instructions:
            if instruction.compare == ">" and parts[instruction.letter] > instruction.value:
                return instruction.workflow
            elif instruction.compare == "<" and parts[instruction.letter] < instruction.value:
                return instruction.workflow
        return self.default_workflow
    
    def __repr__(self):
        return f"{self.name} {self.instructions} {self.default_workflow}"

with open("Day 19/workflows.txt") as f:
    workflows = {}
    input_workflows = [line[:-1] for line in f.readlines()]
    for input_workflow in input_workflows:
        name = input_workflow.split("{")[0]
        workflow = Workflow(name)
        workflow.parse_instruction(input_workflow)
        workflows[name] = workflow

with open("Day 19/parts.txt") as f:
    parts = []
    input_parts = [line[:-1] for line in f.readlines()]
    for input_part in input_parts:
        values = {key: int(value) for key, value in [x.split("=") for x in input_part[1:-1].split(",")]}
        parts.append(values)

def part_one():
    total = 0
    for part in parts:
        workflow = workflows["in"]
        while True:
            new_workflow = workflow.get_next_workflow(part)

            if new_workflow == "A":
                print(part, "A")
                for value in part.values():
                    total += value
                break

            elif new_workflow == "R":
                print(part, "R")
                break
            
            workflow = workflows[new_workflow]

    return total

def part_two():
    return 0

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))