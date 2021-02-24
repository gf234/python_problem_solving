import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


v, e = map(int, input().split())
pq = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, (c, a, b))


def find(parent, e):
    if parent[e] == e:
        return e
    parent[e] = find(parent, parent[e])
    return parent[e]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(n, pq):
    parent = [i for i in range(n+1)]

    ret = 0

    while pq:
        cost, a, b = heapq.heappop(pq)

        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            ret += cost
    return ret


print(kruskal(v, pq))
