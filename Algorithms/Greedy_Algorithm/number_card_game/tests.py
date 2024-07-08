import unittest
import timeit
import psutil
import os
from solution import *

class TestNumberCardGame(unittest.TestCase):
    def setUp(self):
        # 테스트 시작 전 메모리 사용량 측정
        self.mem_before = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        self.start_time = timeit.default_timer()

    def tearDown(self):
        # 테스트 종료 후 메모리 사용량 및 실행 시간 측정
        self.mem_after = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        self.execution_time = timeit.default_timer() - self.start_time
        print()
        print(f'{self.id()}')
        print()
        print(f"Execution time: {self.execution_time:.6f} seconds")
        print(f"Memory usage before: {self.mem_before:.2f} MB")
        print(f"Memory usage after: {self.mem_after:.2f} MB")
        print(f"Memory used: {self.mem_after - self.mem_before:.2f} MB")
        print()

    def test_empty_matrix(self):
        self.assertEqual(number_card_game(0, 0, []), 0)

    def test_single_row_matrix(self):
        self.assertEqual(number_card_game(1, 3, [[3, 1, 2]]), 1)

    def test_multiple_rows_matrix(self):
        self.assertEqual(number_card_game(3, 4, [[3, 1, 2, 4], [4, 2, 4, 2], [4, 9 , 10, 3]]), 3)

    def test_all_equal_values(self):
        self.assertEqual(number_card_game(2, 2, [[2, 2], [2, 2]]), 2)


if __name__ == '__main__':
    unittest.main()