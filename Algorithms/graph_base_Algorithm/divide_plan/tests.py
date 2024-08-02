import unittest
from unittest.mock import patch
import timeit
import psutil
import os
from solution import *


class TestDivideTown(unittest.TestCase):
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
        
    def test_find_parent(self):
        parent = [0, 1, 2, 3, 4]
        self.assertEqual(find_parent(parent, 3), 3)
        parent[3] = 2
        self.assertEqual(find_parent(parent, 3), 2)
        parent[2] = 1
        self.assertEqual(find_parent(parent, 3), 1)

    def test_union(self):
        parent = [0, 1, 2, 3, 4]
        self.assertTrue(union(parent, 1, 2))
        self.assertEqual(parent[2], 1)
        self.assertTrue(union(parent, 2, 3))
        self.assertEqual(parent[3], 1)
        self.assertFalse(union(parent, 1, 3))

    @patch('builtins.input', side_effect=['4 4', '1 2 3', '2 3 2', '3 4 4', '4 1 1'])
    def test_divide_plan(self, mock_input):
        result = divide_plan()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()