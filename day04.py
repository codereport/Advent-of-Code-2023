#!/usr/bin/env python3

# Parsing

f = "data/04.txt"

def nums(xs):
    [a, b] = xs
    return (set(a.split()), set(b.split()))

def parse():
    return [nums(l.strip().split(":")[1].split("|")) for l in open(f).readlines()]

cards = parse()

# Part A

def points(n) -> int:
    if n == 0: return 0
    return 2 ** (n - 1)

def total_points(c):
    return sum(points(len(a & b)) for a, b in c)

# Part B

def points_per_card(c):
    return list(len(a & b) for a, b in c)

def total_scratch_cards(c):
    ppc = points_per_card(c)
    cards = [1] * len(ppc)
    for i, p in enumerate(ppc):
        for j in range(i + 1, i + 1 + p):
            if j >= len(ppc): break
            cards[j] += cards[i]
    return sum(cards)

# Print Results

print(total_points(cards))
print(total_scratch_cards(cards))
