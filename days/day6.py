import re
from math import sqrt, ceil

part1_exp_test_result = 288
part1_exp_result = 1084752
part2_exp_test_result = 71503
part2_exp_result = 28228952


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


def part2(_input: tuple[list[int], list[int]]) -> int:
    time = int(''.join([str(x) for x in _input[0]]))
    dist = int(''.join([str(x) for x in _input[1]]))

    root = ceil((time + sqrt(time ** 2 - 4 * dist)) / 2) - 1
    return root - (time - root) + 1

