# https://adventofcode.com/2024/day/17
# Day 17: Chronospatial Computer

from re import *

def solve(data):
    A, B, C, *D = map(int, findall(r'\d+', data))

    part1 = []
    p = 0
    while p < len(D):
        op, lt = D[p:p+2]
        cb = [A, B, C][lt - 4] if lt > 3 else lt
        if op == 0: A = A >> cb
        if op == 1: B ^= lt
        if op == 2: B = cb % 8
        if op == 3: p = lt - 2 if A else p
        if op == 4: B ^= C
        if op == 5: part1 += cb % 8,
        if op == 6: B = A >> cb
        if op == 7: C = A >> cb
        p += 2
    yield ','.join(map(str, part1))

    def part2(A, i):
        if i == len(D):
            return A
        for a in range(8):
            a += 8 * A
            b = a % 8
            b = b ^ 5
            c = a >> b
            b = b ^ 6
            b = b ^ c
            if b % 8 == D[~i]:
                found = part2(a, i + 1)
                if found:
                    return found
    yield part2(0, 0)


def inputs():

    yield """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

    yield """
Register A: 24847151
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0
"""


from time import time
start = time()
for data in inputs():
    print(*solve(data.strip()))
print(f"Elapsed time: {time() - start:.2f} seconds")
