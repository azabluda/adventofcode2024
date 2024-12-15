# https://adventofcode.com/2024/day/15
# Day 15: Warehouse Woes

def solve_puzzle(data):
    A, B = data.split('\n\n')
    boxes = set()
    walls = set()
    for i, r in enumerate(A.split()):
        for j, v in enumerate(r):
            z = i + 1j * j
            if v == 'O': boxes.add(z)
            if v == '#': walls.add(z)
            if v == '@': robot = z
    for move in B.replace('\n', ''):
        move = 1j ** 'v>^<'.find(move)
        box = 0
        z = robot + move
        while z in boxes:
            box = box or z
            z += move
        if z not in walls:
            if box:
                boxes.remove(box)
                boxes.add(z)
            robot += move
    yield int(sum(100 * z.real + z.imag for z in boxes))


def inputs():

    yield """
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

    yield """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

    yield """
##################################################
#...O.O#....O.O.O.#.O....O.#O.O.O.O.......O#O...O#
#OO......OOO........#...OO#O..OOO.OO..O....##....#
#O........O..O#....O.O.....O...#...O.O.O.......O##
#OO.OOOOO..OO..##.....O..........#...#OO.#O.OO.O.#
#.O#.....O..OOO......OOO...#..OO..#OOO.O.#......##
#..OO......#O..#O#O.O.......O..OO#...#O....O....O#
#..#.#OOO..OO#..OOOO..#....O.OO.#.O..OO..O.O..O..#
##....#..O...O...O.#.OO......#O.O..#..O.........O#
#.........#.O.#...........O.....O..OO..O......O.O#
#..OOOO..OO.#OO#..O..#.O.O#...O...#O..O...#.O.O#.#
#..O....#O#.O........O..#OO.OO....O..O#.O#...#...#
##.O..#..O.##O.O#OOO.O#..OO...............O#O#OO.#
#OOO...O...O...O......O..O..O..O..........#...O..#
#OO..##.OO.O..#..O.O......O....O..O..O.O..O.#..O.#
#...O.#.O.#O.#O#.O.#.O..O#O.O......O.........O...#
#..#.O.O.....O.#O.O.........O.OO#.O......#..O..O.#
#....O..O..#...OO#.O..#.....#......OO..O.OO.....O#
#...........OO.....O...O.O........O#.#...O......##
#...#..OO.OO....OO.#..#...O..OO.O......OO.#...O..#
#..O...O..OOO.OOO.O.......O.....OO.#...OOO..O...O#
#...O.O..#...O...#.O#...O.#...O....OOO.O...OO....#
#O.....O...O...O..##.O..#..O...O.....OOO##.O.....#
#..#...OO..OO.#....#..#OOOO.OOO....O..O.....O....#
#...O..OO...OO.O........@O....OO..O.O..O.........#
#...O....##O........O..O.#O..O......O....O....O.O#
#.....#...OO....OOOO.O.#O..O......O...#.O........#
#OO##....#..#O..O.OO#............O..#OOO....O.O.O#
#.O..O.....OO...#OO#OO#.#.OO.......#.O#.O.O..O.O.#
#.O....O.#O#..#.....O.....O....O.O......OO.O#..O##
#.OO.O.O....O.O..O#.O.OO.O.O........#.#..O...#..##
#.O##.#.OOO..O.##......OO...O#.OO..OOOO.........O#
#....O.O......O#..OO........O.O......O...OO.O...O#
##O.....O..#O.O..O#.O.O..OO.#....OO.O....OO..#..O#
#.O...OOOO.#.#.#.OO..O..#.O..OO....OO.......OOO..#
#O.O.O.OO..OO.O.O..O..#.....OO...O.O.O...O..O....#
#O..OO..O#O.....OOOOO.#...O#....O#....O.O#.O.O.O.#
#.O...#O#O.O..O........O#O......O...O..#...#...#.#
#.O....OO...O.O..O...O...#.........OOO#..O.O...O.#
#..O...O.O..OO........O....O............O.##...O.#
#O......O...O....O...O.#.....O.........O......OOO#
#O.O.#...OO....##..#...OO.#.........O..OO..OO#...#
#......O.OO..O..OOO.#O....#O.OO.O.......O....OO..#
##...O....O#.O..O.O....#..........OO.O...#OO..O.O#
#....##OO.O..O#.#...#..O...OOO..O..........OO....#
#.......O...........#OO..O#........O..OO....OO..O#
#O.....O..OOOO.O.........O#....OO...O.#.O.#....OO#
#....O.###...#.#OOO....OO.O......O...##.....#....#
#.OO.OO............#.OOO..OO.#OO......O..O..O.O..#
##################################################

v^^^>^<><v<^<<^<v<>vv<<v<<v><^^<vv<>^<<<>v<>><>^>>^>v>>>>><vv><<v>>^<v^<^^vv><><^>>^^^>v<>><v^vv>>v>v^<v^>>^>^<v<vv^<v<>><>>^<<^><^v>><<>v<vvvv><v^<<>>>v<v^>^^><^^v^><v>^>><<^<<^v><^>^^v^><>>^v<<><<>>>><v^><v<>>v<<<>v><>v<>><><^<^>^>v>vv<<v^^>v^v^^>^>^><<vvvv>>^^>^^<>^v<v><vv>><><<v<<v<>>>>vv><>vv>v^<><<^>>>v^>vv<^<<>>>><^vv>vv^>^><^v>v>>v><^>^<^^<^vv><>>^<vv><>v^<^><<^vvv^<^<vvv<v^>^v>v>v>>^^<><><^><v^>><>vv^v><v><>^>><v>v<^vv><<<vv<<^vvv<^v^^^<v>^^<vv>v>v^^^^><vv>>v^v>v>><^<>v>^>^v<v<v^v>v^<<^v^^^>v<^^v<>^^<^<vvv^v^v<<^v<^v>v^v<^v^vvv^^<v>vv<^<<>v<>>>v<>^^^<>v<^^^<<^<<>^^<>>vv^<<vvv^^^<^^<vv^>v<>vv<v^><<<^><v<v^>>v><<<vv<^^>vv>^><<>v^>v<^vv>^v>v^v^v^v<>>v^><<^><<><>>v<>><<^^<>>^><>^<v>v>^><v^<>^>^v^<<<^^<<^v<>>v^v^v<>>>^>v^<>v<^<^>v><>><v^>>v<>>v>v<^v>^<><<<^^^vv<<<<<>v>^>v>><vv^>v><><<>v<<v<>v^v<>vvvv><><vv<^<^^>^v<>vv^^>v^>v<^<v^vvv^<^v<v<v^v>>vvv<^v>vv^><><v<<v<<<><^vvv^vv>v><^<v><vvvv>^>^>^>^<^^v^v^>^vv<<vv>><>>>>^^^^^<>^><v<>v<>>^<>^^>>^^^<^^v^<>vv>>^^<^<vvv<<<^<^<>v<v><v><^vv><
v^v<^<<<>>^<vv>^^<^^<<^<>><vv>^v>v^v<>^^><<vvv><<^<<<^<<>^^vvv<v^>^<^>>>>vv<^vv^vv<^<^v^<^^<><^^<><<>>^>>^vvvv>^<<<^v^<>vv>vv<^>vv^><^vv^<v^v>v^^^<<v<v^^>v<v>^^v<^>^^<vvv>v><<vvvv<<><>><<v>^^v<^>^^v>>^<^vv<v>><>v^^>^>^v<<><><vv^><<^>v>^<^<>vvvv^<v<>>vv^>^>^<v<<>^>^<^v>v<^^vvv^^>v^<v<^<v<v<>v>>^vv><<v<><<v><<^^vv^^<<>>>^^<v>>^^^>^^><^v<>vv<<<>^<^v<vv><<v<>v<>><<^>><<<>>v<^^<>vv<v^^v>^>v>v^vv^>^^^v<<<v^v<<<vvv^^vvv^v>^><><^><>^v^<^>>^<^<vv^<>^^<><><>v>v>>vv><v^^<v<<><^^v>v>v>^^<<^<<>>><<vvv<v><v<v<^<^<<^vv<^^<<<^v^^^>v>^>^v<>v^<><>vv<>^v>^^<<<^>v^v<<<>^>^v^^>^v^<>^<>v^v><>v<<v^^>><^v<vvvv<>^<v<><^vv>v>>>v>>v^^vv>>v>>^v>><>><>v><v<v>^v<^<v^>v<^<^<<>vv^^^>^<>>vv>><>vv>v^<^^<^v^v^>>^v<>v^^^v^><^<v<<<>v<><<<<vvvvv<v>v<<v<v<>>^^><<vv^><<^v<<^^vv^>>><v><<v<v>>><^>v>v<>^v<<v^v<>>^^>>>>v^><<vvv>>v><^vvv<vv^<<<^<><><v>v^v^>^v^<>v<^v><v>v<<v<vv^^>>^v^>^v>>^<<>^<^v^v<^<v^v^^^^^<>v<><^<^>>>v<<^<><>>>v<><>>^^^^<<>^><>^<><>vv^>>^^v^v^>>vv>^^<<>^<>^><<v<^vv^>v><>^^>^v^^<<><v>v^^^^>^>vv^>^^^^^<<^<^v<>vv
^^<<^^<^vv><><><^vv^^v^v<v><>^^<^v<^v<^v<^v^^>vv>>^^>><<^>vv^>^v^>v^v^<>><v^^v><><<v>v>^v^v<>^v<<v<>^^<vv>^>>^>>vv<^<v^^<v>v><<^<v^vv<v>>^<<>>>v<>v^^<<v<^v>vvv>>v<^^<v^>^v<v><>v^<vv>>^>>v<v^><>v^<^<><>vv<v>><^vv^vvv<v<>>v^>^>>vv<>^>>^<<v^>^>v>>v><v^<v<^^<v<v^><<^><>^<v>>><>>^<<^<><<<^v^^<>>^^>^<<^<<>vv<^v^vv>><><<<v<^>vv>^<^^<><^><<^<><<>^v^^<<v>^>v<^>v^^><^v^v<^<>^^<>>>>v^>v^v^<^^>><^<>v>^^^><^^<<vv^^<<>vv<v>v><vv<<^>>>^<<>>^v>>>><>^<^^<^>v<^^^<<vv^<v^v<<>><><^v><v^<v<v>^v><<vv^vv<vv^v>v>vv^><v>^v^^vv^v><v^<<<^^^>vvv<>v^v>>^vv<v>vv>^vvvvvv<>>v><><>v^<<>>>^<<<<vv<v<<<v<vvv<^^^vv<v>><^vvv^<<^>^>>>><v<v<v<><^vv<<^>^^^>v^>v^<<^^^>^<>^^vv><><<v^^<<^v^>>^>^>^><<^^^v^<<>^vvv^v>vv^>v^^<<vvv>^><>>>>^^<^v><<>vv<^v<v^<><>v<><v>>^<<v<v<<><v<^<>v<>><^v>^>^v>^^>^vvv^^^vvv<^<v>>v>^^^vv>vv><<^>v<<v<>>>vv<<>><><^v>><<<<<v^v><v^^<^v<<<vv<^^^>>>^v<<^>vv^^v<<^^^^>^v^>v>vv<>>>^<^<^^^v^^^>^vv><<^<<v>v<><<^v>><>>^^^>>v><v^><v^vv^<v<<v^^>v>>^<<<<^<v>^>^v>>^v<<><<<<>>v^>><vv><^^>>^v^^>^^>^><^^>^v<^v<^v>^v<^<>
<v<vv>>^>^<^>v<v><vvv>^v^^>^^v>vv<>^vv>v>^^<<<^^>^>>>^v>>^^><><v>><v<<><^>vv^<^<>v><>>^>^><v^>v>^>v^^<^^^v^^>v<<v^v><<v>vvv<><><v^<v>>^v><><v>>v<>^<>><>>v<^^<<<v>^><<v^>>>^^<>>v>>v<^<<v^<><>^<v>><v<v^<v>v>>v<^<v<^v^^<>>^<v><vv^<<^><<<>v^>^^^^<^v<v^v^>>v>><v^<><>^<>>vv>>>^^vv>v^>>vv>vv^<vvv>>v<vvvv><>^>v^^v<^>vvvv<v>>vv^<>>v^^v><vv<<^v<><^<vv>^>>>^^<<<v^^vv^<<>>^^^^>><^<<^^v<<>v<vv^<^<><>><<<><^>^^v>>><<v<v^<^v>>^^v>^vv<>^vv^>^>v>^>^>^^><>^v<<v><>v^^>vvv<^v^<^^>>^^><<v^v>><>><v>><<^v^^<<v>^v>v<<v<>><<>v<<vv>>>>><v>^^<^>v<^v^<<^v>>^<v^><>><^^^>>>^v>vv<^vv<^><^<>v^^v^v<><<>^^>^v^^<<<^<v>^v>^<<><v<<v>><<><vv^^^v^v>^<>^<^>^<^>^<><vv><^^^<v>v>vv^>v<^^v<<<^<<vvv><<^>v^v^<<>v^>^v<vv<^<v>v<<v^<<<>v>^>^<>vvv<><>^<>^<^v<<^>vv>>>v><v>^^vv>^v^>v^v^^^>^^v^>v^<>>v^>v^<v>v>^>>vvv<^v>>vvv<v^<^^vv>><^>^><vvv^<<<^v>v<>v^<^v>>^><vv^vv>^<><><><>^^v^^^>><^>v<<vv><><v<<vv<>v^v^^><<^^^v<v^v^>><><<>>v<^v<<<v><<<^^><>>><v<<>v<v>>>v>v^^>v^v^>>v<><>v^>^^<>>v<v>>v><<<>vv<<><^><>^^>>^^^<>v>><>^>^^>>v><v<<^v>^<v<<<<
<<^v<<^>^v<v><<v>v<<<>v^>v>^>v<^^<vvv^^>>v><v<>^v>>^^<<<<>v^v^v>>>^^vv^^^>v><<>><^^>v>v^^<^vv^^vv<^v^>><^<v^<v^<<<>v^^<v^vvv<^<^<^v>^>>>v>v>>v>v<<<><<>><>>v^<v>^><>^v<>>^v>><<vv^>>v<vv<^<^^^<<<<<v>^v<>^<v>>vvv>>v<<<<<<<vv>v>^>>>^<^>v>><v^^<^><^^v><>>^<><vvv<^^^v><<^>^><^<<<<v<<>v^>v<>^<^<>^^<>>><<vv<vv><^<vvvvvv<^^<^v^<^vv<<>>>>v<v^><^v<<vv^<>>v^vv<v>>v>>^>vv^<<^^>v>>^v>^>v^^<v^><v<^vv^>><<>^^>>^v^v^vv^^<v>><<<<^>>v<<v>^v^>^>><v><<<<<^><v<<<v^<^><><v<v>><v^>>>v<<><^>>><vv>v>>v<v<>v>^^v^>>^v^v<^<v>>v<<<><<>>>vv^v>^^^v<>>>^v^v<<<^>^>vv^<^>><^^<v<<^^vvv^<<v^><<>v>^v^><><^>^^<><>><>^><>^>>>v^>>>^^^^v<v<>v><vv<^<<>>><>vv^<>v><v<<v^<v<>^<v<>v^>>>>v><^>^<>>>v>>^v^<^v>^<<<v><>><>>^^v><>>^v<^>^^>^^>><^<^^v<v^<^v><^<<^<><<>v^>v^<>^<<vvv^^<>vv><v><<><^<^v><vv><<<><>v^v<vv>>>^v^<<>>>v^<<>>v>v^>><^<>^><^^^>>^<^^<>^v^^>>vvvv<^<<^^^v><v^v^vv<^^>>>>v^v>>>vv^<v><v><v>>^^^<<<<<v<^v<>v>^<>^>^><>v^<<v<v<>v^<vvvv<<v^vv^<^^^^>>^v<^v<>>>v<^<>>^^v<^^vv^<v^>v^v^^v<^<<^>^v^><v^>v<v<^<v<<v<v<vvv^vv^^v<>vvvv^<v<>
v<<<>v>v><v^v<v<<^v><<<vv^<^^>>^^><vv<>><<v<^<v>vv>v<<^^<v^vv>v><vvv^<^>^v<>><^><^v^<><>vv><<vv>>^^v<vvv^>v<>^<v<<<<^>^>vv^>^>><^v^v>>>vvv<<>><v><v^>^v^^>><v<^<v<^^<<>^^^<>^>v>^^>>^<<^^>^>v>^<><v>^><^<<v><^^>v^vv^v>v^vvvv^><^^<v>>v>^v<><<<v><v^<><^>>^^v^v>>^^vv<>>><v<^<><>^<^<>^^^vv>^v<>^><>>^>vv>>><v>>v^^>^^<<^^<>>><^<v^vv<^^^><>>>^<^>^>>>v<^v>>>^^<<v<>^>^<<v<><>^>vv><<^^>v>>v>v^^<>^><>>^^>v>^^<<^>><vv><<^^><^>v>^vv>^>vv^<v<<<^<>>><>>^vvv^^^>vvv^^v<<<^^v>^v^<<v>><<^><v>v><>v^vv>v>vv>>^<^><^^>^>vvv<vv<>^>^>>v><vv>><v^v^>>>>^>>><v<v><<^>v^v^vv^>><^^>v>^>^v<v><>v<>v>^^<>v<v>^>v<>>^vv><>^^v<v^>vvv>^^^vvv>v>>^>^<<^<v^<vvv><^<^><^>vv>vvv<<vv^<vv>>v>v^>v>^<^v<v^<<vv^>v>>^>v>>^<<v>^>v>^^>>^^^>v<v^^<>>><><^<^<^^vvv<<vv>^^^<>v^<^vv>v^v<v^<^>^><^^^^<<<<<^^<<>^>vv^v>vv<^<>^>><<^>^v<<^<>v<vvv^^><v^<^>v^^v<<vvv><v<^<^<^>^^><v><v<^vvv<<^<>v>v^^^<>v<<>><^<><><^><v>>><v><v<>><^>v^><<v>>v>>^v<v>v>v^>><vv>>^<>>v<v<<v^<vvv^<<<v>v>v>>><><>>^^>v^<<>v>v^^>^<v^v>v^v<>^>v<^<v^<>v<v><><<<<>v^>vvvvv>^^^>v<<^>^^
>>^<<<>vv<>vv^vv<^v>v^v>><vv^><<^^>vv^<vv^v^v<>>^^v<>>^v<>^v^<^v<v<>v^<>vvv>>^>>^^v<>>><v>^^<^<^v>^>v>vv<^^^^<<><v^^^^vv^^>>^^^<vv>^^<<>v^^^v<^>vv><^><^<><<^^>><<<^^^<<v<<^<^>vv>>v>><>^>><vv><<^<vv^^>^^>^<v>>v^^>^v<>vv>>^>^v>v<><v<<<v<<v<<v<v<>v^>>^>^vv><>v>v>v<v^^<v><v^^^>>^<<v>^<v^>^<<>v<^v^<^>^v^^^<^vv<<vv^<<^>^<><>^<v<^^^>vv^><>vv^^>><<^v<vv>v><<^>v^^v>^^^^^>^<<v^^^v<<^v<>^vv^v^<><>^>^v^v<^v^><>^<<v<>^>v<^>>>^v<vv^><>vvv>v^<^><<^^<^^><v^<>v^><>v><^>v<^v<v^>v><<^<v>>v<<^<>^v^v<v^^<<v^<v<><>>v>^<^^>v>>>^>v<v>v<^v<>>><^>^^>v<>v><v>^v<v<><v^>^^vv><<><^<^>vv><^v^><<v<^v^^^>^>^<^>vv>><vv^v^^^vv<^vv<><v><><<>^^vv<<><><<^v><<>v^v<^^><^^>v><v><vv>>^<<>vv^v>v>^v>>>^<v>>v<^^^>^^>^^<vv<^v^^>>v<^^v><<<^^>v^>^^>^^>v<>^><><^^^v>^>^>>^<>>^^<v<>v<<v<v^<v>v>v>^<v<^^>><<<^<<^v<^^vv<>>>vv^^>^v^^<<^v>v<^^>^v^^<>>^<<<<>^><^v<>>^^>^v^>><<><v^vv^^<v^>^^<v>><>v<<><v><v>^>vv^><v<<vv<>v<>>vvv<<<<<>><v^<<<^^<<v<><v>><v^^<<v^^>>v^^<><<v^<><vv<v>^^^<<<v^<<>>^^<^<>>>^v<^^>^v^>>vv^<v<<>vv>^^<<>^<^<<v<<><v<>v^^>^<
^<<v>>>^>>^<v<^>^>v^v>v^>>^^^v<v>>^v<v^^v^^vv>^>^^<><<<vv<<^<^^><>>^^<vv<^v>>^<<^^vv<v<<^v^^>v>>vv^v<<v^v<^v>^>v<<>v^<^v>^><>^^><^<v<<^^^<v<>^v>>v<<^vv<<><v<>v<>>^^^v^v^v><><^^<vv>v<<v>v^<^>^>^vvvv^^><>>><><<vv^^>^>v^<v<^v^<^<>^v>^v>^^>^>vv<vv^>><<^vvv<>>v<v<^v^<^>>v^^^<<^>>^><^>^v<v>^><<><^^v^^v<v^v><^<^>>^v^^v^v^><v<v>^><><<<><<<<v^v>^v><^<>v^vv<>>vv<<>>><<<<<v>^v<>^<^<^><^<^>^><^^v<v<v<^>^>v<vv^^v>><^v<<vvvv^v^><vv^<v^><^>^><^><^^vv<^v<<<^v^<><^^>^vv>^<v>v^^v^v<>><^><<<^^v^^>v<vv^vv><>vv>v>v^vv>^^<<v><^<v^><>><<^^<>>v>>^>v><<<<^^vv^<>^^>v>vv>v>v^>vvv><v^><<^vvv^^>v<<^>>^^<v>><><^^><v<>v<^><v>v^>vv^<^^<<<^>^^^>>v<>vvv^v<v<^v<v>^><vv^<v^vvv>vv<>^v<>>>>^>^<<<>>^^^>>><^<vvv<><vv^vv>v><^<>^v>v^^<<<^^^^v>^>>^vv^<vv^^^<v<v<^>v>>^>v>>>>>>^v<vv^<<>v<<<>>vv<v<>^^<vv^<^^<>>>v>vv>v^^<^vv>>vv>v<<>v<>^v<<v>vv<<>>v>>^<<>^^^<v<>>v<><^>^<<<<>>v<<>>^^>v>^>>^v<v>^>^>v<^<<<v><<<^vv<<<<v<<<>v^^<<>>v<^>^^>>^v<<<^><v^^>>^v>^^>v^>^<^v>>v<<<v<^^<>>^>>v><^>v<v>^>^^v^v>v<><^vv<<<^<>><v<v^^^vv^vv>><<>v>^<^<>v^
v<<^<>^>><>vv^^v^>>>>vvvv<<<^><v>v>vv^><<^<<^<v^v>>>>^>>^^vv<<v^^^>^v^<v>>^<v<v<^^>v<^<^^vvv>^^<<<<^><^vv^<v^<vv<vv^>^^^v<<>>>vvv^^<><<><v>^>v><>v^^<>^>>vvv><<<<v>vv<<^>>>^vv<v><<v>>>><<<<^vv<^vv<><v^^^^>>v^^<>^v<^^<<v^v>>^<<><><vvv<><>v^>>^<vv^><v><^^>^vv>>><^<<>v<^^v^^vv<<<^<^^v>vv>^<^>^^^^><v>vv<^v^>>^<^^<<^vvvvv^^>^>^>vv^^v^v><<^<<>>vv><><>v^><v<^<^<<>vv<<v^<^<>v^v^<<>^^<<<^<>v^^>>^<>vv<<v^><v^^>^>v<>^>^<>v<><v<<<vv<^v^v>v><^<>^><^<vvv<>^v<<^<^<<><^<v>>v>^v>^v<>>^v<^^<<>v<^>^<^v<><><><^>^<>^>vv>>>^v<vv><<v<><<>v<<<>v^<>v^><<^^v<v<><^^^^v>>v>^<^v<^^<<>^^<<v<>v<>v<>vvv^>>v>v^<><<^>vvv>>^>v^v><<<v^>^^v<<vv<>v^^<vv^<<^^<>v>^v<^><vv>^v>v<^^v>>v>><<<vvv>v>^>>><<<>^>v>^<v<^^^<^^><<<^^<^v>><v><<^>>>vvvv<><>>v<v^v^><<^>^><v>>vv><<<<^v>v>>>v^v<><^^><v<v<v^v<<^^v>v><>>>v^>v^<<><<^>v^^v<>^^^>v^^^<>v<<v<>v<>>><>^<^<>v>^vvv<><v>>^^>><<^^<v<<<><>>>>^v>v<v><^v<<^<<<>><v>v<^>^<<>v>v<<v^vv^>vv^>v>>>^v>v>v^vv^^<v>><><^<^><>^v<v>vv^vv^^<<v<v>><vv>v<^<>v<>^vvv>v>>vv><>^^<v<>><v^>^^^v^v<<^v><v>>^^>>>v^^
<<^<vvv<v^<^vvv^<^<><<<<^<^>^>>>vv<<<<>>v^^v^><>^>v<<^<<<v>^<^<>^vvvv>>v^><^>>v<<^^>v<>v>^v^>>^>v>vv>^<<>v<v<^>v^>>v<^<v^>>v^>^^v^>><<<^<vv<>v^<^<^<<<v><^v>>>^v^>v>>^<v>v>v>>vv^><<^<v>^>>>^v^>v<<v>^^^>^v>^>^^^^v^v><<<<^>v<<>^v^vv>><^^>vv^>>^^><<^v<>v<v>^^^vvvv<>^>>v^vv>^>v<<^<<^vvv^>^>v<^^>><^<<^<^>vvv^^^^vv><>^<>^vvv<^<<v<<vv><<><>^<^>^>v><^>>^>^<v<^<><<v>>>>^^<v>>>><>><vv^^<^^^><v>^<<>vv^v<>v^<>v><>>><v<v^>>vvvv<vv>>^<vvv><^v^<<>^<vv>^>^<>^>v><^><^<v^vvv><>>>>v<v>^<^<<^>><<v>v><><><>v>>vv<>vv<v>^v<>>v<^<^><v^^>>v><v^>v<^>vv^>><>^^^<>^v>>>>>><<>>><>^>v^<^<^vv><>v<<^<<<><^^<<>v^v<v<<^<^<^<^<^v^vv><<><<^<v^^^>^^v<<v><<v^<<v>>>>v^^<<v><^<>>v>v>^vv>^vv>>^<^>^<>^^><^^><v><^v>^<vvv<><^v^^<vv>^^^^^>^^><vvv<v>^>^^<^v^^^^>^^<v>v<^<v>v^v<<v><v^><>v^^<v<^<<^v<vv^><><>><^vv>^v^v<^<v^^^<>v><v^^<<^^<^>v>v><<^<>^^><><^>v>vvv><>^^^^<><vv><vv>v^>><^v^v^>v<<>vv<^^v><v<v<v>^^<>>^>><^>^<^>v><vv^<^v^^<v^>>vvv^^v><<>>>vvv>^vvvvv><vv^<>^v^v<v><<vv^^><v>^^v<^<<<^vvv<<v<<^>^v<^v^^>^^v<>>>v^<^^><^<^>>>vv^^><^>
>^^>^v^>>^^^><v>>^>v^<v<<v>^v><vv^v><^^vv<^<><^>>^>v>^^^v<>><v<vvvvv>^>><>^><^v^<>v>^^^<<<<v><<<^<^<^>v><^><<v<>^><<<>^><^>><>vvv^<<>>v^<v^>v>^><v<v^^<<>vv^<^<^<>^^<>v>>^<<<^<<>>>vv^v^v>^v><v>^<<vv<vv^^>vv>v><v<><<vv^<>vv<v<<v>v^vv><<<>><v><>>^^^^<<v^<^><<vv^vv<>v><^<^^^^>^v^<v<vv^^<<^^>^^>^>>v<<<>^vv^vvv<v>>^v>>v>vvv<>>^v^<^>vv^>>>v^^>><v<^>>>^v^<v><v><<>>v<>v^v<<v>>>>>><v^vv<<>v<vv>>vv<^>v>v^><^vv^v><<v^v^<^^^^^<^>^<>v>v<><<<>^><v>vv><><v<v>>^v<v^>v^<<^^v^^>v<vvvv^<<^>>><^v>^v>^v^>>><>v^><^^^^^^<<^>^^>^vv<^><>v<vv><<^v^v><><>^^<^^<^vv<<><v<^>v>^<v>v<>>>^<v^^v>>vv^<vv>^>>>v>^^v<^^v><>^><>>v>^>>^>vvvv^<<<><v^^<v<<v^^><>>>>v^v^^<><<<<<v^^^v<^<<v<^vv<^>^><><<<^>>vvv>v<v<^v>^v>>vv^vv<>><v>^^^>^^^v^<><<<^^^vv>v>vvv<>vvv<v^>v^v^^v<>v<>>vv<^v^>v^^<^vv^^>><^><^^<><<<v<v><vv>v^^>^^^<^vv>vv^v>>^<vv<><>>^^>^v^<>>^v<>v>v<>v<<v>v>^>v>v<><v<^v<^<v<<<><vv<>vv^v><^^<v^v^^vv>v<>v>>><>>v><^<<><<>><v>vv<^<<vv<v>vvv<><>^vv<v><^^v^>><v>>>v^>v<v>>vv<<v^>>>>>v>^<>^<^>><>v<vv>^>vv<^<^v<v^<<vvvv>^^<<v^<vvvv^v
<^<^vv^>>>^v^<^<^>^^^^>>v<vv<><v>vv^^v<<v^v<^vvvv^v^^<v>^>^^>>v<v>vv><<<^^>>>>>vvv><v<<^^v^^v><>^vvv<><^><<>^<v<<>^>>v<<>v><vvv<<^^^>>v^<<^^v^v>>><>v<<v^^><<^<vv^<v>^v>><><<<v^>>vv^vvv<>^>v<<>><<vvvvv>vvv<^>>>v<<^>^^v>>>^>^>^^^v^^^<^<^^><><<>v<>^<vv<<>>v<^vv<><v^^<>>^>^<^><>v<<<v^<v>^vv>^>vv^>v<>>>v^<>><<><v^v^<^vv^vv<<>^<<v>><v^v>^^^^><v><<>v>^v<>^<^<<v^>^>><<^>><>^>vv<v><v>>^<v^>v>>v^<><<>^<^<>v^^v<>v<>v<<v<>>vv^^vv^<v^^^^vv>^<<><v^v<<v>^v^v^v<<>^^v><^v>><v^^<<<^<<><>v<>>vvv<^>vvv>vv<v^>>>>>v^>v>><v>>^>v<vv<^v^><vv<^v<>>v><^><>>v<^<^<v><v<<^^^vv<>>^^^<>vvv>>>v^<><v>^v^>>v<<^<v^<^^<>^<>v<^>>><>>v>^vv^^<<>^^<><>>>v><>vv<<<<^<<^<v><^>v>><<v^v^vv<v<<<vv<><v>>v^<<<^<<><vv<v<<>^^<^^>^v>v>><<v<^vv>><<v>v<<^<<^v>><^<>>^^v<>^>^<>v^>v><vv<^^^^>>^v^v>vvv<v>^v>><v<<^vv>^<<^<>^<v^>^v<^<vv>v^^v><v>v>v<v^vv<>^v<v^v^>><<<<>^<v<<>>v>><^>v>v^^<^^^vv^>>vvv>^v>>>v<<^^>^<<<<^vv^^<>^v^<<>^>v^<v^<<vv>v>>vv>vvvv<><<v>>>^<v><>>vv><^^^<^v><^^<vv<<<>^<v^<^^v>^>^^<v>>^^vvv<<^^>vv>^^>^<<><^^><v><>><vv<>>v^^>vv^<
^>>^<<<v>^<<><v<<^<^>v<v><>^^v^v>v>^v<>^>vvvv<>><<v<^>^<>vv<>^v>><<^^v<<^>><^^^>^>^<>>v<v^^vv^v^>^v^^^>^<v>^^>>^>v>^>^<<^^<<<<>><^^^><<^>^^>^<^^>^>vv<<^<v>^><vv>vv<<<<v>>>><v<<>>>^^<><<><>^^<v^>><<^>^v^^v^<^<^>^>v>^>vv>vv^<v>^^^v>>><<^^v^^^>^><^><v><<>^>^<<vv>^v^>><<v>>>>^^^v>>v^v<<v<v>>>>>>v^>v<v^<><><v<<^^vvv>^^<v<>>>>^^>>>^v><^<^>>>>>v>^vv>v<<>^vvv>^v>^<>v>vvv^<v<v<v><>>><^><<^><^v>v>^>>v<<^<vv>vvv><^<<^^>^^>^v<^v^v^^<^<<^><^<^<><<^<v^v><v><>>^><^<>v<>^>^v>^^vv>^v<>><>vvv><<>^^^v^>><^^^>><<^<<^<vvv>><>^^v^v<^><>^<^<<v>^^<><v>^<<><v<><<^>>v>>><<>^>>vvv>v<v^v>^v^v^^<^v>><^<<><v<<^>>^vv>^<v^^<^v<^v<^<<v>v^>v<v<vv^<>^v^><<<^<^^v^v<^vv>^v^<v^v>vvv><v<v<<^v^>^^><>v>>v^<<>^<v>><^<>vv>^^^^><<>^>^><^<<>vv><v^<^<v<^vvv^^<vv^<^<>v<^v>^><<^<<v><^<v>vv^v^>v<>><^><v^<><v<^^v^v<^<v><><<<^vv><>>^>>v<>v<><><^^<<v>v<^v^v^v^^<><v>^<^v>>vv<^<v>>^v^<vv>>>^><>>^v^>^^<^^<v^><>>^>><^v<>^^vv>^<^^<v><<vv<v<<<<vv>>^^>^<^<<<^<>vvv^>>^v^>^<<^^v<vv<v>v<^^><<<^<>^><<^>v<v<^vv<>>v<>>>^<>>v^^v<^<v^<v>v^>><^v^<>>>v>
^>vv<<>v^^^^^v^<^^><^>><>^>>vvv<v<v<<v>>^>v<<>v^^vv^<<>>^^><>><^>>>><><vvv^<>^^<^v<>>^^^^^v^v^vv>v<v<v>v>>><<^<>>^<>v>v<<^<>^>^v>>^<<vv>v>v^v<<^>>><><<^v>^>^<v>^<<><<^^>>^^<<<>^>>>>^^><vv<v^^>>^<>v>v><^^v><vvv<<<^^<>>vv^><<>^^^^v<v^<<>v>^<><vv<^vv>><^<^vv<>^>v>vv>^<vv<<vv<><<v^v<^<>><>>><v^^vv>>^>>vv>v>v^^>vv<v><^<v^vv<<><v>>^^^>^v^^<^^v<>v<v^^><^v>>v>>vv<><^^^^<>><<<v^><^^v^<^v^<vv>v<<v^^>vv<>><^^<>v<<^v^<v^vvvv<vv<vv<>>v<^<<>>^<^v^v>><<^<v^^^>v^<^vvv^>^v^v^>vv>^^>v<<vvv^<^^<<<^<>><vvv^^>^<><<^v^vv^<><>><>^v^v^v^><<^v^>>^>^><>>v<<^v>>>vv^^^^<<^<^>v>>v>>>v<>>^^v<v<<^vvv>^^^<^<>><^v><<<<vv>v>>v^vvv^v<^>^v<^><<vv^^>>><^<vvvv^v<<^^^<<<<v>vv>vv^>^^>>^<v<v^>>^^>><>>v>>>>>vvvv<>^<>^^<v^v><<<>v><^>v><vv<^^>><v<<^<^v>>^^>><<><><<<^>^<<^<^vv>^>>><<^<vv^vv^<><^<>>^>^><^><v<v<<>^^vvvv^v^^vv>^>>>>vvv>v^^^^v<^>>^^<^<^<>><v^><>>v>^v^><^^v>><v<>v<vvvv<v><<^^>v<<<v<>>^<^>vvv^v<><v<><>><><^<vv>v>>>><<><^<<vvv>vv>>^>vv<>>^v^>v^>><<<>v>>^<<^^vv>>v^<vv>vv^<><<v^v<<<v>v<vv>v><^vv^v>^v<^^<<^>v>^v><<^<^^<<v<
^>><>>v>^v<>>^^>v<v^>v>v>v>vv^>>^<>>^<><>v>v<<v>^<^v>><v<<^^v><<<<>vv><vv>^>><<^v^<^^^<v^>vvv>^>vv><v><<^<vv>v<><v<^v<>^<vv^v><^<>^v^>vv^^>>><><vvvv>^^><v^>>><^>><vv<^^^>>vv^<<<<<v>>vv<v><>>v<v><>><^^><^><^v<^>^<<^v^>>><>><v>v<><<v<^vv^^<><<<>>v^>vv<v<>v<^><<v>^vv>>>v<^^><><^^^>^^<>^v<<<<>>^^^<>^^^vv<>v<<>^<<^v><^>^^<^>>>v>v^v^vv>>v^>v<v^^<<<^><^v^v>>^<>v<<<^><<<><>vv<^v^^<^><v^<<<<>^^<v^^>v^v<vvvv^<^>v^^v<<><^v^><^^<>>^^>v><vvvv^<><^vv^vv^v<v^>^^^><^v><v^<v>^v>^v<^^<vvv><<v>^^><^vv<<^<^v<^^^>v<v^^>^><v^>^>vv><>^^>>^v<<^^v<^vv<^<v<v<><<vvv^>v^^v^v^^<><^v<^v>vv^vv>v^^v<>v>>^<^^^^<<^v>><<v^<>^vv<v<<^>^^v><>^vvv<>^v^>v><v<^^^>v<>vvv<v<<<v>^>v^^<^^^>v<><v^<v>>>>^>v<vvvv>v<>><v^><<<^^^^><^vv^^^<^v>>^v<<<><>>^vv^><>>^<><^^^v^<<>^^^<<<<>^><^>^<^<<^v><<><>vv<vvvv<v>^v^v^>>^^^<vv<<<>>v<<>v^v<>>^<<^v>vv<<><<v<^<>^^<<<v<^v^^>^>>vv<v><<^^^vvv><v<^<>>v>>>>>^>><v<>>^>>>v^>vv><>vv<v^><v<><>><>v^>^><v<<v>^<v<<<<<vv>>^vvv^>vv<^<>^<<<v^<^>^v>>^vv>><^<<>>^<<v<^<<>v>^v<><<>><<>^<^<>v><<<<v>>>^<<v<^>v^^v^v
^<v>v<><^>^^<v^>^^^<<>^v^^<^>>>v>vv><^^<v^<v<<<<<<v<vv>>v<^v>^v<>v^^^>v>v><>v^><<<>^>>vv^v<^><^v<><vv^vvv<>>>^>><v>>^^v><^^v><<^>vv><vv^v^><>v^<v>v^>^<vv><<vv^<<^v<vv<^^<^^^<<^>^v>>v>v>vvvvv<<^<^<v^<>>><<><<<<^^^><^v<<^<^^>v^v<<v><v<<^v<v^^v><>vv<<>vv<>>><v^<^<^^<<vv><<^v^<v<v<>^^^vv<><v<>>^>vv>vv<<v^^v^vvv^^^v<<v^>^<<<>^<>vv><>^^v<<v<^v<>>>^^>>v>^<v^v^vvv<<>v<<<<^<<>v<<v<><<^>^^>^v^<<<<v>><vv>vvv<v>><^>^v>^><<^>vv^^^<^>^^^>vv>v<<>^^<v<><>^^v<^<^v>^^vv><>vv<^^^^>v><><v^>v><<<>^>vv>>v^>vvv>><>^v>>^^v<^<<v^<^^<>^<>>>><^<>^><v><><v<<<>>^<<<vv^v^^<^>v^<<v<^^<><^>><>>v>v<^v>>><>><><^>vv^><>^v^v<vv>^^^<^<v<vv>vvv^><vv<^v>v>>^>><>>^>v>>><v^^>^^^v>^^v^^<<>v><v<<<v>^^>vv<<<^>>^><<<<><^<>>^^vv^^><<>^>vv>^v<^>^v>>vv><^^<>v>^v<v>>v<><vv>>^<>>><<v^>v^<^vv>^><<v<><v><>^<^vvvvv<^v<>^v^<>v^v<v^^<><^>>><^^><^^<<^^<<^^<<^^>v<<^^>>>v><^<<v<<>v<v^><v^^<<^^>^^v^vv<<^<<<v^v<<<<^^<^v>><<^^>v>^v>v<<><><>>v><>><^>v<><><<v<vv>v>vvv><<<<v<>^^>><v<><^<<<^v^^^<<v^>>>^v>vv^>v<<^vvv>vv<>^vv>v^>>v<^<>vvv>>vv^^<><^>^^
v><>vvv>v>v<v><><^^<v>>v<v<<<^<^>^^^v<<v>^^<^v>^v<>><^v^>>vv<^<^<v^v<<^v^v>^^<^^<<><>v<v<v<^<^><^^<>^<>>>>^^<v^>v^^<v^^^<^>vv>^>><^v>^^v^>v>v^>v<v>vv^<<v><<<v^><<^<><vv^<<<<^<v<v^>>^^^v^v>>^>v<v^<>v<vvv>>^^^><<^^^<><<<^^^<>^v<^>>v^^v<<v>v<vv^v<^>^vv<^>^>v<<vvv><<^>>v<^vv<<<v>v>^v<vvv^^>^>v^v^<<^^>>^<<vv<v<>v^v<><^^<>vvvv>^^><^>^<v<vv<v^><<v>>^<v^v<<>v<>>^<<v<>>^<v<><v^>>>>^^^^<<^^>^>>^v^^>>><>>>^vvv>>><^<v^v><v^v>>vv^>><><^v<<>^>^^><<<vv<><>>^><v>>v<<^v<<<v<^^<^<>><v^><>v<>^>v<v<^>v^>v>^^>v>>^v<^v^v<>^v><^vv<<>>>^><<>v<^v>v^v^^vv^<v^>^^vv<vv><<<^>^><^^<><v><vv^v<^<>>v^^>^^>><v>^v><^>v><<<^^<^>^^^^^<<>^<vv>vv><<>^><vv^<^^>>^<<^v><><>>^v<<>>^>^^v<>^>^>>>v><v^<>>v<>><>>v^vv<^v<^<vvvv^v<^v^><^^>>^<^^>^v>^^vv<v>vv<^^>^^>^<<>v<>^v^>><^<^^v^^v><>^>>^v^<^<>vvvv>v<>^^>v<<><<<vv^v>>v>>>v>><^><>>^<^<v^>><<^<>>v<v<>v<^>><v<>v^<^<v>>>>^<>>><^<v>v<v<^<v<<<>^^<^<<<^^><v^v>>><>v>v<^>^^^>v>vv<<<>>^<v>^^<^<>>^v^>v<v>v>v>^vv^v>v^>^<^<v><^<>^^^^^v><^^^^><^^vv<<v^v<vv<vv^<>v>>^^>^v>>^^^^>^><^>v^<v<v>^<>^^<
^vv^>>^>^v^<^><<<v<>^^^<v<vv<>>vv>vvvv<v<>vv<v>v^v^>>v<<<><v<v<>^<><v><>v><^v>vv><v^vvvv>v<^<v<^<^>v>><v<vv<>^^vvv><^vvvv^<v><^v^><^>>>^vv<>><<><<<^^v>^<v>^v><>>^vv^>^^<^^<v>v>>vv<>v<^<<><<<^>^>vv<>><>>vv^^^<<v^<^^<^<>>v>v>^^<v<<<^<>>^v>^v^^v^>v^<^<>v<<<>>v<v^>^><>>^vvv^>^>>^><<v<v>^^^>v><^v^^^^v>v^<^v>><><v>><^^>>>vv^^^>^v^v<<v>>v<>>^<<vv<^v>v<v^<<^<<<v>>vv<<><<><v<>>^>>v<^>vv^<^>v>v>>>^^v>v^^^vv<><^v^<v><<vvv<><<v<v^v<v<^<<v<>v>><v><v^^><<<<^<^>>^^<^v>v<vvv<><^>>>>^v<^v<^^v<><^v>^v>vv^>>v^>>v><<vvvvv^^^^^<<>^<>>^<<>>^v>v<<>v<><><><v<<>^<v^>>^>^>>v<^^<>>>>v>>v<v^vv>>^v^<^><^<>><<<<>>>><v<v^><^>v<<<>^<<^><^v^>>>^^^>^v^vv>><^<vvv^>vv<><vv^v<v>^<<v><<<>v^^^^^v>vv^<^<>^<<vv<<v^<^>^v>>^^<^^>>v^<vv>>^vv>>vv>><<v>^<<<^vv>v^<>v<<v<^>v>^^<v<^v>^<<vvvv^<>v>^v^^^>>>^vv>^<^<vvvv<^^<^<^v>^^<v>^vvvv<^^><<<>^<<v<v<v^<^>vv>v<^<<v>^v>^^^<v<^v>><^^>v<^^^^>v<^>v<>>><<<^<^<^<>>^<^^><^>^^<v><<v^^^v^^^>^>v>^>><>><^<vv<>vv>v^<vv<><<<<>^<v<v><>><<<<vvv^>^<><v<^<><>^<^^^<^v>vv<<<><^><>v><>^^^vv>>>^><>>v><>^^<
<vvv>><^>vvv^>v<<>>vv<<>vv><><><vv^^<v>>>v<><v>^^v^v<<v>^vv>v<v><>>>vvv^^vvv>^^><<>^vv^>^<v>^v>^vv^<>vvvv^><v>v<><^>v>v<^>><^^vvv<<^>^v>^>vv<>>vv^>><<v>^^<^<>^^>><^>^vv^>^>v<v^><^<<^^<<>^v<>^vv>><<>v^>^<v><<^^<^><v>^vvv^^vvv^^<v><>v<v>>v<^^^v>v^v<v<^v<>v^<<v>>v^>^<>>^>>>^>v>v^<<><v>^v^>^^v^^<v><^vvv<>vv^v^^^^v>vv^<>^>vv^>^^^vv^>v^<v<><>^v>>v<^<>><><<<^v<>><>vv^vv^>>^^^<^>^<^<v<vv^vv<><<v>^vv<v>v^><^^^^vv^^<v>^^^<<<^>^^>^^>>v<<v<>><vv^^vv<vv>^><<<^>>>>vvv^v>>v^<vv<>^<vvvvv^v><^^>^v<<v>^>>>vv<^^><>><v^<><^>>vv<^<>>^vvv^<<^><^v<><>>v<^><>v>>^<<>^^><^^<^<^vvv<<v^<>>v>><<>>vvv^<<vvv<>>vv>^v^><><^^><^><><<<><>^^v<^>^><<<><>vv>>><^<^<<<^<>^<^<<>v<<^v<v>>^<<>^^>^^vv^>>><^^^>><^><><^^^v<^>v>^^^vv^<>>^<^vv^^vv<><v<v^>><<v^vv^^v>v^>^>^<>v^^<<>^vvv>v<^v>><^<v>v<>^^<>^<<v^>>^^<<<v^v<v>v<^>vv<<<<v>v>>vv<v<vvvv<^vv<>^v>^v<^^v<<<>>>vv<<>>vv>>^><v>^>>^vv<vv<vv>><v^^<^<^>>>^<vvv^vv><^>>v<<^<><^<><<^^v<v>>>vvvv>^<<v^v^><>vv^^v^^^^^<v>>^^^^v<^><^v<v<v^>vv<>^^vv^v^>>^vv<<<^^><v>><^v^v^^^^^^<v^^<v<v^><v>vv^
><vv>vv<^<^^<><^<<<v<^>^^<<v>>^v>v>v^^v>>>v>>vvv>>v>^<>vvv<v>><v<v>^>v>>^^<>^^<<<>>^^vv^<<^vv^<<^><>>v>><v<<><>>^v<<>><^^^vvv>>>>v>^v>v<vv>v>v<>^>>^v<vv<><^^v^<><<^^^<^>^v<^v<>vv><<v^><><^^>^>v<vvvvv^^^vvv^<^v^v<v<<<<<><<v^v>>^^^^>>^v^<vv^vvv<>^v>v<^^^v>vvv>>^^^^<vv^>>>^^^v<v>>^^<>^><<>>v<<v<<><^>>^vvvvv^v<<><v>v<v^^<v^^^<^<<>v>v>v<>^<^>>^>^^^<<<v<^^^>v^>v>^v^v>>^<<>^><v^v^^>^v<<^v>^<v<v<>v<>^^<^<v<<>^><^<>^><v>>^v><<^>^^>>vv^^<><^v><<>^<v^vv><^<^v><>>>>^<^>><>v<^vvv>^v<<<<^vvv>><vv>v^^<vvvv<v^^<v^^v^<>>^^v^><vvv>^>^^^^^^<v>v>><^^><><>v<<><>^<^><<vvvv^>^vvv>><^>v<>^v><vv<^^<><^<<<^v^^>^><^^v><v<<<v^>>^<<^<v><^vv<<><^>v^<<^v<v><^>v^>>^^v^><v>>><v<vv^v^^vv>^vvv^>v>>v^^>><<<^^^v<v>><vv^v<vv><><<<^>>>v^<v^>>vv^>>v>^<^^<^v<^>^<v^^vv>v^v^^>><>^vv<>^^vv><>^v^^^><<>^v><>v<v^^<^v<<>^^v<v^^>><vv<<<^^>v^^><>v<^^^v<^><<^<^vv>vv<<^><^><^><<>vv<><>v<v<v>^^^^><^vvvv<>>>vv><>^>^^>^<<v^<<v^<<^^>>>>v^v^v^vvv>^<v><v^>vv^<^^^<>v>>^<><<<^^^^>>vv><>^^^^>>v<<v>^<<><vvvv<<^<^<vvv>>><<<<^>vv^<^<v^>v^>>>^vv^v><
"""

from time import *
start_time = time()
for data in inputs():
    print(*solve_puzzle(data.strip()))
end_time = time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
