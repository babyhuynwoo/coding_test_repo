
def making(arr, M):
    start = 0
    end = max(arr)
    answer = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for x in arr:
            if x > mid:
                total += x - mid

        if total < M:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid

    return answer


import random
import time

if __name__ == "__main__":
    sample = [random.randint(1, 1000000000) for _ in range(1000000)]
    M = random.randint(1, 100000000)

    start_time = time.time()
    result = making(sample, M)
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution Time: {end_time - start_time} seconds")