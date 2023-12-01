import re

part1_exp_test_result = 142
part1_exp_result = 55621
part2_exp_test_result = 281
part2_exp_result = 53592

_num_int = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
_num_re = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'


def part1(lines: list[str]) -> int:
    nums_on_lines = [[c for c in line if c.isdigit()] for line in lines]
    return sum(int(x[0] + x[-1]) if len(x) > 1 else int(x[0] + x[0]) for x in nums_on_lines)


def part2(lines: list[str]) -> int:
    nums = []

    for line in lines:
        if line[0].isdigit() and line[-1].isdigit():
            nums.append(int(line[0] + line[-1]))
            continue

        matches = re.findall(_num_re, line)

        if len(matches) > 1:
            nums.append(int(_to_digit(matches[0]) + _to_digit(matches[-1])))
        else:
            nums.append(int(_to_digit(matches[0]) * 2))

    return sum(nums)


def _to_digit(s: str) -> str:
    """
    Returns the number representation of the string
    :param s: Should be only a one-digit integer
    :return:
    """
    if len(s) == 0:
        raise ValueError('String should not be empty')

    if s[0].isdigit():
        return s[0]
    else:
        try:
            return str(_num_int.index(s) + 1)
        except ValueError:
            raise ValueError(f"Could not convert string '{s}' to int")
