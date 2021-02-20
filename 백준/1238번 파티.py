from collections import defaultdict
import math
import sys
import heapq

n, m, x = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((t, b))


def bfs(start):
    pq = []
    pq.append((0, start))

    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    while pq:
        d, here = heapq.heappop(pq)

        for td, there in adj[here]:
            nd = d+td
            if dist[there] > nd:
                dist[there] = nd
                heapq.heappush(pq, (nd, there))
    return dist


answer = 0
for i in range(1, n+1):
    if i == x:
        continue

    dist1 = bfs(i)
    dist2 = bfs(x)

    answer = max(answer, dist1[x]+dist2[i])
print(answer)
