# https://adventofcode.com/2024/day/6
# Day 06: Guard Gallivant

def guard_gallivant(data):
    A = {i + 1j * j: val for i, row in enumerate(data.split()) for j, val in enumerate(row)}
    cur = next(z for z in A if A[z] == '^')
    dir = -1

    def vis(cur, dir, ext = -2):
        seen = set()
        while cur in A:
            if (cur, dir) in seen:
                return set()
            seen.add((cur, dir))
            nxt = cur + dir
            if nxt == ext or A.get(nxt, 0) == '#':
                dir *= -1j
            else:
                cur = nxt
        return seen

    B = {z for z, _ in vis(cur, dir)}
    yield len(B)
    yield sum(not vis(cur, dir, z) for z in B if z != cur)


def inputs():

    yield """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

    yield """
.............#........................................................#...#...........................................#...........
.....#...............................#.........................................#...#...............#........##...............#.#..
..................................#..................#.......................................#...#................................
.........................................#................#....#..............................................#................#.#
........#.........................................................#...........#.......#..............................#............
........................#.............................#.......................#.......#.......................#........#.........#
................................#.......#............................................#...........................................#
...........#........#...#..#...........................#..................#.............#.......#..........................#......
............................................#........#.......#..#......#..............................#..#................##......
............#..#...#......#.........................................##.......#..........#.......#...................#.............
.....................................................................................#.....#......................................
.......................................................#................#.....................................#...................
...........#.....#.#....................................#.......#.#...........#................#.......#.................#........
............#.............#....................#....#............................#.........................................#......
.#..........#......#................#........................#............#..#..............#.....................................
..................#....#...........................................#.....#.....#.........................................#.#......
.............#..............#..#...........................#..#..........#...............................#........................
.................................................................................................#................................
.......................................................#..............#..............................................#..#.........
......#............................#.......................#................................................................#.....
..........#.........#..................#....#....#...#......#.........#.................................#........................#
..#...#............................#............#.......###.................................#.............................#...#...
.................#....#...................#........................................................................#..........#...
....#..........................#......................................................................#.....#......#..............
.#........................................................................#..........#............#..................#............
...................##.#.......................#....#.#........................................#.........##........................
#...........................................................#..........#........#.#..................................#............
.......#...#.........................................#.......#........#...............##..#.......................................
......................#....#...............................#......................................................#..#............
......#.....................................................#...............................#......................#..#...........
.........................#.#......................................................................................................
.......................................#...............#...................#................#..........#.#......................#.
.......#......#...#...........................#.........................#...............#..#...............#.............##.......
.....#..#..#..................#............#......................................................#...#.........................#.
#.#...............#...........#................#...................................................#..........#...................
..........................................................................#...............................................#.......
.........#.......#..........................#.##.............................#..##...#.......................................#....
....#...............#..........#........................................#.....#.........................................#.........
...........#................................................#....##...................................................#..#........
........................#........#...........#...#............................................#......................##...........
......#........................................#...#.............................................#................................
#.....#......#..................................#.............#..#...............................#................................
..................#......................#..........#...................#............................................#....#.......
.................#.............................................................................#.......#..........................
......#........................................................................................#...#....................#.........
....#......................#..................##..................#.......#.......................#...........#.........#..#......
............................................................#......##.............................#.#.....#............#..........
..............#.......................#...^.....................................#.....................................#...........
..............#...##......#..#.....#..........................................................................#.......#.........#.
.#................................................................#........##......#....#.......#.................................
....#.....................#........#...........#.............................................#........#................#......#..#
...................#.............#.........#.........................#...........#..................#...................#....#....
.#...............................................#.....#..#...#...................................................................
........................##............#.....................................#........#..................................#.........
..............#................................#.....................................#...................................#........
...........#..........#...........#........#...................#..#..........................#....................................
.#..............................................................#....#.......#.....................................#..............
.....................#........#......#................#.............#........................#.......................#........#...
.........................#..............#...#....#..................#.............................................................
..#............................##.........................................................#...........................#.#..#......
.....#............#...##........#..........#....#......#................................#.................#...............#....#..
.....#...............#.............................#............#......#....#........................................#............
...#..........#.........#.....................##.......#.....#...................#................................................
.................................#...........................................#.................#...........................#......
..........................................................#........................#.......#.................................#...#
..#......#......................................#...#..#....................#...........#....#.............................#......
..#........#.............#......................#...#.....#....#........................#..#......................................
.........#...........#.......................................................................#.........#....#...#.................
..................................#....#.............##....#.......#.........#.........................................#..........
....#.................................................#.......#...........#.......................................##.....#........
..............................#.........................................................#.....#........................#..........
...#........#...........#..#..................................................#..............#.............................#......
................................................#...............................................................#.....#..#.....#..
...............#.........................#..#...................#....................................#................#...........
............................#...........................................................................................#.........
.....#.........................#.......#..#..##.............................#................##.......##............#.............
.........#........................................................................................................................
.........................#............................#........................#.....#..........#.....................#...#..#....
.......#........#..............................#..........................#...#.................#............#....................
#...#..#...............................#..........................................#...#...#.........................#.............
...........................................................#..............#..........#..................#.........................
...........................................................#..............................................................#....#..
...........#.......................#................#......#.....................................#..................#.....#.......
.....#.................................#........................#.#...................#.....#............#........................
...........................#.#............#..............#..............#..#...#..........................#................#......
.........#...................#........................#......#..#..................................................#..............
.............................................#.................................................................#.......#.......#..
#.......................#...............#.......................#...........#................................#....................
......................................#............#....................................................##...................#....
#...............#...........................................#......#....................................#...............#.........
...#...............#.................................#..................................#..#............#.........................
......................#..#............#..#..............................................#......#....#...............#.............
..................#.....................#.....#...................#..#................#....#..........#......#..........#.........
.......................#.....#..............#..........................#............#...................#.#.......................
......#...........#..............#........#........................................#......................................#.......
............#................#..##....................................................................#........................#..
...........#....................................#.............................#.....#....#...#.#......................#...........
...................................................#...............................#....................#.........#...............
........#......#..#................#..................................................................#.................#.........
.............................#................................................#...........#.....#....#............................
........#.............#.........#............#....#.....................#........#...............#................................
..#................................#................................#..#......#.............................................#.....
.........#...........................................#..................................#....#..#.....................#...........
.....................................................#.........................................................#..................
.........#...#.#.....#.......##................................#...#..........................#........#..........................
......................##...............................#..........................................................................
.........#...#.....#........................................#................#........#............#........#.....................
...............#............#.................................................................#................................#..
......#..............#...................................................#............#.....................#.....................
.........#.........#..............................................................................................................
.#........#...............#..##......#..............................#...........#..#.........#...........................#........
...................#................................................................................#...............#.............
..............................................................................#........................#................#.........
...........#.....#..#.#....................................................#......#......#..#................##...................
....#......#...................................................................#..............#.....#.........#..................#
..#...........#...#...........#.......##..........##......................#......................................................#
..................#................................................#.#............................................................
#................................................................#............#...##..........................................#...
......#............................................#.......#.#.................................................#..................
..............................#..............#.#....#............#..........................#.....................................
............................#..................................#.................#..#...........................................#.
.........................................#................#..................#...#............................#..#......#........#
....................#..............................................................#..............................#..........##...
...#......................................#...........#..#............................................#.....#....#................
................#..#....#.........................................................................................................
...................................#...................#...............................#................................#.......#.
..........#.................#.............#..................#...............................................................#....
.....#...........#........#................#.........................................#..........................#......##.........
..........................#................#..............................................................#.......................
........#.................................................................#......................#.#..........................#...
"""

for data in inputs():
    print(*guard_gallivant(data.strip()))
