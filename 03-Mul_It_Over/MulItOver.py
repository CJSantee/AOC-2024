from utils import aoc
import re

filename = aoc.get_input_filename()
part = aoc.get_part()

with open(filename, 'r') as file:
  text = file.read()


def part_one():
    mul_ops = [str(x) for x in re.findall(r"(mul\(\d{1,3},\d{1,3}\))", text)]
    sum = 0
    for operation in mul_ops:
        multiplicand, multiplier = [int(x) for x in operation.removeprefix('mul(').removesuffix(')').split(',')]
        sum += multiplicand * multiplier
    return sum

def part_two():
    mul_ops = [str(x) for x in re.findall(r"(?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don't\(\))", text)]
    # print(mul_ops)
    sum = 0
    enabled = True
    for operation in mul_ops:
        if operation == 'don\'t()':
            enabled = False
        elif operation == 'do()':
            enabled = True
        elif enabled:
            multiplicand, multiplier = [int(x) for x in operation.removeprefix('mul(').removesuffix(')').split(',')]
            sum += multiplicand * multiplier
    return sum
    

if part.lower() in ['one', 'both']:
    print(f"Part One: {part_one()}")
if part.lower() in ['two', 'both']:
    print(f"Part Two: {part_two()}")  
