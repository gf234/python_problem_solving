import heapq
import math
import sys

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append((b, t))
start, end = map(int, input().split())


def bfs(start):
    pq = []
    pq.append((0, start))

    dist = [math.inf for _ in range(n+1)]
    dist[start] = 0
    while pq:
        d, here = heapq.heappop(pq)

        for there, td in adj[here]:
            nd = d + td
            if dist[there] > nd:
                dist[there] = nd
                heapq.heappush(pq, (nd, there))
    return dist


dist = bfs(start)
print(dist[end])
