from helpers import window

part1_exp_test_result = 114
part1_exp_result = 2008960228
part2_exp_test_result = 2
part2_exp_result = 1097


def process_input(lines: list[str]) -> list[list[list[int]]]:
    diffs_list: list[list[list[int]]] = []
    for seq in ([int(x) for x in line.split()] for line in lines):
        diffs = [seq]

        while not all(x == diffs[-1][0] for x in diffs[-1]):
            diffs.append([y - x for x, y in window(diffs[-1])])

        diffs_list.append(diffs)
    return diffs_list


def part1(diffs_list: list[list[list[int]]]) -> int:
    return sum(sum(x[-1] for x in diffs) for diffs in diffs_list)


def part2(diffs_list: list[list[list[int]]]) -> int:
    _sum = 0
    for diffs in diffs_list:
        sub_sum = diffs[-1][0]
        for i in [diff[0] for diff in diffs[:-1][::-1]]:
            sub_sum = i - sub_sum
        _sum += sub_sum
    return _sum
