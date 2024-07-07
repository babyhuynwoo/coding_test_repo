from solution import *

def test():
    pass

if __name__ == '__main__':

    N, M, K, input_ = input_big_number_rule()
    
    print()
    print('result',big_number_rule(N, M, K, input_))
    print()
    print('Performance measurement')
    print()
    measure_performance(big_number_rule, N, M, K, input_)