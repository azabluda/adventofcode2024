# https://adventofcode.com/2024/day/21
# Day 21: Keypad Conundrum

from time import time
from functools import *
from itertools import *

def solve(data: str):
    R = [{}, {}]
    for i, kbrd in enumerate(['789|456|123| 0A', ' ^A|<v>']):
        kbrd = kbrd.split('|')
        keys = {s: (i, j) for i, r in enumerate(kbrd) for j, s in enumerate(r)}
        for p in product(keys, repeat=2):
            s, d = map(keys.__getitem__, p)
            m = [b - a for a, b in zip(s, d)]
            v, h = (k and t[k // abs(k)] * abs(k) or '' for k, t in zip(m, [' v^', ' ><']))
            vh = (d[0], s[1]) != keys[' ']
            hv = (s[0], d[1]) != keys[' ']
            R[i][p] = [h + v] * hv + [v + h] * vh

    for part in 2, 25:
        @cache
        def dp(s, i):
            if i > part: return len(s)
            return sum(min(dp(r + 'A', i + 1) for r in R[i > 0][p]) for p in pairwise('A' + s))
        print(sum(dp(s, 0) * int(s[:-1]) for s in data.split()))


def inputs():
    yield """
029A
980A
179A
456A
379A
"""
    yield """
319A
985A
340A
489A
964A
"""


start = time()
for data in inputs():
    solve(data.strip())
    print()
print(f"Elapsed time: {time() - start:.2f} seconds")
