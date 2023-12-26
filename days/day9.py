from helpers import window

part1_exp_test_result = 114


def part1(lines: list[str]) -> int:
    _sum = 0
    for seq in ([int(x) for x in line.split()] for line in lines):
        diffs = [seq]

        while not all(x == diffs[-1][0] for x in diffs[-1]):
            diffs.append([y - x for x, y in window(diffs[-1])])

        _sum += sum(x[-1] for x in diffs)
    return _sum
