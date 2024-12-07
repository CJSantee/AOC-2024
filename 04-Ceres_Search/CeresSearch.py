from utils import aoc

filename = aoc.get_input_filename()

part = aoc.get_part()

with open(filename, 'r') as file:
    graph = [list(line.strip()) for line in file.readlines()]

NORTH = (-1, 0)
NORTH_EAST = (-1, 1)
EAST = (0, 1)
SOUTH_EAST = (1, 1)
SOUTH = (1, 0)
SOUTH_WEST = (1, -1)
WEST = (0, -1)
NORTH_WEST = (-1, -1)
DIRECTIONS: list[tuple[int, int]] = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]
XMAS = list('XMAS')

# Check if a point is on the graph
def on_graph(point: tuple[int, int]):
    row, col = point
    if row < 0 or row >= len(graph):
        return False
    if col < 0 or col >= len(graph[0]):
        return False
    return True

# Count the number of times xmax can be spelled starting for a particular point
def count_xmas(point: tuple[int, int]):
    count = 0
    origin_row, origin_col = point
    for direction in DIRECTIONS:
        found = True
        for char_i in range(len(XMAS)):
            row_offset, col_offset = direction
            row = origin_row + (row_offset * char_i)
            col = origin_col + (col_offset * char_i)
            if not on_graph((row, col)):
                found = False
                break
            test_char = graph[row][col]
            x_char = XMAS[char_i]
            if test_char != x_char:
                found = False
                break
        if found:
            count += 1
    return count

# Check if point is the A in an X-MAS
def is_x_mas(point: tuple[int, int]):
    count = 0
    origin_row, origin_col = point

    # Check North-West
    row = origin_row + NORTH_WEST[0]
    col = origin_col + NORTH_WEST[1]
    test_char = graph[row][col]

    return count

def part_one():
    count = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            test_char = graph[row][col]
            if test_char == 'X':
                count += count_xmas((row, col))
    return count

def part_two():
    count = 0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            test_char = graph[row][col]
            if test_char == 'A':
                count += count_x_mas((row, col))
    return count

if part.lower() in ['one', 'both']:
    print(f"Part One: {part_one()}")
if part.lower() in ['two', 'both']:
    print(f"Part Two: {part_two()}")  
