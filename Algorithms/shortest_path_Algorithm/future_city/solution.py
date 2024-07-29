from collections import defaultdict, deque

def future_city(X, K, edges):

    shortest_way = bfs_shortest_path(edges, 1, K) + bfs_shortest_path(edges, K, X)

    return shortest_way        

def bfs_shortest_path(graph, start, end):
    if start == end:
        return 0

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        current_node, distance = queue.popleft()
        
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in graph[current_node]:
                if neighbor == end:
                    return distance + 1
                else:
                    queue.append((neighbor, distance + 1))
    
    return -1

def get_input():
    N, M = [int(_) for _ in input('input N, M').split()]

    edges = defaultdict(set)

    for _ in range(1, M+1):
        tmp = [int(num) for num in input('input edge: ').split()]
        edges[tmp[0]].add(tmp[1])
        edges[tmp[1]].add(tmp[0])

    tmp = [int(num) for num in input('input X, K: ').split()]
    X, K = tmp

    for _ in edges:
        edges[_] = list(edges[_])

    return N, M, X, K, edges

def answer(n, x, graph):
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][k] + graph[k][x]

    if distance >= 1e9:
        return -1
    else:
        return distance
    

def convert_graph(edges):
    n = max(edges.keys()) + 1
    INF = 1000000000

    graph = [[INF] * n for _ in range(n)]

    for i in range(1, n):
        graph[i][i] = 0
        for j in edges[i]:
            graph[i][j] = 1

    return graph

if __name__ == '__main__':

    # N, M, edges, X, K = get_input()

    N = 5
    M = 7
    X = 4
    K = 5
    edges = {1: [2, 3, 4], 2: [1, 4], 3: [1, 4, 5], 4: [1, 2, 3, 5], 5: [3, 4]}
    
    graph = convert_graph(edges)

    print(future_city(X, K, edges))
    print(answer(N, X, graph))