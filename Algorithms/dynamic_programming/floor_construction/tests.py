import unittest
import timeit
import psutil
import os
from solution import *

class TestTilePlacement(unittest.TestCase):
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

    def test_simple_case(self):
        self.assertEqual(tile_place_bt(3), tile_place_memo(3))
        self.assertEqual(tile_place_bt(3), answer(3))
        self.assertEqual(tile_place_bt(4), tile_place_memo(4))
        self.assertEqual(tile_place_bt(4), answer(4))
        self.assertEqual(tile_place_bt(5), tile_place_memo(5))
        self.assertEqual(tile_place_bt(5), answer(5))
    
    def test_large_case(self):
        self.assertEqual(tile_place_bt(1000), tile_place_memo(1000))
        self.assertEqual(tile_place_bt(1000), answer(1000))
        self.assertEqual(tile_place_bt(10000), tile_place_memo(10000))
        self.assertEqual(tile_place_bt(10000), answer(10000))


if __name__ == '__main__':
    unittest.main()