import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
    heapq.heappush(edges, (c, a, b))

parents = [i for i in range(n+1)]


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal():
    ret = 0
    for _ in range(n-2):
        while edges:
            c, a, b = heapq.heappop(edges)

            if find(a) != find(b):
                union(a, b)
                ret += c
                break
    return ret


print(kruskal())
