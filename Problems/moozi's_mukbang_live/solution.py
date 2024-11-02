

def func(array, k):

    length = len(array)

    if length == k:
        for i in range(length):
            if array[i] != 1:
                return i + 1 
        return -1
    elif length > k:
        return k + 1
    else:
        times = 0
        i = 0
        while True:
            
            if times >= k:
                break
            
            if i >= length:
                i = i % length
            
            if array[i] == 0:
                i += 1
                continue
            else:
                array[i] -= 1
                i += 1
                times += 1
    return find_next(array, length, times)
            
def find_next(array, length, index):

    next = index

    while True:
        if next >= length:
            next %=length

        if array[next] != 0:
            return next + 1
        else:
            next += 1

        if next == index:
            break

    return -1

if __name__ == "__main__":
    
    food_time_1 = [3, 1, 2]
    food_time_2 = [3, 1, 2, 5, 6 ,2 ,1, 3]
    food_time_3 = [2, 1, 3, 5, 7]
    food_time_4 = [4, 3, 3, 6, 7, 5, 5, 8]
    
    print(func(food_time_1, 5))
    print(func(food_time_2, 8))
    print(func(food_time_3, 12))
    print(func(food_time_4, 12))



