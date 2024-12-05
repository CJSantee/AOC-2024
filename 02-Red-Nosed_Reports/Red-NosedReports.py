from utils import aoc

filename = aoc.get_input_filename()

part = aoc.get_part()

with open(filename, 'r') as file:
  reports = list(map(lambda line: list(map(int, line.split(' '))), file.readlines()))

def is_safe(report):
    increasing = False
    decreasing = False
    for previous, current in zip(report, report[1:]):
        diff = previous - current
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        increase = diff > 0
        decrease = diff < 0
        if increase and decreasing: 
            return False
        if decrease and increasing:
            return False
        increasing = increase
        decreasing = decrease
    return True

def is_tolerable(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i+1:]):
            return True 
    return False
        
def part_one():
    sum = 0
    for report in reports:
        if is_safe(report):
            sum += 1
    return sum

def part_two():
    sum = 0
    for report in reports:
        if is_tolerable(report):
            sum += 1
    return sum

# Running Parts
if part.lower() in ['one', 'both']:
    print(f"Part One: {part_one()}")
if part.lower() in ['two', 'both']:
    print(f"Part Two: {part_two()}")