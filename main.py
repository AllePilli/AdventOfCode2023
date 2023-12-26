import os.path
from days import * # do not delete this import !


def get_lines(file_path: str) -> list[str]:
    """
    Returns the lines of a file without the newline characters (\n)
    :param file_path: Path to the file
    :return: List of str representing the lines in the file
    """
    f = open(file_path)
    return [x[:-1] for x in f.readlines()]


if __name__ == '__main__':
    day = 9

    day_module = eval(f'day{day}')

    # if the test inputs for part 1 and 2 are the same, just use one file named
    # 'day{day}_test.txt'. otherwise use 2 separate files for the inputs:
    # 'day{day}_part1_test.txt' and 'day{day}_part2_test.txt'
    if os.path.exists(f'./input/day{day}_test.txt'):
        paths = [
            (f'./input/day{day}_test.txt', f'./input/day{day}.txt'),
            (f'./input/day{day}_test.txt', f'./input/day{day}.txt'),
        ]
    else:
        paths = [
            (f'./input/day{day}_part1_test.txt', f'./input/day{day}.txt'),
            (f'./input/day{day}_part2_test.txt', f'./input/day{day}.txt'),
        ]

    try:
        process_input_func = day_module.process_input
    except AttributeError as e:
        process_input_func = None

    for idx, (test_path, path) in enumerate(paths, start=1):
        try:
            function = eval(f'day_module.part{idx}')

            try:
                test_lines = get_lines(test_path)
                test_input = process_input_func(test_lines) if process_input_func is not None else test_lines
                test_result = function(test_input)
                expected_test_result = eval(f'day_module.part{idx}_exp_test_result')

                assert test_result == expected_test_result, \
                    f"part {idx} failed: expected {expected_test_result}, got {test_result}"

                print(f'Test day {day} part {idx}: {test_result}')
            except FileNotFoundError:
                print(f'!! file not found, path = {test_path}')

            try:
                lines = get_lines(path)
                _input = process_input_func(lines) if process_input_func is not None else lines
                result = function(_input)
                print(f'Solution day {day} part {idx}: {result}')
                expected_result = eval(f'day_module.part{idx}_exp_result')
                assert result == expected_result, \
                    f"part {idx} failed: expected {expected_result}, got {result}"
            except FileNotFoundError:
                print(f'!! file not found, path = {path}')
        except AttributeError as e:
            print(f'!! {e}')
