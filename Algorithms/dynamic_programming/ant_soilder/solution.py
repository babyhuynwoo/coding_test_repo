
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

def my_answer(stores):
    # 실행시간 면에서 이득 
    length = len(stores)

    dp = stores.copy()
    dp[2] += dp[0]

    for i in range(3, length):
        dp[i] = max(dp[i] + dp[i-3], dp[i] + dp[i-2])

    return max(dp[-1], dp[-2])

def my_answer(stores):
    # 메모리 면에서 이득
    length = len(stores)

    stores[2] += stores[0] 

    for i in range(3, length):
        stores[i] = max(stores[i] + stores[i-3], stores[i] + stores[i-2])

    max_value = max(stores[-1], stores[-2])

    return max_value
