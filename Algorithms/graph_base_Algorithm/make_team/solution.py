
def find_perent(parent, x):

    if parent[x] != x:
        parent[x] = find_perent(parent, parent[x])

    return parent[x]

def union(parent, u, v):
    node_u = find_perent(parent, u)
    node_v = find_perent(parent, v)

    if node_u != node_v:
        parent[v] = node_u
    else:
        pass

def get_input():
    N, M = [int(num) for num in input('input N, M: ').split()]

    parent = list(range(N+1))

    for _ in range(M):
        c, a, b = [int(num) for num in input('cal, st1, st2: ').split()]
        if c == 0:
            union(parent, a, b)
        else:
            if parent[a] == parent[b]:
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    get_input()