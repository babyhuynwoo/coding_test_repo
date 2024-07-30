import heapq
import pprint

class defaultDict(dict):
    def __init__(self, default_factory):
        self.default_factory = default_factory

    def __missing__(self, key):
        self[key] = self.default_factory()
        return self[key]

NOT_CONNECTED = 1e9

def get_input():

    N, M, start = [int(num) for num in input('input N, M, start: ').split()]

    graph = {}

    for _ in range(N+1):
        graph[_] = {}

    for _ in range(M):
        tmp = [int(user_input) for user_input in input('edges: ').split()]
        graph[tmp[0]][tmp[1]] = tmp[2]

    return graph, start


def telegram(N, M, graph, start):

    que = [(0, start)]
    distance = [NOT_CONNECTED] * (N+1)
    distance[start] = 0
    visited = set()

    while que:
        dist, node = heapq.heappop(que)

        if dist > distance[node]:
            continue

        neighbors = graph[node].keys()

        for neighbor in neighbors:
  
            cost = graph[node][neighbor]

            if distance[neighbor] > cost:
                distance[neighbor] = cost + dist
                heapq.heappush(que, (cost, neighbor))
                visited.add(neighbor)

    
    city = len(visited)

    return city, dist


if __name__ == '__main__':


    N = 4
    M = 2
    start = 1
    graph = {0: {}, 1: {2: 4}, 2: {}, 3: {}, 4: {}}

    print(telegram(N, M, graph, start))
