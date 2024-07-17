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

    def test_make_one(self):
        self.assertEqual(make_one(1), 0)
        self.assertEqual(make_one(2), 1)
        self.assertEqual(make_one(3), 1)
        self.assertEqual(make_one(4), 2)
        self.assertEqual(make_one(5), 1)
        self.assertEqual(make_one(26), 3)
        self.assertEqual(make_one(10), 2)
        self.assertEqual(make_one(87), 6)

    def test_make_one_(self):
        self.assertEqual(make_one_(1), 0)
        self.assertEqual(make_one_(2), 1)
        self.assertEqual(make_one_(3), 1)
        self.assertEqual(make_one_(4), 2)
        self.assertEqual(make_one_(5), 1)
        self.assertEqual(make_one_(10), 2)
        self.assertEqual(make_one_(26), 3)
        self.assertEqual(make_one_(87), 6)


if __name__ == '__main__':
    unittest.main()