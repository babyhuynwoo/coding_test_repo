import unittest
import timeit
import psutil
import os
from solution import *

class TestUntilOneAdvance(unittest.TestCase):
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

    def test_example_cases(self):
        # N을 1로 만드는 기본적인 경우 테스트
        self.assertEqual(until_one_advance(25, 5), 2)  # 25 -> 5 -> 1
        self.assertEqual(until_one_advance(10, 2), 4)  # 10 -> 5 -> 4 -> 2 -> 1
        self.assertEqual(until_one_advance(100, 10), 2)  # 100 -> 10 -> 1

    def test_edge_cases(self):
        # N이 K보다 작은 경우와 N이 K로 나누어떨어지지 않는 경우 테스트
        self.assertEqual(until_one_advance(1, 10), 0)  # 이미 1
        self.assertEqual(until_one_advance(15, 4), 6)  # 15 -> 11 -> 10 -> 5 -> 4 -> 2 -> 1

if __name__ == '__main__':
    unittest.main()