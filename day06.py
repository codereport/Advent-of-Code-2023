#!/usr/bin/env python3

from math import prod

# Parsing

f = "data/06.txt"

def ints(s: str):
    return [int(i) for i in s.split()]

def parse():
    temp = [ints(g.split(":")[1]) for g in open(f).readlines()]
    return temp[0], temp[1]

times, dist = parse()

# Part A

def can_win(t, d):
    return sum(i * (t - i) > d for i in range(0, t + 1))

def ways_to_win(times, dist):
    return prod(can_win(t, d) for t, d in zip(times, dist))

# Part B

def flatten_ints(ints):
    return [int("".join(str(i) for i in ints))]

# Print Results

print(ways_to_win(times, dist))
print(ways_to_win(flatten_ints(times), flatten_ints(dist)))
