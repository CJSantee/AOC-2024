from collections import defaultdict
import copy
from utils import aoc

filename = aoc.get_input_filename()

part = aoc.get_part()

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

with open(filename, 'r') as file:
    file_graph = [list(line.strip()) for line in file.readlines()]

def on_graph(point: tuple[int, int], graph: list[list[str]]):
    row, col = point
    if row < 0 or row >= len(graph):
        return False
    if col < 0 or col >= len(graph[0]):
        return False
    return True

def get_guard_position(graph: list[list[str]]):
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            char = graph[row][col]
            if char == '^':
                return (row, col)

def get_char(point: tuple[int, int], graph: list[list[str]]):
    row, col = point
    return graph[row][col]

def get_corner(positions: list[tuple[int, int]]):
    rows = defaultdict(int)
    cols = defaultdict(int)
    for position in positions:
        row, col = position
        rows[row] += 1
        cols[col] += 1

    for key, value in rows.items():
        if value == 1:
            row = key
    for key, value in cols.items():
        if value == 1:
            col = key
    
    return (row, col)

def offset(position: tuple[int, int], offset: tuple[int, int]):
    return tuple(map(sum, zip(position, offset)))

def is_loop(graph: list[list[str]]):
    corners = set()
    dir_idx = 0
    previous_position = None
    guard_position = get_guard_position(graph)
    while on_graph(guard_position, graph):
        next_position = offset(guard_position, DIRECTIONS[dir_idx % len(DIRECTIONS)])
        if on_graph(next_position, graph):
            char = get_char(next_position, graph)
            if char == '#':
                if guard_position in corners and previous_position != guard_position:
                    return True
                corners.add(guard_position)
                dir_idx += 1
                previous_position = guard_position
            else:
                previous_position = guard_position
                guard_position = next_position
        else:
            break
    return False

def part_one():
    positions = set()
    dir_idx = 0
    guard_position = get_guard_position(file_graph)
    while on_graph(guard_position, file_graph):
        positions.add(guard_position)
        next_position = offset(guard_position, DIRECTIONS[dir_idx % len(DIRECTIONS)])
        if on_graph(next_position, file_graph):
            char = get_char(next_position, file_graph)
            if char == '#':
                dir_idx += 1
            else:
                guard_position = next_position
        else:
            break
    return len(positions)

def part_two():
    num_loops = 0

    positions = set()
    dir_idx = 0
    guard_position = get_guard_position(file_graph)
    while on_graph(guard_position, file_graph):
        positions.add(guard_position)
        next_position = offset(guard_position, DIRECTIONS[dir_idx % len(DIRECTIONS)])
        if on_graph(next_position, file_graph):
            char = get_char(next_position, file_graph)
            if char == '#':
                dir_idx += 1
            else:
                guard_position = next_position
        else:
            break
    
    guard_position = get_guard_position(file_graph)
    positions.remove(guard_position)
    for position in positions:
        new_graph = copy.deepcopy(file_graph)
        new_graph[position[0]][position[1]] = '#'
        if is_loop(new_graph):
            num_loops += 1

    return num_loops


    # found_corners = []
    # loops: list[list[tuple[int, int]]] = []
    # corners: list[tuple[int, int]] = []

    # dir_idx = 0
    # guard_position = get_guard_position()
    # while on_graph(guard_position):
    #     if guard_position in corners:
    #         found_corners.append(guard_position)
    #         corners.remove(guard_position)
    #     next_position = offset(guard_position, DIRECTIONS[dir_idx % len(DIRECTIONS)])
    #     if on_graph(next_position):
    #         char = get_char(next_position)
    #         if char == '#':
    #             print('turning')
    #             print(f'loops: {loops}')
    #             corners = []
    #             for loop in loops:
    #                 if len(loop) < 3:
    #                     loop.append(guard_position)
    #                     if len(loop) == 3:
    #                         corner = get_corner(loop)
    #                         loop.append(corner)
    #                         print(f'loop: {loop}')
    #                         corners.append(corner)
    #                         print(f'corners: {corners}')
    #             loops.append([guard_position])
    #             dir_idx += 1
    #         else:
    #             guard_position = next_position
    #     else:
    #         break

    # print(positions)

    # count = 0
    # for corner in corners:
    #     if corner in positions:
    #         print(f'corner: {corner}')
    #         count += 1

    # print(corners)

    # print(found_corners)
    # return len(found_corners)

if part.lower() in ['one', 'both']:
    print(f"Part One: {part_one()}")
if part.lower() in ['two', 'both']:
    print(f"Part Two: {part_two()}")
