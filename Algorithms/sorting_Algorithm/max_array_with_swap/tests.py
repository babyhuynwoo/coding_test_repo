import unittest
import timeit
import psutil
import os
from solution import *

class TestSwapArray(unittest.TestCase):
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

    def test_basic_functionality(self):
        arr_1 = [1, 2, 5, 4, 3]
        arr_2 = [5, 5, 6, 6, 5]
        self.assertEqual(swap_array(arr_1, arr_2, 3), 26)

    def test_no_swaps_needed(self): 
        arr_1 = [5, 6, 7]
        arr_2 = [1, 2, 3]
        self.assertEqual(swap_array(arr_1, arr_2, 2), 18)

    def test_all_elements_swapped(self):
        arr_1 = [1, 2, 3]
        arr_2 = [7, 8, 9]
        self.assertEqual(swap_array(arr_1, arr_2, 3), 24)

    def test_k_zero(self):
        arr_1 = [1, 2, 3]
        arr_2 = [4, 5, 6]
        self.assertEqual(swap_array(arr_1, arr_2, 0), 6)

if __name__ == '__main__':
    unittest.main()