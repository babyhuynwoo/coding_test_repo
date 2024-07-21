
def bug_efficient_pay(coins, M):

    coins = sorted(coins)

    count = 0

    for _ in range(len(coins)-1, 0, -1):
        cur = coins[_]
        if _ != 0:
            next = coins[_-1]
        else:
            next = 0

        while M >= cur:
            if M - cur < next:
                break

            __ = (M // cur)
            count += __
            M -= (cur * __)

    if M > 0:
        return -1
    else:
        return count

def efficient_pay(array, m):
    n = len(array)
    d = [10001] * (m + 1)

    d[0] = 0
    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array[i]] + 1)

    if d[m] == 10001:
        return -1
    else:
        return d[m]    
