from collections import Counter

part1_exp_test_result = 6440
part1_exp_result = 251106089
part2_exp_test_result = 5905


def _get_type(hand: str) -> int:
    freq = Counter(hand)
    return ([1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 1, 3], [2, 3], [1, 4], [5]).index(sorted(freq.values()))


def _hand_score(hand: str) -> tuple[int, ...]:
    _type = _get_type(hand)
    hand_score = ['23456789TJQKA'.index(x) for x in hand]
    return _type, *hand_score


def hand(h, part1):
    if part1:
        h = h.replace('J', 'X')
    h2 = ['J23456789TXQKA'.index(i) for i in h]
    ts = []
    for r in '23456789TQKA':
        c = Counter(h.replace('J', r))
        p = tuple(sorted(c.values()))
        t = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)].index(p)
        ts.append(t)
    return (max(ts), *h2)


def part1(lines: list[str]) -> int:
    _sum = 0
    hands = [x.split() for x in lines]
    for rank, line in enumerate(sorted(hands, key=lambda x: _hand_score(x[0])), start=1):
        _sum += rank * int(line[1])
    return _sum


def part2(lines: list[str]) -> int:
    h = sorted((hand(h, False), int(b)) for h, b in (l.split() for l in lines))
    t = 0
    for i, (_, b) in enumerate(h):
        t += i * b + b
    return t
