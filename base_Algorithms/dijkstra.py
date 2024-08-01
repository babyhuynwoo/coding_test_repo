import heapq

def dijkstra(graph, start, end):
    # 우선순위 큐 초기화
    queue = [(0, start)]  # (거리, 노드)
    distances = {start: 0}
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node in visited:
            continue

        visited.add(current_node)

        # 종료 조건: 목적지에 도달했을 때
        if current_node == end:
            return current_distance

        # 인접 노드에 대한 거리 갱신
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return -1  # 경로가 없는 경우

# 가중치 그래프 정의 (인접 리스트 형식)
graph = {
    1: [(2, 1), (3, 4)],
    2: [(1, 1), (3, 2), (4, 7)],
    3: [(1, 4), (2, 2), (4, 3)],
    4: [(2, 7), (3, 3)]
}

# 시작 노드와 끝 노드 설정
start_node = 1
end_node = 4
shortest_distance = dijkstra(graph, start_node, end_node)
print(f"The shortest distance between node {start_node} and node {end_node} is {shortest_distance}")