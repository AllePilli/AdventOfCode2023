from helpers import split, transpose

part1_exp_test_result = 405


def part1(lines: list[str]) -> int:
    s = 0
    for g in split(lines, ''):
        grid = [list(x) for x in g]
        s += _get_reflection_score(grid, multiplier=100)
        s += _get_reflection_score(transpose(grid))

        # ss = _get_reflection_score(grid, multiplier=100)
        #
        # if ss == 0:
        #     # has no horizontal reflection
        #     grid = transpose(grid)
        #     s += _get_reflection_score(grid)
        # else:
        #     s += ss

    return s


def _get_reflection_score(grid: list[list[str]], multiplier: int = 1) -> int:
    s = 0
    if grid[0] in grid[1:]:
        # perfect reflection from left
        end_idx = grid[1:].index(grid[0]) + 1
        if _is_reflection(grid, 0, end_idx):
            if (end_idx + 1) % 2 != 0:
                for l in grid:
                    print(''.join(l))
                print(f'odd length: 0 - {end_idx}')
            reflect_idx = int((end_idx + 1) / 2)
            s += multiplier * (reflect_idx + 1)
    elif grid[-1] in grid[:-1]:
        # perfect reflection from right
        start_idx = grid[:-1].index(grid[-1])
        if _is_reflection(grid, start_idx, len(grid) - 1):
            if (len(grid) - start_idx) % 2 != 0:
                for l in grid:
                    print(''.join(l))
                print(f'odd length: {start_idx} - {len(grid) - 1}')
            reflect_idx = int((len(grid) - start_idx) / 2)
            s += multiplier * (reflect_idx + 1)

    return s


def _is_reflection(grid: list[list[str]], start_idx: int, end_idx: int) -> bool:
    if end_idx - start_idx < 2:
        return True

    for i in range(1, 1 + (end_idx - start_idx) // 2):
        if grid[start_idx + i] != grid[end_idx - i]:
            return False
    return True
