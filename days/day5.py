import itertools
import re

part1_exp_test_result = 35


def part1(lines: list[str]) -> int:
    seeds = [int(x) for x in re.split(r'\s+', lines[0])[1:]]
    maps_tuples = [list(group)[1:] for k, group in itertools.groupby(lines[2:], lambda x: x == '') if not k]
    _maps = [[[int(z) for z in re.split(r'\s+', x)] for x in y] for y in maps_tuples]

    locations: list[int] = []
    for seed in seeds:
        value = seed

        for _map in _maps:
            for dest_start, src_start, range_len in _map:
                if src_start <= value < src_start + range_len:
                    offset = value - src_start
                    value = dest_start + offset
                    break

        locations.append(value)

    return min(locations)
