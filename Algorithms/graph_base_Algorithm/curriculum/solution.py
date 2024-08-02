from collections import deque
import copy

class defaultDict(dict):
    def __init__(self, default_factory):
        self.default_factory = default_factory
    
    def __missing__(self, key):
        self[key] = self.default_factory()
        return self[key]

def my_curriculum_1(N):

    lectures = range(1, N+1)
    prerequisite_courses = {}
    required_time = {}

    for lecture in lectures:
        user_input = [int(num) for num in input('user input: ').split()]
        required_time[lecture] = user_input[0]
        prerequisite_courses[lecture] = user_input[1:-1]

        if prerequisite_courses[lecture]:
            courses = []
            for course in prerequisite_courses[lecture]:
                courses.append(required_time[course])
            cost = max(courses)
            required_time[lecture] += cost

    return required_time

def my_curriculum_2(N):
    
    lectures = range(1, N+1)
    required_time = {}
    prerequisite_courses = {}

    for lecture in lectures:
        user_input = [int(num) for num in input('user input: ').split()]
        required_time[lecture] = user_input[0]
        prerequisite_courses[lecture] = user_input[1:-1]

    memo = {}

    def calculate_time(lecture):
        if lecture in memo:
            return memo[lecture]
        if not prerequisite_courses[lecture]:
            memo[lecture] = required_time[lecture]
            return required_time[lecture]
        max_time = 0
        for course in prerequisite_courses[lecture]:
            max_time = max(max_time, calculate_time(course))
        memo[lecture] = required_time[lecture] + max_time
        return memo[lecture]

    for lecture in range(1, N+1):
        calculate_time(lecture)

    return memo

def my_curriculum_3(N):
    lectures = range(1, N+1)
    prerequisite_courses = defaultDict(list)
    required_time = {}
    in_degree = {i: 0 for i in lectures}

    for lecture in lectures:
        user_input = [int(num) for num in input('user input: ').split()]
        required_time[lecture] = user_input[0]
        for prereq in user_input[1:-1]:
            prerequisite_courses[prereq].append(lecture)
            in_degree[lecture] += 1

    queue = deque([lecture for lecture in lectures if in_degree[lecture] == 0])
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in prerequisite_courses[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    total_time = {lecture: required_time[lecture] for lecture in lectures}
    for lecture in order:
        for neighbor in prerequisite_courses[lecture]:
            total_time[neighbor] = max(total_time[neighbor], total_time[lecture] + required_time[neighbor])

    return total_time

def answer(v):
    indegree = [0] * (v + 1)
    graph = [[] for i in range(v + 1)]
    time = [0] * (v + 1)

    for i in range(1, v + 1):
        data = list(map(int, input().split()))
        time[i] = data[0] 
        for x in data[1:-1]:
            indegree[i] += 1
            graph[x].append(i)

    def topology_sort():
        result = copy.deepcopy(time)
        q = deque() 

        for i in range(1, v + 1):
            if indegree[i] == 0:
                q.append(i)

        while q:
            now = q.popleft()
            for i in graph[now]:
                result[i] = max(result[i], result[now] + time[i])
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        for i in range(1, v + 1):
            print(result[i])

    topology_sort()

if __name__ == '__main__':

    N = 5

    print(my_curriculum_3(N))