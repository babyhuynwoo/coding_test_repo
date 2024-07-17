

def make_one(x):
    if x == 1:
        return 0

    d = [0] * (x + 1)

    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[x]

def make_one_(x, memo=None):
    if memo is None:
        memo = {}

    if x in memo:
        return memo[x]

    if x == 1:
        return 0

    operations = [make_one_(x - 1, memo) + 1]

    if x % 2 == 0:
        operations.append(make_one_(x // 2, memo) + 1)
    if x % 3 == 0:
        operations.append(make_one_(x // 3, memo) + 1)
    if x % 5 == 0:
        operations.append(make_one_(x // 5, memo) + 1)

    memo[x] = min(operations)
    return memo[x]
