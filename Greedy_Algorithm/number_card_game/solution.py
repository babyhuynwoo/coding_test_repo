import sys

sys.path.append('..')

from measure_limits import *

def input_number_card_game():
    
    N, M = [int(_) for _ in input('first input (N, M): ').split()]

    matrix = []

    for row in range(N):
        matrix.append([int(_) for _ in input(f'input {(row)} row values: ').split()])
    
    return N, M, matrix

def number_card_game(N, M, input_):

    result = 0

    for i in range(N):
        result = max(result, min(input_[i]))

    return result
