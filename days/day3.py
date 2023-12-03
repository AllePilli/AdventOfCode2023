from collections import namedtuple

part1_exp_test_result = 4361
part1_exp_result = 536202

_Point = namedtuple('_Point', ['x', 'y'])


class _Token:
    def __init__(self, position: _Point, value: str):
        self.position = position
        self.value = value

    def __repr__(self):
        return f"Token({self.position}, {self.value})"


def tokenize(lines: list[str]) -> list[_Token]:
    tokens: list[_Token] = []

    def get_int_str(p: _Point) -> str:
        line = lines[p.y]
        x = p.x
        num = ''

        while x < len(line) and line[x].isdigit():
            num += line[x]
            x += 1

        return num

    for y, line in enumerate(lines):
        x = 0
        while x < len(line):
            if line[x].isdigit():
                position = _Point(x, y)
                tokens.append(_Token(position, get_int_str(position)))
                x += len(tokens[-1].value)
            else:
                x += 1
    return tokens


def part1(lines: list[str]) -> int:
    _sum = 0

    for token in tokenize(lines):
        x, y = token.position
        edges = []

        if y > 1:
            edges.extend(
                [_Point(ix, y - 1) for ix in range(x - 1, x + len(token.value) + 1) if ix in range(len(lines[y - 1]))]
            )

        if x > 0:
            edges.append(_Point(x - 1, y))
        if x + len(token.value) < len(lines[y]):
            edges.append(_Point(x + len(token.value), y))

        if y + 1 < len(lines):
            edges.extend(
                [_Point(ix, y + 1) for ix in range(x - 1, x + len(token.value) + 1) if ix in range(len(lines[y + 1]))]
            )

        if any(lines[iy][ix] != '.' and not lines[iy][ix].isdigit() for ix, iy in edges):
            _sum += int(token.value)

    return _sum
