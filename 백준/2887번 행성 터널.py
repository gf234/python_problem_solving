import sys
import math
import heapq


def input(): return sys.stdin.readline().rstrip()


n = int(input())
xs = []
ys = []
zs = []
for i in range(n):
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))
xs.sort()
ys.sort()
zs.sort()
# x,y,z 의 최소 거리를 구해서 저장한다.
# 전체를 구해서 저장하면 n*n 이 되지만 x,y,z 를 기준으로 가장 가까운 점들만 연결하는 방법으로 저장하면 3*(n-1)이 된다.
edges = []
for i in range(n-1):
    def add(loc):
        edges.append((loc[i+1][0]-loc[i][0], loc[i+1][1], loc[i][1]))
    add(xs)
    add(ys)
    add(zs)
edges.sort()

parents = [i for i in range(n)]


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return
    parents[pb] = pa
    return


def kruskal():
    ret = 0
    for dist, i, j in edges:
        if find(i) == find(j):
            continue
        ret += dist
        union(i, j)
    return ret


print(kruskal())
