import sys
import heapq
import math


def input(): return sys.stdin.readline().rstrip()


n = int(input())
stars = []
for _ in range(n):
    a, b = map(float, input().split())
    stars.append((a, b))


def dist(a, b):
    return math.sqrt(math.pow(abs(a[0]-b[0]), 2) + math.pow(abs(a[1]-b[1]), 2))


edges = []
for i in range(n):
    for j in range(i+1, n):
        d = dist(stars[i], stars[j])
        heapq.heappush(edges, (d, i, j))

parents = [i for i in range(n)]


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
    for _ in range(n-1):
        while edges:
            d, a, b = heapq.heappop(edges)

            if find(a) != find(b):
                ret += d
                union(a, b)
                break
    return ret


print(kruskal())
