import math
import re
from itertools import chain

part1_exp_test_result = 4361
part1_exp_result = 536202
part2_exp_test_result = 467835
part2_exp_result = 78272573

_num_re = r"(\d+)"


def _get_edges(y: int, xspan: tuple[int, int], grid_dimensions: tuple[int, int]) -> list[tuple[int, int]]:
    start, end = xspan
    height, width = grid_dimensions
    edged = []

    if y > 1:
        edged.extend(
            [(ix, y - 1) for ix in range(start - 1, end + 1) if ix in range(width)]
        )

    if start > 0:
        edged.append((start - 1, y))
    if end < width:
        edged.append((end, y))

    if y + 1 < height:
        edged.extend(
            [(ix, y + 1) for ix in range(start - 1, end + 1) if ix in range(width)]
        )

    return edged


def part1(lines: list[str]) -> int:
    _sum = 0
    grid_dimensions = len(lines), len(lines[0])

    for y, line in enumerate(lines):
        for match in re.finditer(_num_re, line):
            edges = _get_edges(y, match.span(), grid_dimensions)

            if any(lines[iy][ix] != '.' and not lines[iy][ix].isdigit() for ix, iy in edges):
                _sum += int(match.group())

    return _sum


def part2(lines: list[str]) -> int:
    _sum = 0
    grid_dimensions = len(lines), len(lines[0])

    for x, y in ((x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '*'):
        neighbour_lines = [
            lines[y],
            lines[y - 1] if y > 0 else '',
            lines[y + 1] if y + 1 < grid_dimensions[0] else ''
        ]

        nums = {int(m.group())
                for m in chain.from_iterable([list(re.finditer(_num_re, nl)) for nl in neighbour_lines])
                if x in range(m.start() - 1, m.end() + 1)}

        if len(nums) == 2:
            _sum += math.prod(nums)

    return _sum
