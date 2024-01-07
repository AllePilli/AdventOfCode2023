from typing import NamedTuple

part1_exp_test_result = 8
part1_exp_result = 7097
part2_exp_test_result = 10

Point = NamedTuple('Point', [('x', int), ('y', int)])


def add(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)


def mul(p: Point, a: int) -> Point:
    return Point(p.x * a, p.y * a)


def sub(p: Point, q: Point) -> Point:
    return Point(p.x - q.x, p.y - q.y)


N, E, S, W = Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)

_pipes = {
    '|': (N, S),
    '-': (E, W),
    'L': (N, E),
    'J': (N, W),
    '7': (S, W),
    'F': (S, E),
    'S': (N, E, S, W)
}


def _get_starting_points(grid: list[list[str]]) -> list[Point]:
    s = [Point(x, y) for y, row in enumerate(grid) for x, pipe in enumerate(row) if pipe == 'S'][0]
    neighbours = [Point(x, y) for x, y in
                  [add(s, d) for d in [N, E, S, W]]
                  if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] in _pipes.keys()]

    return list(filter(lambda n: mul(sub(n, s), -1) in _pipes[grid[s.y][s.x]], neighbours))


def process_input(lines: list[str]) -> tuple[list[str], list[tuple[Point, str]]]:
    grid = [[x for x in line] for line in lines]
    paths: list[list[tuple[Point, str]]] = []

    for start in _get_starting_points(grid):
        path = [(start, grid[start.y][start.x])]

        while path[-1][1] != 'S':
            pos, cur = path[-1]
            if len(path) == 1:
                n = [x for x in [add(pos, y) for y in _pipes[cur]] if grid[x.y][x.x] not in ('S', '.')][0]
            else:
                n = [x for x in [add(pos, y) for y in _pipes[cur]] if x != path[-2][0]][0]

            path.append((n, grid[n.y][n.x]))

        paths.append(path)

    return lines, max(paths, key=len)


def part1(_input: tuple[list[str], list[tuple[Point, str]]]) -> int:
    return len(_input[1]) // 2


def part2(_input: tuple[list[str], list[tuple[Point, str]]]) -> int:
    grid, path = _input
    path_pos = {pos for pos, _ in path}

    start_pos = [Point(x, y) for y, row in enumerate(grid) for x, p in enumerate(row) if p == 'S'][0]
    connected_to_start = [path[0][0], path[-2][0]]
    start_connected_dirs = [x for x in (N, E, S, W) if add(start_pos, x) in connected_to_start]
    s_pipe = [x for x, dirs in _pipes.items() if all(y in dirs for y in start_connected_dirs)][0]
    grid[start_pos.y] = grid[start_pos.y].replace('S', s_pipe)

    def edge_cnt_contribution(p: Point, dirs: tuple[Point, ...]) -> int:
        pp = grid[p.y][p.x]

        if (pp in ('F', 'J') and dirs in ((N, E), (S, W))) or (pp in ('L', '7') and dirs in ((N, W), (S, E))):
            return 2
        else:
            return 1

    enclosed_cnt = 0

    outside_loop: set[Point] = set()

    for x, y in (Point(x, y) for y, row in enumerate(grid) for x, pipe in enumerate(row) if Point(x, y) not in path_pos):
        if Point(x - 1, y) in outside_loop or Point(x + 1, y) in outside_loop or Point(x, y - 1) in outside_loop or Point(x, y + 1) in outside_loop:
            outside_loop.add(Point(x, y))
            continue

        to_ne = min(len(grid[0]) - x, y)
        to_nw = min(x, y)
        to_se = min(len(grid[0]) - x, len(grid) - y)
        to_sw = min(x, len(grid) - y)

        steps, diag_dirs = max((x for x in [(to_ne, (N, E)), (to_nw, (N, W)), (to_se, (S, E)), (to_sw, (S, W))]), key=lambda t: t[0])

        if diag_dirs == (N, E):
            points = [Point(x + steps - i, y - steps + i) for i in range(steps)]
        elif diag_dirs == (N, W):
            points = [Point(x - steps + i, y - steps + i) for i in range(steps)]
        elif diag_dirs == (S, E):
            points = [Point(x + steps - i, y + steps - i) for i in range(steps)]
        elif diag_dirs == (S, W):
            points = [Point(x - steps + i, y + steps - i) for i in range(steps)]
        else:
            raise ValueError(f"unkown diagonal directions {diag_dirs}")

        diag_cont = [edge_cnt_contribution(p, diag_dirs) for p in points if p in path_pos]
        edge_cnt = sum(diag_cont)

        if edge_cnt % 2 != 0:
            enclosed_cnt += 1

    return enclosed_cnt
