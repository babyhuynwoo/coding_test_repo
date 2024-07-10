from collections import deque

if __name__ == '__main__':

    graph = \
    [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    visited = [False for _ in range(len(graph))]

    start_node = 1

    queue = deque()
    queue.append(start_node)

    visited[start_node] = True

    log = []
    log.append(start_node)

    while len(queue) != 0:
        for node in graph[queue.popleft()]:
            if visited[node] == False:
                queue.append(node)
                log.append(node)
                visited[node] = True
            else:
                continue

    print("BFS 방문 순서:", log)