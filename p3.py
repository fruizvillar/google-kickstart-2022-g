""" Happy Subarrays

https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17491"""

import numpy as np


DEBUG = False


def test():
    # Read integers Rs (stone radius) and Rh (Home radius) from the standard input.

    len_array = int(input())

    array_x = np.array(list(map(int, input().split())))

    cumsums = array_x.cumsum()

    if DEBUG:
        print()

    sum_happy_sub_arrays = 0

    for idx_0 in range(len_array):

        if np.any(cumsums < 0):
            last_happy_pos = np.argmax(cumsums < 0) - 1
            if last_happy_pos >= 0:
                subarray_partial_sum = sum(cumsums[:last_happy_pos+1])
                sum_happy_sub_arrays += subarray_partial_sum
        else:
            # all unhappy!
            sum_happy_sub_arrays += sum(cumsums)

        cumsums = cumsums[1:] - cumsums[0]

    print(sum_happy_sub_arrays)


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
