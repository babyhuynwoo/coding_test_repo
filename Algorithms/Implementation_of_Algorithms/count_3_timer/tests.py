import unittest
import timeit
import psutil
import os
from solution import *

class TestCount3InTimer(unittest.TestCase):
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

    def test_base_case(self):
            self.assertEqual(count_three_in_timer(0), 1575)

    def test_no_three_in_hour(self):
        self.assertEqual(count_three_in_timer(1), 3150)

    def test_three_in_hour(self):
        self.assertEqual(count_three_in_timer(3), 8325)

    def test_double_digit_hour_with_three(self):
        self.assertEqual(count_three_in_timer(13), 26100)

    def test_max_hour(self):
        self.assertEqual(count_three_in_timer(23), 43875)

if __name__ == '__main__':
    unittest.main()