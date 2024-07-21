import unittest
import timeit
import psutil
import os
from solution import *
import random


class TestAntSoldier(unittest.TestCase):
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

    def test_example_cases(self):
        # 기본적인 경우 테스트
        self.assertEqual(soldier_ant([1, 2, 3, 4, 5]), answer([1, 2, 3, 4, 5]))
        self.assertEqual(soldier_ant([10, 20, 30, 40, 50]), answer([10, 20, 30, 40, 50]))
        self.assertEqual(soldier_ant([5, 5, 10, 100, 10, 5]), answer([5, 5, 10, 100, 10, 5]))

    def test_edge_cases(self):
        # 경계 조건 테스트
        self.assertEqual(soldier_ant([3, 2, 5, 10, 7]), answer([3, 2, 5, 10, 7]))
        self.assertEqual(soldier_ant([3, 2, 7, 10]), answer([3, 2, 7, 10]))
        self.assertEqual(soldier_ant([3, 2, 5, 10, 7, 8]), answer([3, 2, 5, 10, 7, 8]))

    def test_large_cases(self):
        # 대규모 데이터 테스트
        sample = [random.randint(1, 1000) for _ in range(100000)]
        self.assertEqual(soldier_ant(sample), answer(sample))
        self.assertEqual(my_answer(sample), answer(sample))
        sample = [random.randint(1, 10000) for _ in range(1000000)]
        self.assertEqual(soldier_ant(sample), answer(sample))
        self.assertEqual(my_answer(sample), answer(sample))

    def test_my_answer_example_cases(self):
        self.assertEqual(my_answer([1, 2, 3, 4, 5]), answer([1, 2, 3, 4, 5]))
        self.assertEqual(my_answer([10, 20, 30, 40, 50]), answer([10, 20, 30, 40, 50]))
        self.assertEqual(my_answer([5, 5, 10, 100, 10, 5]), answer([5, 5, 10, 100, 10, 5]))


if __name__ == '__main__':
    unittest.main()