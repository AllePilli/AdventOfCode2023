from helpers import window

part1_exp_test_result = 114
part1_exp_result = 2008960228
part2_exp_test_result = 2
part2_exp_result = 1097


def part1(lines: list[str]) -> int:
    _sum = 0
    for seq in ([int(x) for x in line.split()] for line in lines):
        diffs = [seq]

        while not all(x == diffs[-1][0] for x in diffs[-1]):
            diffs.append([y - x for x, y in window(diffs[-1])])

        _sum += sum(x[-1] for x in diffs)
    return _sum


def part2(lines: list[str]) -> int:
    _sum = 0
    for seq in ([int(x) for x in line.split()] for line in lines):
        diffs = [seq]

        while not all(x == diffs[-1][0] for x in diffs[-1]):
            diffs.append([y - x for x, y in window(diffs[-1])])

        sub_sum = diffs[-1][0]
        for i in [diff[0] for diff in diffs[:-1][::-1]]:
            sub_sum = i - sub_sum

        _sum += sub_sum
    return _sum
