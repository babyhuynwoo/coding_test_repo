import unittest
import timeit
import psutil
import os
from solution import *

class TestBigNumberRule(unittest.TestCase):
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

    def test_basic_example(self):
        self.assertEqual(big_number_rule(5, 8, 3, [2, 4, 5, 4, 6]), 46)

    def test_all_same_numbers(self):
        self.assertEqual(big_number_rule(3, 7, 2, [5, 5, 5]), 35)

    def test_max_repetitions(self):
        self.assertEqual(big_number_rule(4, 100, 5, [1, 2, 3, 4]), 396)

if __name__ == '__main__':
    unittest.main()