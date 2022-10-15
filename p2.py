""" Curling

https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17c82
"""
import math
from enum import Enum

DEBUG = False


class Team(Enum):
    RED = 'r'
    YELLOW = 'y'


class Stone:

    def __init__(self, xy_str, team: Team):

        self.x, self.y = map(int, xy_str.split())
        self.team = team
        self._d = None

    @property
    def d(self):
        if self._d is None:
            self._d = math.sqrt(self.x ** 2 + self.y ** 2)
        return self._d

    def __lt__(self, other):
        return self.d < other.d

    def __repr__(self):
        return f'({self.x}, {self.y}) |{self.team}| {self.d}'


def test():
    # Read integers Rs (stone radius) and Rh (Home radius) from the standard input.
    r_stone, r_home = map(int, input().split())

    stones = _read_stones()

    stones = sorted(filter(lambda si: _stone_is_in_home(r_home, r_stone, si), stones))

    try:
        winner_team = stones[0].team
    except IndexError:
        # Lol to this corner case :)
        print(0, 0)
        return

    score_winner = 0

    for s in stones:

        if s.team != winner_team:  # We don't even count 1st one of other team
            break

        score_winner += 1

    score_red = score_winner if winner_team == Team.RED else 0
    score_yel = score_winner if winner_team == Team.YELLOW else 0
    print(score_red, score_yel)


def _read_stones():
    stones = []
    for t in Team:
        n_stones = int(input())
        stones.extend([Stone(input(), t) for _ in range(n_stones)])
    # _print_stones(stones)
    return stones


def _stone_is_in_home(r_home, r_stone, stone):
    is_in = stone.d - r_stone <= r_home
    return is_in


def _print_stones(stones):
    if DEBUG:
        print(*stones)


def main():
    t = int(input())
    # Loop over the number of test cases.
    for test_no in range(1, t + 1):
        # Print case number
        print("Case #%d:" % test_no, end=" ")
        # and solve each test.
        test()


if __name__ == '__main__':
    main()
