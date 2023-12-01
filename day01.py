#!/usr/bin/env python3

# Part A

f = 'data/01.txt'

def num(s: str) -> int:
    n = ''.join(c for c in s if c.isdigit())
    return int(n[0] + n[-1])

print(sum(num(l) for l in open(f).readlines()))

# Part B

def translate(s: str) -> str:
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    conv = ["o1e", "t2o", "t3e",   "f4r",  "f5e",  "s6x", "s7n",   "e8t",   "n9e" ]
    
    for n, c in zip(nums, conv):
        while n in s:
            s = s.replace(n, c)
    return s

print(sum(num(translate(l)) for l in open(f).readlines()))
