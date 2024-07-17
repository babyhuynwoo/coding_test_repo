import unittest
import timeit
import psutil
import os
from solution import *

class TestMakingDDuck(unittest.TestCase):
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

    def test_exact_cut(self):
        arr = [19, 15, 10, 17]
        M = 6
        self.assertEqual(making(arr, M), 15)

    def test_more_than_required(self):
        arr = [20, 15, 10, 17]
        M = 7
        self.assertEqual(making(arr, M), 15)

    def test_less_than_required(self):
        arr = [19, 15, 10, 17]
        M = 30
        self.assertEqual(making(arr, M), 7)

    def test_all_elements_same(self):
        arr = [10, 10, 10, 10]
        M = 5
        self.assertEqual(making(arr, M), 8)


if __name__ == '__main__':
    unittest.main()