import re

part1_exp_test_result = 4361
part1_exp_result = 536202

_part1_num_re = r"(\d+)"


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
        for match in re.finditer(_part1_num_re, line):
            edges = _get_edges(y, match.span(), grid_dimensions)

            if any(lines[iy][ix] != '.' and not lines[iy][ix].isdigit() for ix, iy in edges):
                _sum += int(match.group())

    return _sum
