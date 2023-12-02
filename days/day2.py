import re

part1_exp_test_result = 8

_game_re = r"Game (\d+): (.*)"


def part1(lines: list[str]) -> int:
    cubes_rgb = (12, 13, 14)
    cnt = 0
    for line in lines:
        game_id, subsets_str = re.findall(_game_re, line, re.M)[0]
        subsets = [_get_rgb(s) for s in subsets_str.split('; ')]
        if all(x[0] <= cubes_rgb[0] and x[1] <= cubes_rgb[1] and x[2] <= cubes_rgb[2] for x in subsets):
            cnt += int(game_id)
    return cnt


def _get_rgb(s: str) -> tuple:
    completed_str = s
    if 'red' not in completed_str:
        completed_str += ', 0 red'
    if 'green' not in completed_str:
        completed_str += ', 0 green'
    if 'blue' not in completed_str:
        completed_str += ', 0 blue'
    parts = completed_str.split(', ')
    return tuple([int(x.split(' ')[0]) for x in sorted(parts, key=lambda y: y.split(' ')[1], reverse=True)])
