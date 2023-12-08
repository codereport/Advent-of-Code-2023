#!/usr/bin/env python3

from collections import Counter
from enum import IntEnum

# Parsing

f = "data/07.txt"

def parse():
    return [(l.split()[0],int(l.split()[1])) for l in open(f).readlines()]

hands = parse()

# Part A

class Hand(IntEnum):
    FIVE  = 7
    FOUR  = 6
    FULL  = 5
    THREE = 4
    TWO   = 3
    ONE   = 2
    HIGH  = 1

def common_hand_logic(c):
    v = sorted(c.values())
    if 5 in v:       return Hand.FIVE
    if 4 in v:       return Hand.FOUR
    if [2,3] == v:   return Hand.FULL
    if 3 in v:       return Hand.THREE
    if [1,2,2] == v: return Hand.TWO
    if 2 in v:       return Hand.ONE
    return Hand.HIGH

def hand(h):
    c = Counter(h)
    return common_hand_logic(c)

def card_to_num(c):
    if c in "TJQKA": return 10 + "TJQKA".index(c)
    return int(c)

def numeric_hand(h):
    return [card_to_num(c) for c in h]

def total_winnings(hands):
    return sum(b * i for i, (_, _, b) in
               enumerate(sorted([(hand(h), numeric_hand(h), bid)
                                 for h, bid in hands]), 1))

# Part B

def joker_hand(h):
    c  = Counter(h)
    js = c["J"]
    c.pop("J")
    key     = max(c, key=c.get) if c else "J"
    c[key] += js
    return common_hand_logic(c)

def joker_card_to_num(c):
    if c == "J": return 1
    if c in "T_QKA": return 10 + "T_QKA".index(c)
    return int(c)

def joker_numeric_hand(h):
    return [joker_card_to_num(c) for c in h]

def joker_total_winnings(hands):
    return sum(b * i for i, (_, _, b) in
               enumerate(sorted([(hand(h), numeric_hand(h), bid) if "J" not in h else
                                 (joker_hand(h), joker_numeric_hand(h), bid)
                                 for h, bid in hands]), 1))

# Print Results

print(total_winnings(hands))
print(joker_total_winnings(hands))
