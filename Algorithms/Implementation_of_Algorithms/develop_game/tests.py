import unittest
import timeit
import psutil
import os
from solution import *

class TestDevelopGame(unittest.TestCase):
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

    def test_game_develop_1(self):
        map_info = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]
        x, y, direction = 1, 1, 0
        result = game_develop(map_info, x, y, direction)
        self.assertEqual(result, 3)

    def test_game_develop_2(self):

        map_info = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]
        x, y, direction = 1, 1, 0
        result = game_develop(map_info, x, y, direction)
        self.assertEqual(result, 4)

    def test_game_develop_3(self):
         
        map_info = [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ]
        x, y, direction = 1, 1, 1
        result = game_develop(map_info, x, y, direction)
        self.assertEqual(result, 3)

    def test_game_develop_4(self):
         
        map_info = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        x, y, direction = 2, 2, 0
        result = game_develop(map_info, x, y, direction)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()