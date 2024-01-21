import itertools
from collections import OrderedDict

part1_exp_test_result = 21
part1_exp_result = 8075
part2_exp_test_result = 525152
part2_exp_result = 4232520187524


def part1(lines: list[str]) -> int:
    return sum(
        _StateMachine([int(x) for x in conf.split(',')], springs).reaches_end()
        for springs, conf in [line.split() for line in lines]
    )


def part2(lines: list[str]) -> int:
    cnt = 0
    for springs, conf in [line.split() for line in lines]:
        config = [int(x) for x in conf.split(',')]

        unfolded_springs = '?'.join([springs] * 5)
        unfolded_config = config * 5

        state_machine = _StateMachine(unfolded_config, unfolded_springs)
        cnt += state_machine.reaches_end()

    return cnt


class _StateMachine:
    def __init__(self, config: list[int], line: str):
        self.line = line
        state_cnt = sum(x + 1 for x in config) + 1
        state_names = [str(y) for y in range(state_cnt)]
        self.states = {
            state_names[0]: {'.': state_names[0], '#': state_names[1]},
        }

        curr_state_idx = 1

        for seq_len in config:
            for _ in range(seq_len - 1):
                self.states[state_names[curr_state_idx]] = {'#': state_names[curr_state_idx + 1]}
                curr_state_idx += 1
            self.states[state_names[curr_state_idx]] = {'.': state_names[curr_state_idx + 1]}
            curr_state_idx += 1

            if curr_state_idx == state_cnt - 1:
                self.states[state_names[curr_state_idx]] = {'.': state_names[curr_state_idx]}
            else:
                self.states[state_names[curr_state_idx]] = {'.': state_names[curr_state_idx],
                                                            '#': state_names[curr_state_idx + 1]}
            curr_state_idx += 1

        self.curr_state = state_names[0]
        self.heads = {state_names[0]: 1}

    def reaches_end(self) -> int:
        heads = OrderedDict(self.heads)
        for i, c in enumerate(self.line):
            next_heads: OrderedDict[str, int] = OrderedDict()

            def step(char: str):
                for state, amt in heads.items():
                    mapping = self.states[state]
                    if char not in mapping.keys():
                        continue

                    if mapping[char] in next_heads.keys():
                        next_heads[mapping[char]] += amt
                    else:
                        next_heads[mapping[char]] = amt

            if c in '.#':
                step(c)
            else:
                for x in '.#':
                    step(x)

            heads = next_heads.copy()

        last_states = sorted(self.states.keys(), key=int)[-2:]
        return sum(heads[x] for x in last_states if x in heads.keys())
