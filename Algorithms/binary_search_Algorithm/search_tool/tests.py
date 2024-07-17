import unittest
import timeit
import psutil
import os
from solution import *

class TestSearchTool(unittest.TestCase):
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
        
    def test_search_tool(self):
        # Test case 1
        repo = {1, 2, 3, 4, 5}
        request = [1, 2, 6]
        expected = ['yes', 'yes', 'no']
        self.assertEqual(search_tool(repo, request), expected)

        # Test case 2
        repo = {10, 20, 30, 40, 50}
        request = [10, 25, 50]
        expected = ['yes', 'no', 'yes']
        self.assertEqual(search_tool(repo, request), expected)

        # Test case 3
        repo = {100, 200, 300}
        request = [150, 200, 250]
        expected = ['no', 'yes', 'no']
        self.assertEqual(search_tool(repo, request), expected)

        # Test case 4
        repo = set()
        request = [1, 2, 3]
        expected = ['no', 'no', 'no']
        self.assertEqual(search_tool(repo, request), expected)

        # Test case 5
        repo = {1, 2, 3}
        request = []
        expected = []
        self.assertEqual(search_tool(repo, request), expected)

if __name__ == '__main__':
    unittest.main()