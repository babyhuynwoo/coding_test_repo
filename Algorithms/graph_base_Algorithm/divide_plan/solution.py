
def find_parent(parent, x):

    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union(parent, u, v):

    u_parent = find_parent(parent, u)
    v_parent = find_parent(parent, v)

    if u_parent != v_parent:
        parent[v] = u_parent
        return True

def divide_plan():
    N, M = [int(num) for num in input('input N,M: ').split()]

    costs = {}
    parent = list(range(N+1))

    for _ in range(M):
        u, v, cost = [int(var) for var in input('input a, b, c: ').split()]
        costs[(u,v)] = cost

    cost_keys = sorted(costs, key=lambda k: costs[k])

    result = 0

    for u, v in cost_keys:
        if union(parent, u, v):
            cost = costs[(u,v)]
            result += cost

    result -= cost
    return result 

if __name__ == '__main__':

    result = divide_plan()

    print(result)