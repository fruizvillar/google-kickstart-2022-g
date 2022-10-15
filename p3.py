""" Happy Subarrays

https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17491"""

DEBUG = False


def test():
    # Read integers Rs (stone radius) and Rh (Home radius) from the standard input.

    len_array = int(input())
    sum_happy_sub_arrays = 0

    array_x = list(map(int, input().split()))

    if DEBUG:
        print()

    for idx_0 in range(len_array):
        subarray_partial_sum = 0
        for k in range(idx_0, len_array):
            subarray_partial_sum += array_x[k]

            if subarray_partial_sum >= 0:
                # A happy one!
                sum_happy_sub_arrays += subarray_partial_sum
                happy = True
            else:
                happy = False

            if DEBUG:
                print(f'Subarray: {idx_0}-{k}. Sum={subarray_partial_sum} happy=({happy}). Acc={sum_happy_sub_arrays}.'
                      f'  {array_x[idx_0:k+1]}')

            if not happy:
                break  # Unhappiness won't be forgotten

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
