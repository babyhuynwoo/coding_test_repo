class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        # 경로 압축
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            # 랭크에 따른 합병
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def make_set(n):
    parent = list(range(n))
    rank = [0] * n
    return parent, rank

def find(parent, u):
    # 경로 압축
    if parent[u] != u:
        parent[u] = find(parent, parent[u])
    return parent[u]

def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)
    
    if root_u != root_v:
        # 랭크에 따른 합병
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1


if __name__ == '__main__':
    n = 10
    
    parent, rank = make_set(n)
    union(parent, rank, 0, 1)
    union(parent, rank, 1, 2)
    union(parent, rank, 2, 3)
    union(parent, rank, 4, 5)
    union(parent, rank, 5, 6)
    union(parent, rank, 6, 7)
    union(parent, rank, 7, 8)
    union(parent, rank, 8, 9)

    print(find(parent, 0))
    print(find(parent, 1))
    print(find(parent, 2))
    print(find(parent, 3))
    print(find(parent, 4))
    print(find(parent, 5))
    print(find(parent, 6))
    print(find(parent, 7))
    print(find(parent, 8))
    print(find(parent, 9))
    


    # uf = UnionFind(n)
    # uf.union(0, 1)
    # uf.union(1, 2)
    # uf.union(2, 3)
    # uf.union(4, 5)
    # uf.union(5, 6)
    # uf.union(6, 7)
    # uf.union(7, 8)
    # uf.union(8, 9)
    
    # print(uf.find(0))  
    # print(uf.find(1))
    # print(uf.find(2))
    # print(uf.find(3))
    # print(uf.find(4))
    # print(uf.find(5))
    # print(uf.find(6))
    # print(uf.find(7))
    # print(uf.find(8))
    # print(uf.find(9))