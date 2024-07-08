def input_big_number_rule():

    N, M, K = [int(num) for num in input('first input (N, M, K,): ').split(' ')]
    input_ = [int(num) for num in input('second input (N numbers): ').split(' ')]

    return N, M, K, input_

def big_number_rule(N, M, K, input_):

    input_.sort()
    
    return input_[-1] * (M - (M // K)) + input_[-2] * (M // K)