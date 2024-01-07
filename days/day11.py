from itertools import combinations

import numpy as np

from helpers import Point, manhattan_dist, sub, mul, add

part1_exp_test_result = 374
part1_exp_result = 9609130


def _expand(lines: list[str]) -> list[list[str]]:
    universe = [[x for x in line] for line in lines]

    for _ in range(2):
        ids = [idx for idx, row in enumerate(universe) if all(x == '.' for x in row)]
        for i, row_id in enumerate(ids):
            universe.insert(row_id + i + 1, [*("." * len(universe[0]))])
        universe = np.array(universe).T.tolist()

    return universe


def part1(lines: list[str]) -> int:
    universe = _expand(lines)
    galaxies = [Point(x, y) for y, row in enumerate(universe) for x, p in enumerate(row) if p == '#']

    return sum(manhattan_dist(g1, g2) for g1, g2 in combinations(galaxies, 2))


def part2(lines: list[str]) -> int:
    galaxies_before = [Point(x, y) for y, row in enumerate(lines) for x, p in enumerate(row) if p == '#']
    universe = _expand(lines)
    galaxies_after = [Point(x, y) for y, row in enumerate(universe) for x, p in enumerate(row) if p == '#']
    velocities = [sub(galaxies_after[i], galaxies_before[i]) for i in range(len(galaxies_after))]

    distances = [mul(v, 1000000 - 1) for v in velocities]
    galaxies_final = [add(galaxies_before[i], distances[i]) for i in range(len(galaxies_before))]
    return sum(manhattan_dist(g1, g2) for g1, g2 in combinations(galaxies_final, 2))
