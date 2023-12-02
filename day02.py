#!/usr/bin/env python3

from collections import Counter
from functools import reduce
from math import prod

from more_itertools import chunked

# Utility functions

def remove_all(seq, remove):
    return [e for e in seq if e not in remove]

# Parsing

f = "data/02.txt"

def parse_to_counters() -> list[str]:
    games = []
    for l in open(f).readlines():
        game = []
        for bag in "".join(remove_all(l, ",")).split(":")[1].split(";"):
            c = Counter()
            for [n, color] in chunked(bag.split(), 2):
                c[color] = int(n)
            game.append(c)
        games.append(game)
    return games

counters = parse_to_counters()

# Part A

MAX_COLORS = Counter({"red": 12, "green": 13, "blue": 14})

def id_sum(c: list[Counter]) -> int:
    return sum(id for id, games in enumerate(c, 1) if all(c < MAX_COLORS for c in games))

# Part B

def power_sum(c: list[Counter]) -> int:
    return sum(prod(reduce(lambda a, b: a | b, game).values()) for game in c)

# Print Results

print(id_sum(counters))
print(power_sum(counters))
