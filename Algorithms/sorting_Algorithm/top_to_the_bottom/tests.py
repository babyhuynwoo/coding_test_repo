import unittest
import timeit
import psutil
import os
from solution import *

class TestTopToTheBottom(unittest.TestCase):
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

    def test_empty_list(self):
        self.assertEqual(top_to_bottom([]), [])
    
    def test_integers(self):
        self.assertEqual(top_to_bottom([1, 3, 2, 4]), [4, 3, 2, 1])
    
    def test_negative_integers(self):
        self.assertEqual(top_to_bottom([-1, -3, -2, -4]), [-1, -2, -3, -4])
    
    def test_mixed_integers(self):
        self.assertEqual(top_to_bottom([1, -3, 2, -4]), [2, 1, -3, -4])
    
    def test_floats(self):
        self.assertEqual(top_to_bottom([1.1, 3.3, 2.2, 4.4]), [4.4, 3.3, 2.2, 1.1])
    
    def test_strings(self):
        self.assertEqual(top_to_bottom(['a', 'c', 'b', 'd']), ['d', 'c', 'b', 'a'])

if __name__ == '__main__':
    unittest.main()