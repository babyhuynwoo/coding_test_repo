

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

    start_node = 1

    stack = []
    stack.append(start_node)
    visited = [False for _ in range(len(graph))]
    visited[start_node] = True

    log = []
    log.append(start_node)

    while len(stack) != 0:
        flag = False

        for node in graph[stack[-1]]:
            if visited[node] == False:
                visited[node] = True
                log.append(node)
                stack.append(node)
                flag = True
                break
        
        if flag == False:
            stack.pop()

    print("DFS 방문 순서:", log)