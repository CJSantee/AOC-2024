from collections import defaultdict
from utils import aoc

filename = aoc.get_input_filename()

part = aoc.get_part()

with open(filename, 'r') as file:
    rules, updates = file.read().split('\n\n')
    rules = sorted([tuple(int(num) for num in rule.split('|')) for rule in rules.split('\n')])
    updates = [[int(page) for page in update.split(',')] for update in updates.split('\n')]

def valid_update(update: list[int]):
    cannot_appear = []
    for page in reversed(update):
        if page in cannot_appear:
            return False
        for rule in rules:
            before, after = rule
            if before > page:
                break
            if page == before:
                cannot_appear.append(after)
    return True

def get_relevant_rules(update: list[int]):
    relevant_rules: list[tuple[int, int]] = []
    for page in update:
        for rule in rules:
            before, after = rule
            if before == page and after in update:
                relevant_rules.append(rule)
            if before > page:
                break
    return relevant_rules

def fix_update(update: list[int]):
    new_update = update.copy()
    # Build the page_rules dict
    relevant_rules = get_relevant_rules(update)
    page_rules = defaultdict(list)
    for rule in relevant_rules:
        before, after = rule
        page_rules[before].append(after)
    # Swap elements to the correct position
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            left = new_update[i]
            right = new_update[j]
            if left in page_rules[right]:
                new_update[i], new_update[j] = new_update[j], new_update[i]
    
    return new_update

def part_one():
    sum = 0
    for update in updates:
        if valid_update(update):
            mid = update[len(update) // 2]
            sum += mid
    return sum

def part_two():
    sum = 0
    for update in updates:
        if not valid_update(update):
            update = fix_update(update)
            mid = update[len(update) // 2]
            sum += mid
    return sum

if part.lower() in ['one', 'both']:
    print(f"Part One: {part_one()}")
if part.lower() in ['two', 'both']:
    print(f"Part Two: {part_two()}")
