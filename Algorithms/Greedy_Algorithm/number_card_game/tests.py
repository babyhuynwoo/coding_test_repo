from solution import *

def test():
    pass

if __name__ == '__main__':
    N, M, matrix = input_number_card_game()

    print()
    print('result:',number_card_game(N, M, matrix))
    print()
    print('Performance measurement')
    print()
    measure_performance(number_card_game, N, M, matrix)