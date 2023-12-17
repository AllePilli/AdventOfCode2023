import itertools
import re

part1_exp_test_result = 35
part1_exp_result = 31599214
part2_exp_test_result = 46
part2_exp_result = 20358599


def get_minimum_location(seeds: list[int], lines: list[str]) -> int:
    maps_tuples = [list(group)[1:] for k, group in itertools.groupby(lines[2:], lambda x: x == '') if not k]
    _maps: list[list[list[int]]] = [[[int(z) for z in re.split(r'\s+', x)] for x in y] for y in maps_tuples]
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


def part1(lines: list[str]) -> int:
    seeds = [int(x) for x in re.split(r'\s+', lines[0])[1:]]
    return get_minimum_location(seeds, lines)


def part2(lines):
    seed_ranges_raw = [int(x) for x in re.split(r'\s+', lines[0])[1:]]
    seed_ranges = [seed_ranges_raw[i:i + 2] for i in range(0, len(seed_ranges_raw), 2)]
    boundaries = [(x, x + y) for x, y in seed_ranges]
    maps_tuples = [list(group)[1:] for k, group in itertools.groupby(lines[2:], lambda x: x == '') if not k]
    maps = [[[int(z) for z in re.split(r'\s+', x)] for x in y] for y in maps_tuples]

    for mapping in maps:
        rules = [((s, s + l), (d, d + l)) for d, s, l in mapping]
        new_boundaries = []

        for start, end in boundaries:
            rules_for_start = [t for t in rules if t[0][0] <= start < t[0][1]]
            rules_for_end = [t for t in rules if t[0][0] < end <= t[0][1]]
            rule_for_start = rules_for_start[0] if len(rules_for_start) > 0 else None
            rule_for_end = rules_for_end[0] if len(rules_for_end) > 0 else None

            if rule_for_start is None and rule_for_end is None:
                new_boundaries.append((start, end))
            elif rule_for_start is not None and rule_for_end is None:
                boundaries.append((rule_for_start[0][1], end))

                length = rule_for_start[0][1] - start
                offset = start - rule_for_start[0][0]
                new_boundaries.append((rule_for_start[1][0] + offset, rule_for_start[1][0] + offset + length))
            elif rule_for_start is None and rule_for_end is not None:
                boundaries.append((rule_for_end[0][0], end))
                new_boundaries.append((start, rule_for_end[0][0]))
            elif rule_for_start == rule_for_end:
                length = end - start
                offset = start - rule_for_start[0][0]
                new_boundaries.append((rule_for_start[1][0] + offset, rule_for_start[1][0] + offset + length))
            else:
                boundaries.append((rule_for_start[0][1], end))

                length = rule_for_start[0][1] - start
                offset = start - rule_for_start[0][0]
                new_boundaries.append((rule_for_start[1][0] + offset, rule_for_start[1][0] + offset + length))

        boundaries = new_boundaries.copy()

    return min(x for x, _ in boundaries)
