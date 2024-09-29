class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1


"""
# example

djs = DisjointSets(5)
for i in range(5):
    print(djs.findset(i))

djs.union(3,4)
print(djs.findset(3), djs.findset(4))

djs.union(4,1)
print(djs.findset(4), djs.findset(1))

"""
