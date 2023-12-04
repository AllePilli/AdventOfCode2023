import re

from unopt import unwrap

part1_exp_test_result = 13
part1_exp_result = 26914
part2_exp_test_result = 30
part2_exp_result = 13080971

_line_re = r'Card\s+\d+: (.*) \| (.*)'
_card_re = r'Card\s+(\d+).*'


def process_input(lines: list[str]) -> list:
    cards = []
    for line in lines:
        cards.append(
            [int(unwrap(re.match(_card_re, line)).group(1))] + [set(map(lambda y: int(y), re.split(r'\s+', x.strip())))
                                                                for x in unwrap(re.match(_line_re, line)).groups()])

    return cards


def part1(cards: list) -> int:
    _sum = 0
    for _, winning, numbers in cards:
        power = get_matching_amt(winning, numbers)
        if power > 0:
            _sum += 2 ** (power - 1)
    return _sum


def part2(cards: list) -> int:
    copies = {x: 1 for x in range(1, len(cards) + 1)}

    for card_id, winning, numbers in cards:
        matching_amt = get_matching_amt(winning, numbers)
        for i in range(card_id + 1, card_id + matching_amt + 1):
            copies[i] += 1 * copies[card_id]
    return sum(copies.values())


def get_matching_amt(winning, numbers):
    return len(winning & numbers)
