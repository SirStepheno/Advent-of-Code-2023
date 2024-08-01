class Instruction:
    def __init__(self, letter, compare, value, workflow):
        self.letter = letter
        self.compare = compare
        self.value = int(value)
        self.workflow = workflow
    
    def get_new_ranges(self, current_range: range):
        if self.compare == ">":
            true_range = range(self.value + 1, 4001)
            false_range = range(1, self.value + 1)
        elif self.compare == "<":
            true_range = range(1, self.value)
            false_range = range(self.value, 4001)
        
        # Check the overlap between the current range and the true range and false range
        true_range = range(max(true_range.start, current_range.start), min(true_range.stop, current_range.stop))
        false_range = range(max(false_range.start, current_range.start), min(false_range.stop, current_range.stop))
        
        return true_range, false_range

    def get_workflow(self):
        if self.workflow == "A":
            return "A"
        elif self.workflow == "R":
            return "R"
        return workflows[self.workflow]
    
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
    
    def get_default_workflow(self):
        if self.default_workflow == "A":
            return "A"
        elif self.default_workflow == "R":
            return "R"
        return workflows[self.default_workflow]
        
    
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
                for value in part.values():
                    total += value
                break

            elif new_workflow == "R":
                break
            
            workflow = workflows[new_workflow]

    return total

def part_two():
    workflow = workflows["in"]
    all_workflow_ranges = [[workflow, {"x":range(1,4001), "m":range(1,4001), "a":range(1,4001), "s":range(1,4001)}]]
    new_workflow_ranges = []
    total = 0
    while len(all_workflow_ranges) > 0:
        for workflow, parts in all_workflow_ranges:
            current_parts = parts.copy()
            for instruction in workflow.instructions:
                true_range, false_range = instruction.get_new_ranges(current_parts[instruction.letter])
                # If true range
                if len(true_range):
                    new_parts = current_parts.copy()
                    new_parts[instruction.letter] = true_range
                    new_workflow_ranges.append([instruction.get_workflow(), new_parts])

                # If false range
                if len(false_range):
                    new_parts = current_parts.copy()
                    new_parts[instruction.letter] = false_range
                    current_parts = new_parts
            
            # If default workflow
            new_workflow_ranges.append([workflow.get_default_workflow(), current_parts])
        
        all_workflow_ranges = []

        for workflow, parts in new_workflow_ranges:
            if workflow == "A":
                r = 1
                for part in parts.values():
                    r *= len(part)
                total += r
            elif workflow == "R":
                continue
            else:
                all_workflow_ranges.append([workflow, parts])  
        new_workflow_ranges = []
    
    return total
        


import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))