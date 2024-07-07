from solution import *

def test():
    pass


if __name__ == '__main__':
    N, K = input_until_one()

    """

    first input (N, K): 89423 46

    result: 99

    Performance measurement

    Execution time: 0.000005 seconds
    Memory usage before: 24.81 MB
    Memory usage after: 24.83 MB
    Memory used: 0.02 MB

    """

    print()
    print('result:',until_one_advance(N, K))
    print()
    print('Performance measurement')
    print()
    measure_performance(until_one_advance, N, K)

    """

    first input (N, K): 89423 46

    result: 99

    Performance measurement

    Execution time: 0.000010 seconds
    Memory usage before: 25.15 MB
    Memory usage after: 25.17 MB
    Memory used: 0.02 MB

    """

    print()
    print('result:',until_one(N, K))
    print()
    print('Performance measurement')
    print()
    measure_performance(until_one, N, K)