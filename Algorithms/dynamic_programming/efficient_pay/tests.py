import unittest
import timeit
import psutil
import os
from solution import *


class TestEfficientPay(unittest.TestCase):
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
        
    def test_efficient_pay(self):
        self.assertEqual(efficient_pay([1, 2, 5], 11), 3)  # 5+5+1
        self.assertEqual(efficient_pay([2], 3), -1)  # Impossible to make 3 with only 2s
        self.assertEqual(efficient_pay([1, 2, 5], 0), 0)  # No coins needed for 0
        self.assertEqual(efficient_pay([], 10), -1)  # No coins available
        self.assertEqual(efficient_pay([1, 3, 4], 6), 2)  # 3+3


if __name__ == '__main__':
    unittest.main()