from typing import NamedTuple


def window(lt, size=2):
    if len(lt) == 0:
        return None
    if not (isinstance(lt, list) or isinstance(lt, tuple)):
        raise ValueError(f'Cannot window object of type {type(lt)}')

    for i in range(len(lt) - size + 1):
        yield lt[i:i + size]


######################################
# POINT
######################################

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other: 'Point') -> 'Point':
#         return Point(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other: 'Point') -> 'Point':
#         return Point(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other: int) -> 'Point':
#         return Point(self.x * other, self.y * other)
#
#     def __iter__(self):
#         return iter((self.x, self.y))
#
#     def __getitem__(self, idx) -> int:
#         return (self.x, self.y)[idx]
#
#
Point = NamedTuple('Point', [('x', int), ('y', int)])


def add(p: Point, q: Point) -> Point:
    return Point(p.x + q.x, p.y + q.y)


def mul(p: Point, a: int) -> Point:
    return Point(p.x * a, p.y * a)


def sub(p: Point, q: Point) -> Point:
    return Point(p.x - q.x, p.y - q.y)


def manhattan_dist(p: Point, q: Point) -> int:
    return abs(q.x - p.x) + abs(q.y - p.y)


N, E, S, W = Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0)
