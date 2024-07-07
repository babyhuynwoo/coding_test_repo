import timeit
from memory_profiler import memory_usage
import psutil
import os

def measure_performance(func, *args, **kwargs):
    # Measure memory usage before execution
    mem_before = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    
    # Measure execution time
    execution_time = timeit.timeit(lambda: func(*args, **kwargs), number=1)
    
    # Measure memory usage after execution
    mem_after = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"Memory usage before: {mem_before:.2f} MB")
    print(f"Memory usage after: {mem_after:.2f} MB")
    print(f"Memory used: {mem_after - mem_before:.2f} MB")