from days import * # do not delete this import !


def get_lines(path: str) -> list[str]:
    """
    Returns the lines of a file without the newline characters (\n)
    :param path: Path to the file
    :return: List of str representing the lines in the file
    """
    f = open(path)
    return [x[:-1] for x in f.readlines()]


if __name__ == '__main__':
    day = 2

    day_module = eval(f'day{day}')
    paths = [
        (f'./input/day{day}_part1_test.txt', f'./input/day{day}.txt'),
        (f'./input/day{day}_part2_test.txt', f'./input/day{day}.txt'),
    ]

    for idx, (test_path, path) in enumerate(paths, start=1):
        try:
            function = eval(f'day_module.part{idx}')

            try:
                test_result = function(get_lines(test_path))
                expected_test_result = eval(f'day_module.part{idx}_exp_test_result')

                assert test_result == expected_test_result, \
                    f"part {idx} failed: expected {expected_test_result}, got {test_result}"

                print(f'Test day {day} part {idx}: {test_result}')
            except FileNotFoundError:
                print(f'!! file not found, path = {test_path}')

            try:
                result = function(get_lines(path))
                print(f'Solution day {day} part {idx}: {result}')
                expected_result = eval(f'day_module.part{idx}_exp_result')
                assert result == expected_result, \
                    f"part {idx} failed: expected {expected_result}, got {result}"
            except FileNotFoundError:
                print(f'!! file not found, path = {path}')
        except AttributeError as e:
            print(f'!! {e}')
