
def soldier_ant(stores):
    length = len(stores)
    arr = stores.copy()

    for i in range(length - 2):
        if i + 2 < length:
            arr[i + 2] = max(arr[i] + stores[i + 2], arr[i + 2])
        if i + 3 < length:
            arr[i + 3] = max(arr[i] + stores[i + 3], arr[i + 3])

    return max(arr)

def answer(array):
    n = len(array)

    d = [0] * n

    d[0] = array[0]
    d[1] = max(array[0], array[1]) 
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])


    return d[n - 1]