
def dfs_re(graph, x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(graph, x - 1, y, n, m)
        dfs(graph, x, y - 1, n, m)
        dfs(graph, x + 1, y, n, m)
        dfs(graph, x, y + 1, n, m)
        return True
    return False

def ice_drink_re(graph, n, m):
    count = 0

    for x in range(n):
        for y in range(m):
            if dfs_re(graph, x, y, n, m):
                count += 1

    return count

def dfs(graph, x, y, n, m):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop(-1)
        if graph[x][y] == 1:
            continue
        graph[x][y] = 1
        if y - 1 >= 0:
            stack.append((x, y - 1))
        if x - 1 >= 0:
            stack.append((x - 1, y))
        if x + 1 < n:
            stack.append((x + 1, y))
        if y + 1 < m:
            stack.append((x, y + 1))

def ice_drink(graph, n, m):
    count = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                dfs(graph, x, y, n, m)
                count += 1
    return count

if __name__ == '__main__':
    
    graph = \
    [
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]

    n, m = 4, 5

    print(ice_drink(graph, n, m))