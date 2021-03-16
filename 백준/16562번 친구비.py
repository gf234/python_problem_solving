import sys
import heapq


def input(): return sys.stdin.readline().rstrip()


n, m, k = map(int, input().split())
prices = list(map(int, input().split()))
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(edges, (0, a, b))
for i in range(n):
    heapq.heappush(edges, (prices[i], 0, i+1))

parents = [i for i in range(n+1)]


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal():
    ret = 0
    for _ in range(n):
        while edges:
            cost, a, b = heapq.heappop(edges)

            if find(a) != find(b):
                union(a, b)
                ret += cost
                if ret > k:
                    return 'Oh no'
                break
    return ret


print(kruskal())
