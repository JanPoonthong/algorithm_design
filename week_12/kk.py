from disjointsets3 import DisjointSets

V, E = map(int, input().split())
edges = []
for _ in range(E):
    V1, V2, W = map(int, input().split())
    edges.append((V1, V2, W))

def getKey(x):
    return x[2]

edges.sort(key=getKey)
print(edges)

djs = DisjointSets(V)
# for i in range(V):
#     print(djs.findset(i))


total_weight = 0
for edge in edges:
    # v1 = edge[0], v2 = edge[1], w = edge[2]
    if djs.findset(edge[0]) != djs.findset(edge[1]):
        total_weight += edge[2]
        djs.union(edge[0], edge[1])
        print(djs.findset(edge[0]), djs.findset(edge[1]))
print(total_weight)


#OR
for v1,v2,w in edges:
    # v1 = edge[0], v2 = edge[1], w = edge[2]
    if djs.findset(v1) != djs.findset(v2):
        total_weight += w
        djs.union(v1, v2)
        print(djs.findset(v1), djs.findset(v2))
print(total_weight)
