import functools
import re

part1_exp_test_result = 8
part1_exp_result = 2776
part2_exp_test_result = 2286
part2_exp_result = 68638

_game_re = r"Game (\d+): (.*)"


def process_input(lines: list[str]) -> list[tuple[int, list[tuple]]]:
    """
    Represents each line in the input as a tuple of 'game-id' and its corresponding subsets
    :param lines: lines of program input
    :return: list of games with subsets
    """
    processed = []
    for line in lines:
        game_id, subsets_str = re.findall(_game_re, line)[0]
        subsets = [_get_rgb(s) for s in subsets_str.split('; ')]
        processed.append((int(game_id), subsets))
    return processed


def part1(_input: list[tuple[int, list[tuple]]]) -> int:
    cubes_rgb = (12, 13, 14)
    cnt = 0
    for game_id, subsets in _input:
        if all(x[i] <= cubes_rgb[i] for x in subsets for i in range(3)):
            cnt += game_id
    return cnt


def part2(_input: list[tuple[int, list[tuple]]]) -> int:
    power = 0
    for _, subsets in _input:
        rgb = [[x[i] for x in subsets] for i in range(3)]
        power += functools.reduce(lambda x, y: x * y, [max(x) for x in rgb])
    return power


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