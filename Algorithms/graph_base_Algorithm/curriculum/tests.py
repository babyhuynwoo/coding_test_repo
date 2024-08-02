import unittest
from unittest.mock import patch
import timeit
import psutil
import os
from solution import *


class TestCurriculum(unittest.TestCase):
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
        
    def test_no_lectures(self):
        self.assertEqual(my_curriculum_3(0), {})

    def test_single_lecture(self):
        with patch('builtins.input', return_value='10 -1'):
            self.assertEqual(my_curriculum_3(1), {1: 10})

    def test_multiple_lectures_no_prerequisites(self):
        inputs = iter(['10 -1', '20 -1', '30 -1'])
        with patch('builtins.input', lambda _: next(inputs)):
            self.assertEqual(my_curriculum_3(3), {1: 10, 2: 20, 3: 30})

    def test_multiple_lectures_with_prerequisites(self):
        inputs = iter(['10 2 -1', '20 3 -1', '30 -1'])
        with patch('builtins.input', lambda _: next(inputs)):
            self.assertEqual(my_curriculum_3(3), {1: 60, 2: 50, 3: 30})


if __name__ == '__main__':
    unittest.main()