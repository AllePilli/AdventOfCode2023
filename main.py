import os.path
import pathlib
from typing import Callable

from days import *  # do not delete this import !


def get_lines(file_path: str | pathlib.Path) -> list[str]:
    """
    Returns the lines of a file without the newline characters (\n)
    :param file_path: Path to the file
    :return: List of str representing the lines in the file
    """
    f = open(file_path)
    return [x[:-1] for x in f.readlines()]


def get_process_input_func(day: int) -> Callable[[list[str]], object] | None:
    try:
        return eval(f'day{day}').process_input
    except AttributeError:
        return None


def test_day(day: int, part: int):
    def perform_test(lines, process_input_func, function, expected_result, test: int | None = None):
        _input = process_input_func(lines) if process_input_func is not None else lines
        result = function(_input)

        if test is None:
            assert result == expected_result, f'part {part} failed: expected {expected_result}, got {result}'
            print(f'Test day {day} part {part}: {result}')
        else:
            assert result == expected_result, f'part {part} test {test} failed: expected {expected_result}, got {result}'
            print(f'Test day {day} part {part} test {test}: {result}')

    day_module = eval(f'day{day}')

    # if the test inputs for part 1 and 2 are the same, just use one file named
    # 'day{day}_test.txt'. otherwise use 2 separate files for the inputs:
    # 'day{day}_part1_test.txt' and 'day{day}_part2_test.txt'
    #
    # There could also be multiple test files for a single part, their filenames should look like:
    # 'day{day}_part1_test1.txt' and 'day{day}_part1_test2.txt' and ...
    path: list[pathlib.Path] | str = ""
    if os.path.exists(f'./input/day{day}_test.txt'):
        path = f'./input/day{day}_test.txt'
    elif os.path.exists(f'./input/day{day}_part{part}_test.txt'):
        path = f'./input/day{day}_part{part}_test.txt'
    elif os.path.exists(f'./input/day{day}_part{part}_test1.txt'):
        path = [f for f in pathlib.Path("./input").glob(f"day{day}_part{part}_test[1-9].txt")]
    else:
        print(f'No test file found for day {day} part {part}')
        return

    process_input_func = get_process_input_func(day)
    try:
        function = eval(f'day_module.part{part}')
    except AttributeError as e:
        print(f'!! {e}')
        return

    try:
        expected_result = eval(f'day_module.part{part}_exp_test_result')
    except AttributeError as e:
        print(f'!! {e}')
        return

    if isinstance(path, list):
        assert isinstance(expected_result, tuple), f"expected result for day {day} part {part} should be a tuple"
        assert len(expected_result) == len(
            path), f"The number of expected results and test files for day {day} part {part} do not match"

        for i, p in enumerate(path):
            perform_test(get_lines(p), process_input_func, function, expected_result[i], test=i + 1)
    else:
        perform_test(get_lines(path), process_input_func, function, expected_result)


def solve_day(day: int, part: int):
    day_module = eval(f'day{day}')
    path = f'./input/day{day}.txt'
    process_input_func = get_process_input_func(day)

    try:
        function = eval(f'day_module.part{part}')
    except AttributeError as e:
        print(f'!! {e}')
        return

    try:
        lines = get_lines(path)
    except FileNotFoundError:
        print(f'File not found, path = {path}')
        return

    _input = process_input_func(lines) if process_input_func is not None else lines
    result = function(_input)

    print(f'Solution day {day} part {part}: {result}')

    try:
        expected_result = eval(f'day_module.part{part}_exp_result')
    except AttributeError as e:
        print(f'!! {e}')
        return

    assert result == expected_result, f"part {part} failed: expected {expected_result}, got {result}"


if __name__ == '__main__':
    day = 13

    for part in (1, 2):
        test_day(day, part)
        solve_day(day, part)
