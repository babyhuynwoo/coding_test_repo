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

    def test_simple_graph(self):
        N = 3
        M = 2
        start = 1
        graph = {0: {}, 1: {2: 4, 3: 2}, 2: {}, 3: {}}
        expected_output = (2, 4)
        self.assertEqual(telegram(N, M, graph, start), expected_output)

    def test_disconnected_graph(self):
        N = 4
        M = 2
        start = 1
        graph = {0: {}, 1: {2: 4}, 2: {}, 3: {}, 4: {}}
        expected_output = (1, 4)
        self.assertEqual(telegram(N, M, graph, start), expected_output)

    def test_fully_connected_graph(self):
        N = 3
        M = 3
        start = 1
        graph = {0: {}, 1: {2: 1, 3: 2}, 2: {3: 1}, 3: {}}
        expected_output = (2, 2)
        self.assertEqual(telegram(N, M, graph, start), expected_output)

    def test_disconnect_graph(self):
        N = 4
        M = 1
        start = 1
        graph = {0: {}, 1: {4:3}, 2: {}, 3: {}, 4: {}}
        expected_output = (1, 3)
        self.assertEqual(telegram(N, M, graph, start), expected_output)


if __name__ == '__main__':
    unittest.main()