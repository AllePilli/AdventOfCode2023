import re

from unopt import unwrap

part1_exp_test_result = 13

_line_re = r'Card\s+\d+: (.*) \| (.*)'


def part1(lines: list[str]) -> int:
    _sum = 0
    for line in lines:
        winning, numbers = [set(map(lambda y: int(y), re.split(r'\s+', x.strip())))
                            for x in unwrap(re.match(_line_re, line)).groups()]
        power = len(numbers & winning)
        if power > 0:
            _sum += 2 ** (power - 1)
    return _sum
