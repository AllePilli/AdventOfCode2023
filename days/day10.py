import copy
from functools import lru_cache

part1_exp_test_result = 8
part1_exp_result = 7097

_pipe_types = {
    '|': ('n', 's'),
    '-': ('e', 'w'),
    'L': ('n', 'e'),
    'J': ('n', 'w'),
    '7': ('s', 'w'),
    'F': ('s', 'e'),
    'S': ('n', 'e', 's', 'w'),
    None: (),
    '.': (),
}

_invert_dir = {
    'n': 's',
    'e': 'w',
    's': 'n',
    'w': 'e'
}


@lru_cache(maxsize=None)
def _get_neighbour_idx(x: int, y: int, width: int, height: int, direction: str) -> tuple[int, int] | None:
    match direction:
        case 'n':
            if y > 0:
                return x, y - 1
        case 'e':
            if x < width - 1:
                return x + 1, y
        case 's':
            if y < height - 1:
                return x, y + 1
        case 'w':
            if x > 0:
                return x - 1, y
        case _:
            raise ValueError(f'unknown direction {direction}')

    return None


def _get_neighbour(x: int, y: int, direction: str, grid: list[list[str]]) -> str | None:
    n = _get_neighbour_idx(x, y, len(grid[0]), len(grid), direction)
    if n is None:
        return None
    return grid[n[1]][n[0]]


def part1(lines: list[str]) -> int:
    grid = [[x for x in line] for line in lines]
    start = (0, 0)

    for y, row in enumerate(grid):
        for x, pipe in enumerate(row):
            if pipe == 'S':
                start = (x, y)
                break
        else:
            continue
        break

    def move(current: tuple[int, int], direction: str) -> tuple[int, int]:
        match direction:
            case 'n':
                return current[0], current[1] - 1
            case 'e':
                return current[0] + 1, current[1]
            case 's':
                return current[0], current[1] + 1
            case 'w':
                return current[0] - 1, current[1]
        raise ValueError(f"Unknown direction {direction}")

    def connects(direction: str, candidate: str | None) -> bool:
        if candidate is None:
            return False
        return _invert_dir[direction] in _pipe_types[candidate]

    possible_starting_positions = [x for x in
                                   [(d, _get_neighbour(start[0], start[1], d, grid)) for d in _pipe_types['S']]
                                   if x[1] not in (None, '.') and connects(*x)]
    _max_path_len = 0

    for incoming_dir, first in possible_starting_positions:
        main_loop = [first]
        cur = move(start, incoming_dir)

        while main_loop[-1] != 'S':
            incoming_dir = [di for di in _pipe_types[main_loop[-1]] if di != _invert_dir[incoming_dir]][0]
            cur = move(cur, incoming_dir)
            main_loop.append(grid[cur[1]][cur[0]])

        _max_path_len = max(_max_path_len, len(main_loop))

    return _max_path_len // 2
