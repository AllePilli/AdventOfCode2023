part1_exp_test_result = 6


def part1(lines: list[str]) -> int:
    dirs = [1 if x == 'R' else 0 for x in lines[0]]
    lines = [x.replace('(', '').replace(')', '') for x in lines[2:]]
    maps = {x: y.split(', ') for x, y in [line.split(' = ') for line in lines]}

    cur = 'AAA'
    steps = 0
    i = 0

    while cur != 'ZZZ':
        cur = maps[cur][dirs[i]]
        i += 1
        steps += 1

        if i >= len(dirs):
            i = 0

    return steps
