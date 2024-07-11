
import random


if __name__ == '__main__':
    
    random_list = [random.randint(0, 100) for i in range(10)]

    print(random_list)

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    print(quick_sort(random_list))