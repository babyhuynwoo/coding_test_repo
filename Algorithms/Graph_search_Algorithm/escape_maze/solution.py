from collections import deque

def maze_break(graph):
        
    n = len(graph)
    m = len(graph[0])

    queue = deque()
    queue.append([0,0])

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        for _ in move:
            x_ = x + _[0]
            y_ = y + _[1]

            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                continue

            if graph[x_][y_] != 0 and graph[x_][y_] == 1:
                queue.append((x_, y_))
                graph[x_][y_] = graph[x][y] + 1

    return graph[n - 1][m - 1]
            