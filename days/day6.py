import re
from math import sqrt, ceil

part1_exp_test_result = 288
part1_exp_result = 1084752


def process_input(lines: list[str]) -> tuple[list[int], list[int]]:
    time_line, dist_line = lines
    times = [int(x) for x in re.split(r'\s+', time_line)[1:]]
    dists = [int(x) for x in re.split(r'\s+', dist_line)[1:]]
    return times, dists


def part1(_input: tuple[list[int], list[int]]) -> int:
    times, dists = _input
    prod = 1

    for time, record in [(times[i], dists[i]) for i in range(len(times))]:
        root = ceil((time + sqrt(time ** 2 - 4 * record)) / 2) - 1
        prod *= root - (time - root) + 1

    return prod


