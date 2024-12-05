from utils import aoc

filename = aoc.get_input_filename()

with open(filename, 'r') as file:
  content = list(map(lambda line: list(map(int, line.strip().split('   '))), file.readlines()))
  left = []
  right = []
  for l, r in content:
    left.append(l)
    right.append(r)

def part_one():
  part_one_left = left.copy()
  part_one_right = right.copy()
  part_one_left.sort()
  part_one_right.sort()

  sum = 0
  for i in range(len(part_one_left)):
    dist = abs(part_one_left[i] - part_one_right[i])
    sum += dist

  return sum

def part_two():
  part_two_left = left.copy()
  part_two_right = right.copy()

  right_dict = {}
  for i in range(len(part_two_right)):
    key = part_two_right[i]
    right_dict[key] = right_dict.get(key, 0) + 1

  similarity = 0

  for value in part_two_left:
    similarity += value * right_dict.get(value, 0)
  
  return similarity


print(f"Part One: {part_one()}")
print(f"Part Two: {part_two()}")
