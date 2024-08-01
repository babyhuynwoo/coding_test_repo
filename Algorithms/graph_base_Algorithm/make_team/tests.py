import unittest
from unittest.mock import patch
from io import StringIO
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
        
    def test_find_perent(self):
        parent = [0, 1, 2, 3, 4, 5]
        self.assertEqual(find_perent(parent, 3), 3)
        parent[3] = 2
        self.assertEqual(find_perent(parent, 3), 2)
        parent[2] = 1
        self.assertEqual(find_perent(parent, 3), 1)

    def test_union(self):
        parent = [0, 1, 2, 3, 4, 5]
        union(parent, 1, 2)
        self.assertEqual(find_perent(parent, 2), 1)
        union(parent, 2, 3)
        self.assertEqual(find_perent(parent, 3), 1)
        union(parent, 4, 5)
        self.assertEqual(find_perent(parent, 5), 4)
        union(parent, 1, 5)
        self.assertEqual(find_perent(parent, 5), 1)

    @patch('builtins.input', side_effect=[
        '5 4',  # N, M
        '0 1 2',  # union(1, 2)
        '0 2 3',  # union(2, 3)
        '1 1 3',  # check if 1 and 3 are in the same set
        '1 1 4'   # check if 1 and 4 are in the same set
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_input(self, mock_stdout, mock_input):
        get_input()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertEqual(output, ['YES', 'NO'])

if __name__ == '__main__':
    unittest.main()