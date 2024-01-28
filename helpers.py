from typing import NamedTuple, Callable, TypeVar

import numpy as np

_T = TypeVar('_T')


def window(lt, size=2):
    if len(lt) == 0:
        return None
    if not (isinstance(lt, list) or isinstance(lt, tuple)):
        raise ValueError(f'Cannot window object of type {type(lt)}')

    for i in range(len(lt) - size + 1):
        yield lt[i:i + size]


def transpose(lst: list) -> list:
    return np.array(lst).T.tolist()


def split(lst: list[_T], el: _T) -> list[list[_T]]:
    arr = np.array(lst)
    idx = np.where(arr == el)[0]
    sub_arrays = np.split(arr, idx + 1)
    return [sub_array.tolist()[:-1] if i < len(sub_arrays) - 1 else sub_array.tolist()
            for i, sub_array in enumerate(sub_arrays) if len(sub_array) > 0]


######################################
# POINT
######################################
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
