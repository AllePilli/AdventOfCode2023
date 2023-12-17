from collections import Counter

part1_exp_test_result = 6440
part1_exp_result = 251106089

_card_vals = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1
}


def _line_key(line: str) -> tuple[int, ...]:
    hand = line.split(' ')[0]
    freq = Counter(hand)
    _type = 0

    match sorted(freq.values(), reverse=True):
        case [5]:
            _type = 7
        case [4, 1]:
            _type = 6
        case [3, 2]:
            _type = 5
        case [3, 1, 1]:
            _type = 4
        case [2, 2, 1]:
            _type = 3
        case [2, 1, 1, 1]:
            _type = 2
        case [1, 1, 1, 1, 1]:
            _type = 1

    return tuple(_card_vals[hand[i - 1]] if i > 0 else _type for i in range(len(hand) + 1))


def part1(lines: list[str]) -> int:
    _sum = 0
    for rank, line in enumerate(sorted(lines, key=_line_key), start=1):
        _sum += rank * int(line.split(' ')[1])
    return _sum
