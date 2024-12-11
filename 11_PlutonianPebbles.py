# https://adventofcode.com/2024/day/11
# Day 11: Plutonian Pebbles

from collections import *

def plutonian_pebbles(data):
    A = Counter(map(int, data.split()))
    for i in range(75):
        A, B = Counter(), A
        for x, n in B.items():
            if x == 0:
                A[1] += n
                continue
            s = str(x)
            q, r = divmod(len(s), 2)
            if r:
                A[x * 2024] += n
                continue
            A[int(s[:q])] += n
            A[int(s[q:])] += n
        if i == 24:
            yield A.total()
    yield A.total()


def inputs():

    yield """
125 17
"""

    yield """
8069 87014 98 809367 525 0 9494914 5
"""

for data in inputs():
    print(*plutonian_pebbles(data.strip()))
