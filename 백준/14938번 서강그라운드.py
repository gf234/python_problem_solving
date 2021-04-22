import sys
import math
import heapq


def input(): return sys.stdin.readline().rstrip()


n, m, r = map(int, input().split())
numItems = [-1] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    adj[a].append((b, l))
    adj[b].append((a, l))


def bfs(start):
    q = [(0, start)]
    dist = [math.inf for _ in range(n+1)]
    dist[start] = 0
    ret = 0
    while q:
        d, here = heapq.heappop(q)
        if dist[here] < d:
            continue
        ret += numItems[here]
        for there, l in adj[here]:
            nd = d + l
            if nd <= m and dist[there] > nd:
                dist[there] = nd
                heapq.heappush(q, (nd, there))
    return ret


def findMaxItems():
    ret = 0
    for i in range(1, n+1):
        ret = max(ret, bfs(i))
    return ret


answer = findMaxItems()
print(answer)
