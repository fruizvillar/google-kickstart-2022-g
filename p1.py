""" Walktober

https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c174f2
"""

DEBUG = False


def test():
    # Read integers M (participants), N (days), and P (John's ID) from the standard input.
    n_participants, n_days, johns_id = map(int, input().split())

    scoreboards = []

    for _ in range(n_participants):
        scoreboards.append(list(map(int, input().split())))

    _print_scoreboards(scoreboards, n_days)

    diff = 0
    for d in range(n_days):
        john = scoreboards[johns_id-1][d]
        max_d = max(scoreboards[i][d] for i in range(n_participants))
        extra = max(0, max_d - john)
        diff += extra

        _print_daily_summary(d, john, max_d, extra)

    print(diff)


def _print_scoreboards(scoreboards, days):
    if DEBUG:
        print()
        print('ID', *(f'Day {d}' for d in range(days)))

        for participant, scores in enumerate(scoreboards):
            print(participant, *scores)


def _print_daily_summary(d, john, max_d, extra):
    if DEBUG:
        print(f'Day {d}: John={john}, max_d={max_d}. Extra={extra}')


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
