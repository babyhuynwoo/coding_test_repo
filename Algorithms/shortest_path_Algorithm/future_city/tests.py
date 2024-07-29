import unittest
import timeit
import psutil
import os
from solution import *

class TestFutureCity(unittest.TestCase):
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

    def test_future_city(self):
        edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
        self.assertEqual(future_city(5, 4, edges), 3)

    def test_answer(self):
        n = 5
        x = 5
        graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            graph[i][i] = 0
        edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
        for u, v in edges:
            graph[u][v] = 1
            graph[v][u] = 1
        self.assertEqual(answer(n, x, graph), 3)

if __name__ == '__main__':
    unittest.main()