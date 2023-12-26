from math import lcm

part1_exp_test_result = 6
part1_exp_result = 13301
part2_exp_test_result = 6
part2_exp_result = 7309459565207


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


def part2(lines: list[str]) -> int:
    dirs = [1 if x == 'R' else 0 for x in lines[0]]
    lines = [x.replace('(', '').replace(')', '') for x in lines[2:]]
    maps = {x: y.split(', ') for x, y in [line.split(' = ') for line in lines]}

    cur = [x for x in maps.keys() if x[-1] == 'A']
    i = 0
    periods = [(False, [(c, 0)]) for c in cur]

    while not all(x for x, _ in periods):
        cur = [maps[x][dirs[i]] for x in cur]

        for idx, (found, period_states) in enumerate(periods):
            if not found:
                if (cur[idx], i) in period_states:
                    prev_idx = period_states.index((cur[idx], i))
                    periods[idx] = (True, period_states[prev_idx:])
                else:
                    periods[idx] = (False, period_states + [(cur[idx], i)])

        i += 1

        if i >= len(dirs):
            i = 0

    return lcm(*[len(x) for _, x in periods])
