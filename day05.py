#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor
from functools import reduce
from operator import add

from more_itertools import chunked

# Parsing

f = "data/05.txt"

def ints(s: str):
    return [int(i) for i in s.split()]

def conversion(curr: int, map: list[list[int]]) -> int:
    for dest, source, rng in map:
        if curr >= source and curr < source + rng:
            return dest + (curr - source)
    return curr


def parse():
    temp = [g.split("\n") for g in open(f).read().split("\n\n")]
    seeds = ints(temp[0][0].split(":")[1])
    maps = []
    for conv_map in temp[1:]:
        map = []
        for conv in conv_map[1:]:
            map.append(ints(conv))
        maps.append(map)
    return seeds, maps

[seeds, maps] = parse()

# Part A

def location(seed, maps):
    for map in maps:
        seed = conversion(seed, map)
    return seed

def lowest_loc(seeds, maps):
    return min(location(seed, maps) for seed in seeds)

# Part B

def split_chunk(rng, n):
    [a, b] = rng
    c, res, start = b // n, [], a
    for _ in range(n - 1):
        res.append([start, c])
        start += c
    res.append([start, (a + b - start)])
    return res

def process_chunk(rng):
    return min(location(i, maps) for i in range(rng[0], sum(rng)))

def lowest_loc_rng(seeds: list[int]):
    seed_chunks = reduce(add, (split_chunk(c, 20) for c in chunked(seeds, 2)))
    with ProcessPoolExecutor(max_workers=60) as executor:
        results = list(executor.map(process_chunk, seed_chunks))
    return min(results)


# Print Results

print(lowest_loc(seeds, maps))
print(lowest_loc_rng(seeds, maps))
