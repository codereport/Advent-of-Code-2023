#!/usr/bin/env python3

from collections import defaultdict
from itertools import groupby
from math import prod

# Utility functions

def chunk_while(predicate, iterable):
    for k, g in groupby(iterable, key=predicate):
        if k:
            yield list(g)

# Parsing

f = "data/03.txt"

def grid() -> list[str]:
    return [l.strip() for l in open(f).readlines()]

def parse(g: list[str]) -> list[(int, int, int, int)]:
    ints = []
    for i, l in enumerate(g):
        for chunk in chunk_while(lambda x: x[1].isdigit(), enumerate(l)):
            ints.append((int("".join(b for _, b in chunk)), i, chunk[0][0], chunk[-1][0]))
    return ints

g    = grid()
nums = parse(g)

# Part A

def is_symbol(grid, row, col) -> bool:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return False
    return not grid[row][col].isdigit() and grid[row][col] != "."

def symbols_adj_to(grid, num) -> list[(str, int, int)]:
    n, row, a, b = num
    adj_to = set()
    dx = [1, 1, 1,  0, -1, -1, -1,  0]
    dy = [1, 0, -1, 1,  1,  0, -1, -1]
    for col in range(a, b + 1):
        for x, y in zip(dx, dy):
            if is_symbol(grid, row + x, col + y):
                adj_to.add((grid[row + x][col + y], row + x, col + y, n))
    return adj_to

def is_symbol_adjacent(grid, num) -> bool:
    return len(symbols_adj_to(grid, num)) > 0

def part_sum(grid, ints) -> int:
    return sum(i[0] for i in ints if is_symbol_adjacent(grid, i))

# Part B

def gear_sum(grid, ints) -> int:
    star_adj = defaultdict(list)
    for num in ints:
        symbols = symbols_adj_to(grid, num)
        for symbol, x, y, n in symbols:
            if symbol == "*":
                star_adj[x, y].append(n)
    return sum(prod(ns) for ns in star_adj.values() if len(ns) == 2)


# Print Results

print(part_sum(g, nums))
print(gear_sum(g, nums))
