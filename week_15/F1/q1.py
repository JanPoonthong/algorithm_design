from disjointsets3 import DisjointSets

V, E = map(int, input().split())
edges = []
for _ in range(E):
    V1, V2, W = map(int, input().split())
    edges.append((V1, V2, W))

def getKey(x):
    return x[2]


edges.sort(key=getKey)

djs = DisjointSets(V)

total_weight = 0
for v1, v2, w in edges:
    if djs.findset(v1) != djs.findset(v2):
        total_weight += w
        djs.union(v1, v2)
print(total_weight)
